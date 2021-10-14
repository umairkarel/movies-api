# Movies API

## Setup
1. Fork this repo.
2. 
    ```shell
        python manage.py makemigrations
        python manage.py migrate 
    ```
3. Loading Movies data to the Database
    ```shell
        python manage.py shell
    ``` 
    Paste this program in the shell and run
    ```python
        import pandas as pd
        from api.models import Movie, Genre
        df = pd.read_csv('movies.csv')
        
        # Loading Genres
        genres = pd.unique(df["Genre"].str.split(", ", expand=True).stack())
        for genre in genres:
            Genre.objects.create(name=genre)
        
        # Loading Movies
        for i in range(df.shape[0]):
            row = df.iloc[i]
            genres = row.Genre
            
            # Creating movie object for each row in csv
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
            # Saving the Movie Object first to add genres later
            m.save()
            
            # Linking all the genres of current Movie with genre object 
            for genre in genres.split(', '):
                genre_obj = Genre.objects.get(name=genre)
                m.genres.add(genre_obj)
    ```

Congrats! Your database is ready. Now you can use the API
## API

### Show Movies
---
Returns JSON data of all the Movies
* **URL**
  `api/movies/`

* **Method:**
    `GET` | `POST` 
  
* **Data Params**
structure of JSON for POST request
    ```
    {
        "title": "",
        "runtime": null,
        "genres": [],
        "rating": null,
        "overview": "",
        "director": "",
        "poster_url": "",
        "year": null
    }
    ```

* **Success Response:**
    **GET**
    ***Code***: 200 <br />
    
      **POST**
    ***Code*:** 201 <br />
 
* **Error Response:**
  * **Code:** 403 Forbidden <br />
    **Content:** `{  "detail":  "Authentication credentials were not provided."  }`

* **Sample Call:**
```python
import requests

# GET
response = requests.get('http://localhost:8000/api/movies/').json()

data = {
    "title": "Hello World",
    "runtime": 175.0,
    "genres": [
        1, 2
    ],
    "rating": 9,
    "overview": "...",
    "director": "Sample",
    "poster_url": "https://github.com",
    "year": 2000
}

# POST
response = requests.post('http://localhost:8000/api/movies/', data)
```


### Movie Detail
---
Returns JSON data of all single Movie
* **URL**
  `api/movies/<int:pk>`

* **Method:**
    `GET` | `PUT` | `DELETE`
  
* **Success Response:**
    * **Code**: 200 <br />
 
* **Error Response:**
  * **Code:** 403 Forbidden <br />
    **Content:** `{  "detail":  "Authentication credentials were not provided."  }`

* **Sample Call:**
```python
import requests

response = requests.get('http://localhost:8000/api/movies/20').json()
```


### Show Genres
---
Returns JSON data of all the Genres
* **URL**
  `api/genres/`

* **Method:**
    `GET` | `POST`  
 * **Data Params**
structure of JSON for POST request
    ```
    {
        "name": ""
    }
    ```
* **Success Response:**
    **GET**
    ***Code***: 200 <br />

     **POST**
    ***Code*:** 201 <br />
 
* **Error Response:**
  * **Code:** 403 Forbidden <br />
    **Content:** `{  "detail":  "Authentication credentials were not provided."  }`

* **Sample Call:**
```python
import requests

# GET
response = requests.get('http://localhost:8000/api/genres/').json()

data = { "name": "Animation" }

# POST
response = requests.post('http://localhost:8000/api/genres/', data).json()

```


### Genre Detail
---
Returns JSON data of single genre
* **URL**
  `api/genres/<int:pk>`

* **Method:**
    `GET` | `PUT` | `DELETE`
  
* **Success Response:**
    * **Code**: 200 <br />
 
* **Error Response:**
  * **Code:** 403 Forbidden <br />
    **Content:** `{  "detail":  "Authentication credentials were not provided."  }`

* **Sample Call:**
```python
import requests

response = requests.get('http://localhost:8000/api/genres/2').json()
```