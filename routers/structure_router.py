from typing import List

from fastapi import APIRouter, Depends

from controllers.structure_controller import StructureController
from models.structure_model import StructureInfo
from schemas.structure_schema import StructureInfoCreate

router = APIRouter()

@router.post("/")
def create_structure(structure: StructureInfoCreate, structure_controller: StructureController = Depends()):
    return structure_controller.create_structure(structure=structure)
