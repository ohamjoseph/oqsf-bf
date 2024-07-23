from fastapi import APIRouter
from controllers.particulier_controller import *

router = APIRouter()

particulier_controller: ParticulierController = Depends()


@router.post('/', response_model=Particulier)
def create_particulier(
        particulier: ParticulierCreate,
        particulier_controller: ParticulierController = Depends()):

    return particulier_controller.create_particulier(particulier=particulier)
