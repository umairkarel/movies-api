from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
@api_view(['GET'])
def overview(request):
    api_urls = {
        'List':'/movie-list/',
        'Detail View':'/movie-detail/<str:pk>/',
        'Create':'/movie-add/',
        'Update':'/movie-update/<str:pk>/',
        'Delete':'/movie-delete/<str:pk>/',
        }

    return Response(api_urls)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(movie)

    return Response(serializer.data)

@api_view(['POST'])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def movie_update(request, pk):
    movie = Movie.objects.get(id=pk)
    serializer = MovieSerializer(instance=movie, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def movie_delete(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()

    return Response('Movie succsesfully deleted!')