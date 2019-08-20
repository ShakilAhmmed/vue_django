from django.db import models


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100, unique=True)
    roll = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
