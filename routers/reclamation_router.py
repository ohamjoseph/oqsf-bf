from fastapi import APIRouter, Depends

from controllers.reclamation_controller import ReclamationController
from schemas.reclamation_schema import Reclamation, ReclamationCreate

router = APIRouter()

@router.post("/")
def create_reclamation(
        reclamation: ReclamationCreate,
        reclamation_controller: ReclamationController = Depends()):

    return reclamation_controller.create_reclamation(reclamation)