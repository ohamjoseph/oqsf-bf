from typing import List

from fastapi import Depends

from models.particulier_model import ParticulierInfo
from repositories.particulier_repository import *
from schemas.particulier_schema import Particulier

class ParticulierService:
    '''
    Service responsable de la creation et de la mise a jour des objets *particulier*
    '''
    def __init__(self,particulier_repository: ParticulierRepository = Depends()) -> None:
        self.particulier_repository = particulier_repository
    
    def create_particulier(self, particulier: ParticulierCreate) -> ParticulierInfo:
        """
        Methode responsable de la creation des objets *particulier*
        :param particulier:
        :return: objets : Particulier
        """
        return self.particulier_repository.create_particulier(particulier=particulier)

    def get_particuliers(self) -> List[ParticulierInfo]:
        """
        Methode responsable de renvoyer  la liste des objets *particulier*
        :return: List[ParticulierInfo]
        """

        return self.particulier_repository.get_particuliers()

    def get_particulier_by_id(self, particulier_id: int) -> ParticulierInfo:
        """
        Methode responsable de la renvoyer des objets *particulier* en un id *particulier*
        :param particulier_id:
        :return: ParticulierInfo
        """

        return self.particulier_repository.get_particulier_by_id(particulier_id=particulier_id)

    def update_particulier(self,
                           particulier_id: int,
                           particulier: ParticulierCreate):
        """
        mise a jour d'un objet particulier
        :param particulier_id:
        :param particulier:
        :return: ParticulierInfo
        """
        return self.particulier_repository.update_particulier(
            particulier_id=particulier_id,
            particulier=particulier)

    def delete_particulier(self, particulier_id: int):
        """
        supprimer un objet particulier
        :param particulier_id:
        :return:
        """
        return self.particulier_repository.delete_particulier(
            particulier_id=particulier_id)


