from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Saisine(Base):
    __tablename__ = 'saisine'

    institution = Column(String, nullable=False)
    agence = Column(String, nullable=False)
    motif_reclamation = Column(String, nullable=False)
    reponse_insatisfaisante = Column(String, nullable=False)
    resume_probleme = Column(String, nullable=False)
    copie_reclamation = Column(String, nullable=True)
    autres_documents = Column(String, nullable=True)

    particulier_id = Column(Integer, ForeignKey('particulier_info.id'), nullable=True)
    structure_id = Column(Integer, ForeignKey('structure_info.id'), nullable=True)

    particulier = relationship("ParticulierInfo", back_populates="saisine")
    structure = relationship("StructureInfo", back_populates="saisine")
