
# %%
from argparse import Action

from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

# %%
#Tester la récupération de quelques films
#movies = db.query(Movie).limit(10).all()
#actions = db.query(Movie).filter(Movie.genres.like("%Action%")).limit(5).all()
#for movie in movies:
#    print(f"Id : {movie.movieId}, Title: {movie.title}, genres; {movie.genres}")

# for movie in actions:
#     print(f"Id : {movie.movieId}, Title: {movie.title}, genres; {movie.genres}")



# %%
""" hight_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating, Movie.movieId == Rating.movieId)
    .filter(Rating.rating >= 4)
    .limit(5)
    .all()
)

for title,rating in hight_rated_movies:
    print(title,rating) """

# %%
# Recupération au tags  associés aux films
links = db.query(Link).limit(10).all()

for link in links:
    print(f"Movie Id: {link.movieId}, ImdbID: {link.imdbId}, TMDB ID: {link.tmdbId}")
    

# %%
