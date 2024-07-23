from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from models import structure_model
from schemas import structure_schema


class StructureRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def create_particulier(self, structure: structure_schema.StructureInfoCreate) -> structure_model.StructureInfo:
        structure = structure_model.StructureInfo(**structure.model_dump())
        self.db.add(structure)
        self.db.commit()
        self.db.refresh(structure)

        return structure

    def get_particuliers(db: Session, skip: int = 0, limit: int = 10):
        return db.query(structure_model.StructureInfo).offset(skip).limit(limit).all()