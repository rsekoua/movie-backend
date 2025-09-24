
"""Database configuration"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker



# 1. Obtenir le chemin absolu du répertoire où se trouve ce fichier (database.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Construire le chemin complet vers le fichier de base de données
DATABASE_PATH = os.path.join(BASE_DIR, "movies.db")

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# # Créer un moteur de base de données (engine) qui établit la connexion avec notre base SQLite (movies.db).
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, #pool_pre_ping=True
)

# Définir SessionLocal, qui permet de créer des sessions pour interagir avec la base de données.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définir Base, qui servira de classe de base pour nos modèles SQLAlchemy.
Base = declarative_base()

# if __name__ == "__main__":
#     try:
#         with engine.connect() as conn:
#             print("Connexion à la database réussie")
#     except Exception as e:
#         print(f"Erreur de connexion à la database : {e}")