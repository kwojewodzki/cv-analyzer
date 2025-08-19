from pydantic import BaseModel, Field
from typing import List, Optional

class CvBase(BaseModel):
    original_name: str = Field(..., title="Nazwa pliku")
    file_path: str = Field(..., title="Ścieżka pliku")


class SkillBase(BaseModel):
    name: str
