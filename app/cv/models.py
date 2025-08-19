from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.db.base import Base

class CvModel(Base):
    __tablename__ = "cv"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    original_name = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.now)
    file_path = Column(String, nullable=False)
    text_content = Column(String, nullable=False)

class SkillModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)