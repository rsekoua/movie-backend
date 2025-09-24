from database import SessionLocal
from query_helpers import *

db = SessionLocal()

ratings = get_link_count(db)
""" for film in ratings:
    print(f"Movie Id: {film.movieId}, User Id: {film.userId}, Titre: {film.rating}") """

#print(f"{rating.movieId}, {rating.userId}, {rating.rating}, {rating.timestamp}")
print(ratings)
db.close()
