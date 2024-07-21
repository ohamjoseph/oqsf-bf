import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from database import get_db

router = APIRouter()

@router.post("/")
async def create_reclamation(reclamation: schemas.Reclamation, db: Session = Depends(get_db)):
    
    try:
        print(reclamation.personal_info.dict())
        # Créer les instances SQLAlchemy pour PersonalInfo et Saisine
        personal = models.PersonalInfo(**reclamation.personal_info.dict())
        #db_personal_info = PersonalInfo(**reclamation.personal_info.dict())
    
        db.add(personal)
        db.commit()
        db.refresh(personal)
        
        
        saisine_data = {
            "institution": reclamation.saisine.institution,
            "agence": reclamation.saisine.agence,
            "motif_reclamation": reclamation.saisine.motif_reclamation,
            "reponse_insatisfaisante": reclamation.saisine.reponse_insatisfaisante,
            "resume_probleme": reclamation.saisine.resume_probleme,
            "personal_info_id": personal.id
        }
       
        db_saisine = models.Saisine(**saisine_data)
        db.add(db_saisine)
        db.commit()
        db.refresh(db_saisine)
        
        return {"personal_info": personal,"saisine": db_saisine}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))