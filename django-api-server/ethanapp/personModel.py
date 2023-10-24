from django.contrib import admin
from django.db import models
from django.urls import reverse


# Create your models here.


class Person(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

