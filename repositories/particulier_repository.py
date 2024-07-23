from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db


from models import particulier_model
from schemas.particulier_schema import ParticulierCreate

class ParticulierRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def create_particulier(self, particulier: ParticulierCreate) -> particulier_model.ParticulierInfo:
        
        particulier = particulier_model.ParticulierInfo(**particulier.model_dump())
        self.db.add(particulier)
        self.db.commit()
        self.db.refresh(particulier)

        return particulier
    
    def get_particuliers(db: Session, skip: int = 0, limit: int = 10):
        return db.query(particulier_model.ParticulierInfo).offset(skip).limit(limit).all()