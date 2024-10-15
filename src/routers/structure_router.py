from fastapi import APIRouter, Depends

from src.controllers.structure_controller import StructureController
from src.schemas.structure_schema import StructureInfoCreate

router = APIRouter()

@router.post("/")
def create_structure(structure: StructureInfoCreate, structure_controller: StructureController = Depends()):
    return structure_controller.create_structure(structure=structure)

@router.get("/{structure_id}")
def get_structure(structure_id: int,
                  structure_controller: StructureController = Depends()):
    return structure_controller.get_structure_by_id(structure_id=structure_id)

@router.get("/")
def get_structures(structure_controller: StructureController = Depends()):
    return structure_controller.get_structures()
