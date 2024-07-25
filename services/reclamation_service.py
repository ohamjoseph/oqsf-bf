from http.client import HTTPException

from fastapi import Depends

from controllers.structure_controller import StructureController
from schemas.particulier_schema import Particulier
from schemas.saisine_schema import SaisineCreate

from services.particulier_service import ParticulierService
from controllers.particulier_controller import ParticulierController
from services.saisine_service import SaisineService
from schemas.reclamation_schema import ReclamationCreate


class ReclamationService:
    def __init__(self,
                 particulier_service: ParticulierService = Depends(),
                 saisine_service: SaisineService = Depends(),
                 structure_controller: StructureController = Depends(),
                 ):
        self.particulier_controller = particulier_service
        self.saisine_service = saisine_service
        self.structure_controller = structure_controller

    def create_reclamation(self,
                           reclamation: ReclamationCreate
                           ) -> dict[str, SaisineCreate | Particulier]:

        saisine = reclamation.saisine
        structure_info = None
        particulier = None

        if reclamation.structure_info:
            try:
                structure_info = self.structure_controller.create_structure(
                    structure=reclamation.structure_info)

                saisine_updated = saisine.model_copy(
                    update={"structure_id": structure_info.id}
                )

            except HTTPException as e:

                raise HTTPException()
        elif reclamation.particulier_info:

            try:

                particulier = (
                    self.particulier_controller.
                    create_particulier(
                        particulier=reclamation.particulier_info))

                saisine_updated = saisine.model_copy(
                    update={"particulier_id": particulier.id}
                )

            except Exception as e:
                raise HTTPException(status_code=400, detail=str(e))

        db_saisine = self.saisine_service.create_saisine(saisine_updated)

        return {
                    "particulier_info": particulier,
                    "structure_info":structure_info,
                    "saisine": db_saisine
                }
