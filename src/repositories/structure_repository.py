from http.client import HTTPException

from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from src.models import structure_model
from src.schemas import structure_schema


class StructureRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def create_structure(self,
                           structure: structure_schema.StructureInfoCreate
                           ) -> structure_model.StructureInfo:
        """
        permet de créer une structure
        :param structure:
        :return:
        """
        structure = structure_model.StructureInfo(**structure.model_dump())
        self.db.add(structure)
        self.db.commit()
        self.db.refresh(structure)

        return structure

    def get_structures(self, skip: int = 0, limit: int = 10):
        return self.db.query(structure_model.StructureInfo).offset(skip).limit(limit).all()

    def get_structure_by_id(self, structure_id: int):
        """
        Permet de récuperer une structure.
        :param structure_id:
        :return: StructureInfo
        """
        structure = (self.db.query(
            structure_model.StructureInfo).
                     filter_by(id=structure_id).first())
        if structure is None:
            raise HTTPException(status_code=404, detail="Structure not found")
        return self.db.query(structure_model.StructureInfo).filter(
            structure_model.StructureInfo.id == structure_id).first()

    def update_structure(self,
                         structure_id: int,
                         structure: structure_schema.StructureInfoCreate):
        """
        Permet de modifier un structure.
        :param structure_id: int
        :param structure: StructureInfoCreate
        :return:
        """
        db_structure = self.get_structure_by_id(structure_id)

        if db_structure is None:
            raise HTTPException(status_code=404, detail="Structure not found")

        for key, value in structure.model_dump().items():
            setattr(db_structure, key, value)
        self.db.commit()
        self.db.refresh(db_structure)
        return db_structure

    def delete_structure(self, structure_id: int):
        """
        Permet de supprimer une structure.
        :param structure_id: int
        :return:
        """
        db_structure = self.get_structure_by_id(structure_id)
        if db_structure is None:
            raise HTTPException(status_code=404, detail="Structure not found")

        self.db.delete(db_structure)
        self.db.commit()

        return db_structure

