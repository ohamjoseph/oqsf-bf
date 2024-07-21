from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine, Base
from models import PersonalInfo, Saisine
from fastapi.middleware.cors import CORSMiddleware
from schemas import PersonalInfoCreate, PersonalInfo, SaisineCreate, Saisine


# Création des tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dépendance de session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return "reclamation"

@app.post("/reclamations/", response_model=Saisine)
def create_reclamation(personal_info: PersonalInfoCreate, saisine: SaisineCreate, db: Session = Depends(get_db)):
    print(f"************* {personal_info}")
    print(f"************* {saisine}")
    db_personal_info = PersonalInfo(**personal_info.model_dump())
    db.add(db_personal_info)
    db.commit()
    db.refresh(db_personal_info)
    
    db_saisine = Saisine(**saisine.model_dump(), personal_info_id=db_personal_info.id)
    db.add(db_saisine)
    db.commit()
    db.refresh(db_saisine)
    return db_saisine

@app.get("/reclamations/", response_model=List[Saisine])
def read_reclamations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reclamations = db.query(Saisine).offset(skip).limit(limit).all()
    return reclamations

@app.get("/reclamations/{numero_membre}", response_model=Saisine)
def read_reclamation(numero_membre: str, db: Session = Depends(get_db)):
    reclamation = db.query(Saisine).join(PersonalInfo).filter(PersonalInfo.numero_membre == numero_membre).first()
    if not reclamation:
        raise HTTPException(status_code=404, detail="Reclamation not found")
    return reclamation

# Pour lancer l'application, exécute cette commande dans le terminal:
# uvicorn main:app --reload
