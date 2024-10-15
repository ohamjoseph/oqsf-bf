from fastapi import APIRouter
from src.controllers.particulier_controller import *
from src.schemas.particulier_schema import Particulier

router = APIRouter()

@router.post('/', response_model=Particulier)
def create_particulier(
        particulier: ParticulierCreate,
        particulier_controller: ParticulierController = Depends()):

    return particulier_controller.create_particulier(particulier=particulier)

@router.get('/',)
def get_particuliers(
        particulier_controller: ParticulierController = Depends()):
    return particulier_controller.get_particuliers()

@router.get('/{particulier_id}', response_model=Particulier)
def get_particulier_by(particulier_id: int,
                       particulier_controller: ParticulierController = Depends()):
    """
    Route la recupérer un particulier.
    :param particulier_id:
    :param particulier_controller:
    :return:
    """
    return particulier_controller.get_particulier_by_id(particulier_id)

@router.delete('/{particulier_id}', response_model=Particulier)
def delete_particulier(
        particulier_id: int,
        particulier_controller: ParticulierController = Depends()):
    """
    Route pour supprimer un particulier.
    :param particulier_id:
    :param particulier_controller:
    :return:
    """
    return particulier_controller.delete_particulier(particulier_id=particulier_id)

