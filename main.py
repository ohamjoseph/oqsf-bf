from fastapi import FastAPI
from database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
import reclamation



# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
""" app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["<votre-url-render>.onrender.com", "*.onrender.com"]
) """

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reclamation.router, tags=['Notes'], prefix='/api/reclamations')

@app.get("/")
def main():
    return "reclamation"
