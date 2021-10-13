from django.urls import path
from . import views as apiView

urlpatterns = [
    path('', apiView.overview, name="api-overview"),
    path('movie-list/', apiView.movie_list, name='movie-list'),
    path('movie-detail/<int:pk>/', apiView.movie_detail, name='movie-detail'),
    path('movie-create/', apiView.create_movie, name='movie-create'),
    path('movie-update/<int:pk>/', apiView.movie_update, name='movie-update'),
    path('movie-delete/<int:pk>/', apiView.movie_delete, name='movie-delete'),
]