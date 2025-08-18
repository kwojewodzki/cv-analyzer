from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class CV(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, index=True)
    owner = relationship("User", back_populates="cvs")