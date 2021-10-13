from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "runtime", "genre", "rating", "overview", "director", "poster_url", "year")