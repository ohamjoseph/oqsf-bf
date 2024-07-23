from pydantic import BaseModel
from typing import Optional


class StructureInfoBase(BaseModel):
    denomination: str
    forme_juridique: str
    numero_police: str
    telephone: str
    email: str
    pays_residence: str
    region_residence: str
    province_residence: str
    commune_residence: str
    secteur_activites: str
    nom_prenom_representant: str
    fonction_representant: str
    contact_representant: str


class StructureInfoCreate(StructureInfoBase):
    pass


class StructureInfo(StructureInfoBase):
    id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
