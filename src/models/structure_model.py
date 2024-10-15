from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database import Base


class StructureInfo(Base):
    __tablename__ = 'structure_info'

    denomination = Column(String, nullable=False)
    forme_juridique = Column(String, nullable=False)
    numero_police = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    pays_residence = Column(String, nullable=False)
    region_residence = Column(String, nullable=False)
    province_residence = Column(String, nullable=False)
    commune_residence = Column(String, nullable=False)
    secteur_activites = Column(String, nullable=False)
    nom_prenom_representant = Column(String, nullable=False)
    fonction_representant = Column(String, nullable=False)
    contact_representant = Column(String, nullable=False)

    saisine = relationship("Saisine", back_populates="structure")
