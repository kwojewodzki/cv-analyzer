from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..db.session import get_db
from .service import create_skill, list_skills
from .schemas import SkillBase

router = APIRouter(
    prefix="/skill",
    tags=["skill"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def create_cv(skill: SkillBase, db: AsyncSession = Depends(get_db)):
    return await create_skill(db, skill)

@router.get("/")
async def read_cv(db: AsyncSession = Depends(get_db)):
    return await list_skills(db)