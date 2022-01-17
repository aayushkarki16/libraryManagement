from django import forms

from library.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookRegisterForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['book_id', 'name', 'author', 'price', 'type']


class BookBorrowForm(forms.ModelForm):
    class Meta:
        model = Bookrenew
        fields = ['student_name', 'student_id']
