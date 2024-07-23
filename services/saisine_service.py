

from fastapi import Depends
from models.saisine_model import Saisine
from repositories.saisine_repository import SaisineRepository
from schemas.saisine_schema import SaisineCreate


class SaisineService:
    def __init__(self, saisine_repository : SaisineRepository = Depends()):
        self.saisine_repository = saisine_repository
    

    def create_saisine(self, saisine: SaisineCreate) -> Saisine:
        return self.saisine_repository.create_saisine(saisine=saisine)
    

    def get_saisines(self, skip: int = 0, limit: int = 10)-> Saisine:
        return self.saisine_repository.get_saisines(skip=0, limit=10)
        