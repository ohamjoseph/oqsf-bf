from fastapi import Depends, HTTPException

from src.schemas.structure_schema import StructureInfoCreate
from src.services.structure_services import StructureService


class StructureController:
    def __init__(self, structure_service: StructureService = Depends()):
        self._structure_service = structure_service

    def create_structure(self, structure: StructureInfoCreate):
        return self._structure_service.create_structure(structure)

    def get_structure_by_id(self, structure_id: int):
        """
        recuperate structure by id
        :param structure_id: int
        :return:
        """
        structure = self._structure_service.get_structure_by_id(structure_id=structure_id)
        if structure is None:
            raise HTTPException(status_code=400,
                                detail='Structure not found')
        return structure

    def update_structure(self,
                         structure_id: str,
                         structure: StructureInfoCreate):
        """
        mise a jour d'une structure
        :param structure_id:
        :param structure:
        :return:
        """
        updated_structure = self._structure_service.update_structure(
            structure_id=int(structure_id),
            structure=structure)

        if updated_structure is None:
            raise HTTPException(status_code=400,
                                detail='Structure not found')
        return updated_structure

    def delete_structure(self, structure_id: str):
        """
        Supprimer une structure
        :param structure_id:
        :return:
        """
        delete_structure = self._structure_service.get_structure_by_id(
            structure_id=structure_id)

        if delete_structure is None:
            raise HTTPException(status_code=400,
                                detail='Structure not found')

        return delete_structure

    def get_structures(self):
        return self._structure_service.get_structures()
