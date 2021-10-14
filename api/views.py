from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from .models import Movie, Genre
from .serializers import MovieSerializer, GenreSerializer


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def overview(request):
    api_urls = {
        'Movies List':'api/movies/',
        'Movie Detail':'api/movies/<int:pk>/',
        'Genres List':'api/genres/',
        'Genre Detail':'api/genres/<int:pk>/',
        }

    return Response(api_urls)

class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailView(APIView):

    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreView(ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenreDetail(APIView):
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
