from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db

from models import particulier_model
from schemas.particulier_schema import ParticulierCreate


class ParticulierRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def create_particulier(self,
                           particulier: ParticulierCreate
                           ) -> particulier_model.ParticulierInfo:
        """
        Permet de créer un nouveau particulier.
        :param particulier: ParticulierCreate
        :return particulier: Particulier
        """

        particulier = particulier_model.ParticulierInfo(**particulier.model_dump())
        self.db.add(particulier)
        self.db.commit()
        self.db.refresh(particulier)

        return particulier

    def get_particuliers(self, skip: int = 0, limit: int = 10):
        """
        Permet de recuperer une liste de particuliers.
        :param skip:
        :param limit:
        :return: Liste de particuliers
        """

        return self.db.query(particulier_model.ParticulierInfo).offset(skip).limit(limit).all()

    def get_particulier_by_id(self, particulier_id: int):
        """
        Permet de recuperer un particulier.
        :param particulier_id:
        :return: ParticulierInfo
        """
        return self.db.query(particulier_model.ParticulierInfo).filter(
            particulier_model.ParticulierInfo.id == particulier_id).first()

    def update_particulier(self,
                           particulier_id: int,
                           particulier: ParticulierCreate):
        """
        Permet de modifier un particulier.
        :param particulier_id:
        :param particulier:
        :return:
        """
        db_particulier = self.get_particulier_by_id(particulier_id)

        if db_particulier is None:
            return None

        for key, value in particulier.model_dump().items():
            setattr(db_particulier, key, value)
        self.db.commit()
        self.db.refresh(db_particulier)
        return db_particulier

    def delete_particulier(self, particulier_id: int):
        """
        Permet de supprimer un particulier.
        :param particulier_id:
        :return:
        """
        db_particulier = self.get_particulier_by_id(particulier_id)
        if db_particulier is None:
            return None

        self.db.delete(db_particulier)
        self.db.commit()

        return db_particulier
