from fastapi import Depends
from repositories.particulier_repository import *
from schemas.particulier_schema import Particulier

class ParticulierService:
    def __init__(self,particulier_repository: ParticulierRepository = Depends()) -> None:
        self.particulier_repository = particulier_repository
    
    def create_particulier(self, particulier:ParticulierCreate) ->Particulier:
        return self.particulier_repository.create_particulier(particulier=particulier)
    
