from typing import Optional
from pydantic import BaseModel

class CvBase(BaseModel):
    original_name: str
    uploaded_at: str
    file_path: str
    text_content: str