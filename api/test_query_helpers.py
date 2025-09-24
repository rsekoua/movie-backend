#%%
from database import SessionLocal
from query_helpers import *

db = SessionLocal()

rating = get_rating(db,movie_id=1, user_id=1)
print(rating.movieId)

# #print(f"{rating.movieId}, {rating.userId}, {rating.rating}, {rating.timestamp}")
# print(ratings)
db.close()
