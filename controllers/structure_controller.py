from _ctypes import Structure

from fastapi import Depends

from schemas.structure_schema import StructureInfoCreate
from services.structure_services import StructureService


class StructureController:
    def __init__(self, structure_service: StructureService = Depends()):
        self._structure_service = structure_service

    def create_structure(self, structure: StructureInfoCreate):
        return self._structure_service.create_structure(structure)