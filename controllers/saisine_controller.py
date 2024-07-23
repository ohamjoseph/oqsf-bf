from fastapi import Depends
from models import saisine_model
from schemas.saisine_schema import SaisineCreate
from services.saisine_service import SaisineService


class SaisineController:
    def __init__(self, saisineService: SaisineService = Depends()) -> None:
        self.saisineService = saisineService
    

    def create_saisine(self, saisine: SaisineCreate) -> saisine_model.Saisine:
        return self.saisineService.create_saisine(saisine=saisine)
    
    def get_saisine(self) -> saisine_model.Saisine:
        return self.saisineService.get_saisines()