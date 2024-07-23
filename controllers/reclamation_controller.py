from fastapi import Depends

from schemas.reclamation_schema import Reclamation, ReclamationCreate
from services.reclamation_service import ReclamationService


class ReclamationController:
    def __init__(self, reclamation_service: ReclamationService = Depends()):
        self.reclamation_service = reclamation_service

    def create_reclamation(self, reclamation: ReclamationCreate):
        return self.reclamation_service.create_reclamation(reclamation)
