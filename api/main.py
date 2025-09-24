from fastapi import FastAPI, HTTPException, Query, Path, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from database import SessionLocal
import query_helpers as helpers
import schema

api_description = """Bienvenue dans l'API Movielens"""

# ----------- Initialisation de l' application fastAPI
app = FastAPI(
    title="Movie API",
    description=api_description,
    version="0.1",
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ENdpoint pour tester la santé de l'API
@app.get(
    "/",
    summary="Verification de la santé de l'application",
    description="Vérifie si l'application fonctionne correctement",
    response_description="Statue de l'API - OK",
    operation_id="Health_check_movies_api",
    tags=["Monitoring"]
)
async def root():
    return {"message": "Movie API opérationnel et OK"}


@app.get("/movie/{movie_id}",
         summary="Obtenir un film par son ID",
         description=f"Retourne les informations d’un film en utilisant son `movieId`.",
         response_description="Détails du film",
         response_model=schema.MovieDetailed,
         tags=["films"],
         )
def read_movie(movie_id: int = Path(..., description="L'identifiant unique du film"), db: Session = Depends(get_db)):
    movie = helpers.get_movie(db, movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail=f"le film avec l'Id {movie_id} non trouvé")
    return movie


# Endpoint pour obtenir une liste des films (avec pagination et filtres facultatifs title, genre, skip, limit)
@app.get(
    "/movies",
    summary="Lister les films",
    description="Retourne une liste de films avec pagination et filtres optionnels par titre ou genre.",
    response_description="Liste de films",
    response_model=List[schema.MovieSimple],
    tags=["films"],
)
def list_movies(
        db: Session = Depends(get_db),
        skip: int = Query(0, description="Nombre de résultats à ignorer"),
        limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"),
        title: str = Query(None, description="Filtre par titre"),
        genre: str = Query(None, description="Filtre par genre"),
):
    movies = helpers.get_movies(db, skip=skip, limit=limit, title=title, genre=genre)
    return movies


# Endpoint pour obtenir une évaluation par utilisateur et film
@app.get(
    "/ratings/{user_id}/{movie_id}",
    summary="Obtenir une évaluation par utilisateur et film",
    description="Retourne l'évaluation d'un utilisateur pour un film donné.",
    response_description="Détails de l'évaluation",
    response_model=schema.RatingSimple,
    tags=["évaluations"],
)
def read_rating(
    user_id: int = Path(..., description="ID de l'utilisateur"),
    movie_id: int = Path(..., description="ID du film"),
    db: Session = Depends(get_db)
):
    rating = helpers.get_rating(db, user_id=user_id, movie_id=movie_id)
    if rating is None:
        raise HTTPException(
            status_code=404,
            detail=f"Aucune évaluation trouvée pour l'utilisateur {user_id} et le film {movie_id}"
        )
    return rating

# Endpoint pour obtenir une liste d’évaluations avec filtres
@app.get(
    "/ratings",
    summary="Lister les évaluations",
    description="Retourne une liste d’évaluations avec pagination et filtres optionnels (film, utilisateur, note min).",
    response_description="Liste des évaluations",
    response_model=List[schema.RatingSimple],
    tags=["évaluations"],
)
def list_ratings(
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"),
    movie_id: Optional[int] = Query(None, description="Filtrer par ID de film"),
    user_id: Optional[int] = Query(None, description="Filtrer par ID d'utilisateur"),
    min_rating: Optional[float] = Query(None, ge=0.0, le=5.0,
    description="Filtrer les notes supérieures ou égales à cette valeur"),
    db: Session = Depends(get_db)
):
    ratings = helpers.get_ratings(db, skip=skip, limit=limit, movie_id=movie_id, user_id=user_id, min_rating=min_rating)
    return ratings