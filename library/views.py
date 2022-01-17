from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, redirect


# Create your views here.
from library.form import *
from .models import *


def index(request):
    books = Books.objects.all()
    return render(request, 'library/index.html', {'books': books})


def log(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
    else:
        return render(request, 'library/log.html')


def log_out(request):
    logout(request)
    return redirect('log')


def register(request):
    if request.method == "POST":
        form = BookRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookRegisterForm()
        return render(request, 'library/register.html', {'form': form})


def borrow(request):
    if request.method == "POST":
        form = BookBorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookBorrowForm()
        return render(request, 'library/borrow.html', {'form': form})

