from fastapi import Depends

from repositories.structure_repository import StructureRepository
from schemas.structure_schema import StructureInfoCreate


class StructureService:
    def __init__(self, structure_repository: StructureRepository= Depends()):
        self.structure_repository = structure_repository

    def create_structure(self, structure: StructureInfoCreate):
        return self.structure_repository.create_particulier(structure=structure)