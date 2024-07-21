from pydantic import BaseModel
from typing import List, Optional

class PersonalInfoBase(BaseModel):
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
    profession: str

class PersonalInfoCreate(PersonalInfoBase):
    pass

class PersonalInfo(PersonalInfoBase):
    id: int
    saisines: List["Saisine"] = []

    class Config:
        orm_mode = True

class SaisineBase(BaseModel):
    institution: str
    agence: str
    motif_reclamation: str
    reponse_insatisfaisante: str
    resume_probleme: str

class SaisineCreate(SaisineBase):
    pass

class Saisine(SaisineBase):
    id: int
    personal_info_id: int
    personal_info: PersonalInfo

    class Config:
        orm_mode = True
