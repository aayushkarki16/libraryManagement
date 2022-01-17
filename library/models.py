from django.db import models

# Create your models here.


class Books(models.Model):
    book_id = models.IntegerField(max_length=200, default="")
    name = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=200, default="")
    price = models.IntegerField(max_length=200, default="")
    type = models.CharField(max_length=200, default="")


class Students(models.Model):
    student_id = models.IntegerField(max_length=200, default="")
    name = models.CharField(max_length=200, default="")
    batch = models.CharField(max_length=200, default="")


class BookBorrow(models.Model):
    student_name = models.CharField(max_length=200, default="")
    student_id = models.IntegerField(max_length=200, default="")

