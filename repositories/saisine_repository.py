from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from models import saisine_model
from schemas.saisine_schema import SaisineCreate


class SaisineRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None :
        self.db = db
    
    def create_saisine(self, saisine: SaisineCreate):
        saisine = saisine_model.Saisine(**saisine.model_dump())

        self.db.add(saisine)
        self.db.commit()
        self.db.refresh(saisine)

        return saisine


    def get_saisines(slef, skip: int = 0, limit: int = 10):
        return slef.db.query(saisine_model.Saisine).offset(skip).limit(limit).all()