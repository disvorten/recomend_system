import keras
import pandas as pd
from django.contrib import auth
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, TemplateView, ListView, UpdateView, CreateView

from common.views import TitleMixin
from main_app import tasks
from main_app.forms import UserRegistrationForm, UserLoginForm, UserProfileForm, RatingForm
from main_app.models import User, Books, Ratings
from ml.main import training, predict


class UserLoginView(TitleMixin, LoginView):
    template_name = 'main_app/login.html'
    form_class = UserLoginForm
    title = 'Login'


class RegisterView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'main_app/registration.html'
    success_url = reverse_lazy('welcome_page')
    success_message = 'Вы успешно зарегистрированы!'
    title = 'Registration'


class ProfileView(TitleMixin, UpdateView):
    model = User
    template_name = 'main_app/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('profile')
    title = 'Profile'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data()
        context['user'] = self.request.user
        if context['user'].checked_items != '':
            context['checked_books'] = [Books.objects.get(id=elem) for elem in
                                        list(map(int, context['user'].checked_items.split(',')))]
        else:
            context['checked_books'] = ''
        if context['user'].read_books != '':
            context['read_books'] = [Books.objects.get(id=elem) for elem in
                                     list(map(int, context['user'].read_books.split(',')))]
        else:
            context['read_books'] = ''
        return context


class WelcomeView(TitleMixin, TemplateView):
    template_name = 'main_app/welcome_page.html'
    title = 'Welcome page'

    def get_context_data(self, **kwargs):
        context = super(WelcomeView, self).get_context_data()
        context['books'] = Books.objects.all()
        if not self.request.user.id:
            context['IsAuth'] = False
        else:
            context['IsAuth'] = True
        context['user'] = self.request.user
        return context


class SearchView(TitleMixin, ListView):
    template_name = 'main_app/search.html'
    model = Books
    title = None
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        self.title = f'Search: {query}'
        object_list = Books.objects.filter(
            Q(authors__icontains=query) | Q(title__icontains=query)
        )
        return object_list


class AllBooksView(TitleMixin, ListView):
    template_name = 'main_app/list_of_books.html'
    model = Books
    title = 'All books'
    paginate_by = 10

    @staticmethod
    def create_dataset(path):
        df = pd.DataFrame(o.__dict__ for o in Ratings.objects.all())
        df.to_csv(path)
        dataset = pd.read_csv(path)
        dataset.sort_values(by='book_id', inplace=True)
        return dataset

    @staticmethod
    def create_and_save_model(dataset, path):
        model = training(dataset)
        model.save('main_app/data_for_ml/model')

    def get_context_data(self, **kwargs):
        context = super(AllBooksView, self).get_context_data()
        context['books'] = Books.objects.all()
        context['ratings'] = Ratings.objects.filter(user_id=self.request.user.id)
        user = User.objects.get(id=self.request.user.id)
        if not user.model_existence:
            tasks.create_model.delay('main_app/data_for_ml/ratings.csv', 'main_app/data_for_ml/model')
            user.model_existence = True
            user.save()
        # tasks.use_model.delay(user.id, 'main_app/data_for_ml/ratings.csv', 'main_app/data_for_ml/model')
        if user.recomm_books == '':
            context['recomm_books'] = ''
        else:
            context['recomm_books'] = Books.objects.filter(pk__in=list(sorted(map(int, user.recomm_books.split(',')))))
        return context


class SingleBook(TitleMixin, DetailView):
    model = Books
    template_name = 'main_app/single_book.html'
    context_object_name = 'book'
    success_url = reverse_lazy('book')

    def get_context_data(self, **kwargs):
        book = self.kwargs.get('pk')
        context = super(SingleBook, self).get_context_data()
        context['books'] = Books.objects.all()
        context['user'] = self.request.user
        user = User.objects.get(id=context['user'].id)
        cur_book = Books.objects.get(id=book)
        context['form'] = RatingForm()
        context['title'] = cur_book.title
        if Ratings.objects.filter(user=user, book=cur_book):
            context['IsRated'] = True
            context['rate'] = Ratings.objects.get(user=user, book=cur_book).rating
        else:
            context['IsRated'] = False
            context['rate'] = None
        if context['user'].read_books != '':
            context['IsinRead'] = book in list(map(int, context['user'].read_books.split(',')))
        else:
            context['IsinRead'] = False
        if self.request.GET.get('Add') == '':
            if not context['IsinRead']:
                if context['user'].read_books == '':
                    user.read_books = str(book)
                else:
                    user.read_books = ','.join([context['user'].read_books, str(book)])
                user.save()
        if context['user'].checked_items != '' and book not in list(map(int, context['user'].checked_items.split(','))):
            user.checked_items = ','.join([context['user'].checked_items, str(book)])
            user.save()
        elif context['user'].checked_items == '':
            user.checked_items = str(book)
            user.save()
        return context

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.get(id=request.user.id)
        self.object = self.get_object()
        context = self.get_context_data(**kwargs)
        if request.method == 'POST':
            rating = self.request.POST['rating']
            cur_book = Books.objects.get(id=pk)
            if not context['IsRated']:
                Ratings.objects.create(rating=rating, user=user, book=cur_book)
            else:
                rate = Ratings.objects.get(user=user, book=cur_book)
                rate.rating = rating
                rate.save()
            context['IsRated'] = True
            context['rate'] = rating
            user.model_existence = False
            user.save()
            return self.render_to_response(context)
