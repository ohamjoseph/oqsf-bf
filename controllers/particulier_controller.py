from fastapi import Depends
from services.particulier_service import *

class ParticulierController:
    def __init__(self, particulier_service: ParticulierService = Depends()) -> None:
        self.particulier_service = particulier_service
    
    def create_particulier(self, particulier: ParticulierCreate) -> Particulier:
        return self.particulier_service.create_particulier(
            particulier=particulier)
