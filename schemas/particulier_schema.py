from datetime import datetime

from pydantic import BaseModel
from typing import List, Optional
from schemas.saisine_schema import Saisine, SaisineCreate


class ParticulierBase(BaseModel):
    nom_prenom: str
    numero_membre: str
    annee_naissance: int
    sexe: str
    niveau_instruction: str
    telephone: str
    email: str
    pays_residence: str
    region_residence: str
    province_residence: str
    commune_residence: str
    profession: Optional[str] = None


class ParticulierCreate(ParticulierBase):
    pass


class Particulier(ParticulierBase):
    id: int
    createDate: datetime
    updateDate: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
