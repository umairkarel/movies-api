from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

def current_year():
    return datetime.date.today().year

class Genre(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"

class Movie(models.Model):
    title = models.CharField(max_length=30)
    runtime = models.FloatField()
    genres = models.ManyToManyField(Genre)
    rating = models.FloatField()
    overview = models.TextField()
    director = models.CharField(max_length=20)
    poster_url = models.URLField()
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(current_year())])
    meta_score = models.FloatField(null=True)
    votes = models.BigIntegerField(null=True)
    gross = models.BigIntegerField(null=True)

    def __str__(self):
        return f"{self.title}"
