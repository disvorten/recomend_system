from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from main_app.models import User, Books


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.path = reverse('registration')
        self.data = {'username': 'qwerty', 'fisrt_name': 'qwe', 'last_name': 'qwerwqr', 'password': '123456'}

    def test_user_reg_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Registration')
        self.assertTemplateUsed(response, 'main_app/registration.html')

    def test_user_reg_post(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertRedirects(response, reverse('welcome_page'))
        self.assertTrue(User.objects.filter(username=username).exists())


class WelcomeViewTestCase(TestCase):
    def test_welcome_page(self):
        path = reverse('welcome_page')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Welcome page')
        self.assertTemplateUsed(response, 'main_app/welcome_page.html')


class AllBooksTestCase(TestCase):
    def test_list(self):
        path = reverse('books')
        response = self.client.get(path)
        books = Books.objects.all()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'All books')
        self.assertTemplateUsed(response, 'main_app/list_of_books.html')
        self.assertEqual(list(response.context_data['books']), list(books[:10]))


class SingeBookTestCase(TestCase):
    def test_book(self):
        path = reverse('book')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # self.assertEqual(response.context_data['title'], )
        self.assertTemplateUsed(response, 'main_app/single_book.html')
