#%%
from database import SessionLocal
from query_helpers import *

db = SessionLocal()

#%%
rating = get_rating(db, movie_id=1, user_id=1)
""" for film in movies:
    print(f"Id: {film.movieId}, Titre: {film.title}, Genre :{film.genres}")
 """
print(f"{rating.movieId}, {rating.userId}, {rating.rating}, {rating.timestamp}")

db.close()

# %%
