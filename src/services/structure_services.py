from fastapi import Depends

from src.repositories.structure_repository import StructureRepository
from src.schemas.structure_schema import StructureInfoCreate


class StructureService:
    def __init__(self, structure_repository: StructureRepository = Depends()):
        self.structure_repository = structure_repository

    def create_structure(self, structure: StructureInfoCreate):
        return self.structure_repository.create_structure(structure=structure)

    def get_structure_by_id(self, structure_id):
        return self.structure_repository.get_structure_by_id(structure_id=structure_id)

    def update_structure(self, structure_id: int, structure: StructureInfoCreate):
        return self.structure_repository.update_structure(
            structure_id=structure_id,
            structure=structure
        )

    def delete_structure(self, structure_id: int):
        return self.structure_repository.delete_structure(
            structure_id=structure_id)

    def get_structures(self):
        return self.structure_repository.get_structures()
