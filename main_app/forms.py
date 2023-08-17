from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import CharField

from .models import User, Ratings


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text",
        'name': "u", 'placeholder': "Username", 'required': "required"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password",
        'name': "p", 'placeholder': 'Password', 'required': "required"}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = None

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=True)
        return user

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4'}))
    read_books = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'read_books')


class RatingForm(forms.Form):
    rating = forms.ChoiceField(choices=[(f'{i}', f'{i}') for i in range(1, 6)], widget=forms.Select(attrs={
        'class': 'form-control py-4'}))
