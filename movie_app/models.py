from django.db import models
from django.urls import reverse


# Create your models here.
# Создание таблицы Movie
#  колонками name varchar=40 and rating integer колонка id создается автоматически
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=1000000)

    def get_url(self):
        return reverse('movie_detail', args=[self.id])

    def __str__(self):
        return f'{self.name} - {self.rating}% {self.year}'


# from book_app.models import Book
# from movie_app.models import Movie

