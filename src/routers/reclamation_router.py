from fastapi import APIRouter, Depends

from src.controllers.reclamation_controller import ReclamationController
from src.schemas.reclamation_schema import ReclamationCreate

router = APIRouter()

@router.post("/")
def create_reclamation(
        reclamation: ReclamationCreate,
        reclamation_controller: ReclamationController = Depends()):

    return reclamation_controller.create_reclamation(reclamation)