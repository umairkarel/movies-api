from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

def current_year():
    return datetime.date.today().year

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    runtime = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    rating = models.FloatField()
    overview = models.TextField()
    meta_score = models.FloatField()
    director = models.CharField(max_length=20)
    votes = models.BigIntegerField()
    gross = models.BigIntegerField()
    poster_url = models.URLField()
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(current_year())])

    def __str__(self):
        return f"{self.title}"

class Genre(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"