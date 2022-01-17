from django.urls import path

from library import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('', views.log, name="log"),
    path('log_out', views.log_out, name="log_out"),
    path('register', views.register, name="register"),
    path('borrow', views.borrow, name="borrow"),
]
