from django.urls import path
from .views import MovieListView, GenreView, MovieDetailView, GenreDetail, overview

urlpatterns = [
    path('', overview, name='overview'),
    path('movies/', MovieListView.as_view(), name='movies'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('genres/', GenreView.as_view(), name='genres'),
    path('genres/<int:pk>', GenreDetail.as_view(), name='genre-detail'),
]