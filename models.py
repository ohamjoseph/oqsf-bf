from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class PersonalInfo(Base):
    __tablename__ = "personal_info"

    id = Column(Integer, primary_key=True, index=True)
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
    

class Saisine(Base):
    __tablename__ = "saisine"

    id = Column(Integer, primary_key=True, index=True)
    personal_info_id = Column(Integer, ForeignKey('personal_info.id'))
    institution = Column(String)
    agence = Column(String)
    motif_reclamation = Column(String)
    reponse_insatisfaisante = Column(String)
    resume_probleme = Column(String)

    personal_info = relationship("PersonalInfo", back_populates="saisines")

PersonalInfo.saisines = relationship("Saisine", back_populates="personal_info")
