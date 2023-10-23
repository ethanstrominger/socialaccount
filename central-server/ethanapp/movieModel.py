from django.contrib.auth import admin
from django.db import models
from django.urls import reverse
from .models import Person


# Create your models here.


class Movie(models.Model):
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class MoviePerson(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, blank=True)

    class Meta:
        unique_together = (
            "movie",
            "person",
        )

    def __str__(self):
        return self.movie.__str__() + " / " + self.movie.__str__()




