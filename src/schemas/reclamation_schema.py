from pydantic import BaseModel
from typing import Optional

from src.schemas import saisine_schema
from src.schemas import particulier_schema, structure_schema


class ReclamationBase(BaseModel):
    saisine: saisine_schema.SaisineCreate


class ReclamationCreate(ReclamationBase):
    particulier_info: Optional[particulier_schema.ParticulierCreate] = None
    structure_info: Optional[structure_schema.StructureInfoCreate] = None


class Reclamation(BaseModel):
    particulier_info: Optional[particulier_schema.Particulier] = None
    structure_info: Optional[structure_schema.StructureInfo] = None
