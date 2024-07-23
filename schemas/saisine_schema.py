from pydantic import BaseModel
from typing import Optional


class SaisineBase(BaseModel):
    institution: str
    agence: str
    motif_reclamation: str
    reponse_insatisfaisante: str
    resume_probleme: str
    copie_reclamation: Optional[str] = None
    autres_documents: Optional[str] = None


class SaisineCreate(SaisineBase):
    particulier_id: Optional[int] = None
    structure_id: Optional[int] = None


class Saisine(SaisineBase):
    id: int
    particulier_id: Optional[int] = None
    structure_id: Optional[int] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
