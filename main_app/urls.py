from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome_page'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('profile/<int:pk>', login_required(views.ProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('books/', views.AllBooksView.as_view(), name='books'),
    path('book/<int:pk>/', views.SingleBook.as_view(), name='book'),
    path('search/', views.SearchView.as_view(), name='search'),
]
