from pydantic import BaseModel
from typing import List, Optional

class PersonalInfoBase(BaseModel):
    id: Optional[int] = None
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

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True



class SaisineBase(BaseModel):
    id: Optional[int] = None
    institution: str
    agence: str
    motif_reclamation: str
    reponse_insatisfaisante: str
    resume_probleme: str
    

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        
class Reclamation(BaseModel):
    personal_info: PersonalInfoBase
    saisine: SaisineBase
