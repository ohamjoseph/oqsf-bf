from typing import List
from fastapi import APIRouter, Depends
from src.controllers.saisine_controller import SaisineController
from src.schemas.saisine_schema import SaisineCreate, Saisine


router = APIRouter()

@router.post("/", response_model=Saisine)
def create_saisine_view(saisine: SaisineCreate, saisine_controller: SaisineController = Depends()):
    return saisine_controller.create_saisine(saisine=saisine)

@router.get("/", response_model=List[Saisine])
def read_saisines_view(skip: int = 0, limit: int = 10, saisine_controller: SaisineController = Depends()):
    return saisine_controller.get_saisine()