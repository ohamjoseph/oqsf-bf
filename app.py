from fastapi import FastAPI
from database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware

from routers import particulier_router, saisine_route, reclamation_router, structure_router

# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
""" app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["<votre-url-render>.onrender.com",
    "*.onrender.com"]
) """

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    particulier_router.router,
    tags=['particulier'],
    prefix='/api/particuliers')

app.include_router(
    saisine_route.router,
    tags=['saisine'],
    prefix='/api/saisines')

app.include_router(
    reclamation_router.router,
    tags=['reclamation'],
    prefix='/api/reclamations'
)

app.include_router(
    structure_router.router,
    tags=['structure'],
    prefix='/api/structures')


@app.get("/")
def main():
    return "reclamation"
