from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.saisine_model import Saisine

class ParticulierInfo(Base):
    __tablename__ = "particulier_info"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom_prenom = Column(String, index=True)
    numero_membre = Column(String, unique=True, index=True)
    annee_naissance = Column(Integer)
    sexe = Column(String)
    niveau_instruction = Column(String)
    telephone = Column(String)
    email = Column(String)
    pays_residence = Column(String)
    region_residence = Column(String)
    province_residence = Column(String)
    commune_residence = Column(String)
    profession = Column(String)

    saisine = relationship("Saisine", back_populates="particulier")

