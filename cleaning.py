# from api.models import Movie
import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('movies.csv')
# print(df.info())
# df.Released_Year = df.Released_Year.apply(lambda x: pd.to_numeric(x, errors='coerce'))
# df.Runtime = df.Runtime.apply(lambda x: float(x.split()[0]))
# df.Gross = df.Gross.apply(lambda x: int(''.join(x.split(','))))

# df.dropna(inplace=True)
# df.to_csv('movies.csv')

genres = pd.unique(df["Genre"].str.split(", ", expand=True).stack())
for genre in genres:
    Genre.objects.create(name=genre)




for i in range(df.shape[0]):
    row = df.iloc[i]
    genres = row.Genre

    m = Movie(title=row.Series_Title, 
          runtime=row.Runtime, 
          rating=row.IMDB_Rating, 
          overview=row.Overview,
          meta_score=row.Meta_score,
          director=row.Director,
          votes=row.No_of_Votes,
          gross=row.Gross,
          year=row.Released_Year,
          poster_url=row.Poster_Link
          )

        # print(genre, type(genre))
    for genre in genres.split(', '):
        genre_obj = Genre.objects.get(name=genre)
        m.genres.add(genre_obj)


    # m.save()









# class MovieViewSet(viewsets.ModelViewSet):
#     serializer_class = MovieSerializer

#     def get_queryset(self):
#         movie = Movie.objects.all()
#         return movie

#     def create(self, request, *args, **kwargs):
#         data = request.data

#         new_movie = Movie.objects.create(
#               title     = data['title'], 
#               runtime   = data['runtime'], 
#               rating    = data['rating'], 
#               overview  = data['overview'],
#               meta_score= data['meta_score'],
#               director  = data['director'],
#               votes     = data['votes'],
#               gross     = data['gross'],
#               year      = data['year'],
#               poster_url= data['poster_url'])

#         new_movie.save()

#         for genre in data["genres"]:
#             genre_obj = Genre.objects.get(name=genre["name"])
#             new_movie.genres.add(genre_obj)

#         serializer = MovieSerializer(new_movie)

#         return Response(serializer.data)


# class GenreViewSet(viewsets.ModelViewSet):
#     serializer_class = GenreSerializer

#     def get_queryset(self):
#         genre = Genre.objects.all()
#         return genre