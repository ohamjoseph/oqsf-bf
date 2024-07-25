from http.client import HTTPException
from typing import List

from fastapi import Depends

from models.particulier_model import ParticulierInfo
from services.particulier_service import *

class ParticulierController:
    """
    Controller class to handle all interactions with the particulier service
    """
    def __init__(self, particulier_service: ParticulierService = Depends()) -> None:
        self.particulier_service = particulier_service
    
    def create_particulier(self, particulier: ParticulierCreate) -> ParticulierInfo:
        """
        Methode de creation de un particulier.
        :param particulier: ParticulierInfo
        :return:
        """

        return self.particulier_service.create_particulier(
            particulier=particulier)

    def get_particuliers(self) -> list[ParticulierInfo]:
        """
        Methode de obtenir tous les particuliers.
        :return: list[ParticulierInfo]
        """
        return self.particulier_service.get_particuliers()

    def get_particulier_by_id(self, particulier_id: int) -> ParticulierInfo:
        """
        methode de obtenir un particulier.
        :param particulier_id:
        :return:
        """

        particulier = self.particulier_service.get_particulier_by_id(particulier_id)
        if particulier is None:
            raise HTTPException(status_code=404, detail="Particulier not found")
        return particulier

    def update_particulier(self,
                           particulier_id: int,
                           particulier: ParticulierCreate):

        updated_particulier = self.particulier_service.update_particulier(
            particulier_id=particulier_id,
            particulier=particulier)
        if updated_particulier is None:
            raise HTTPException(status_code=404, detail="Particulier not found")
        return updated_particulier

    def delete_particulier(self, particulier_id: int):
        """
        Methode de supprimer un particulier.
        :param particulier_id:
        :return:
        """
        delete_particulier = self.particulier_service.delete_particulier(
            particulier_id=particulier_id)
        if delete_particulier is None:
            raise HTTPException(status_code=404, detail="Particulier not found")

        return delete_particulier

