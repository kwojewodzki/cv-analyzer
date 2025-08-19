from typing import Any, Coroutine, Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from cv.models import SkillModel
from .models import SkillModel
from .schemas import SkillBase

async def create_skill(db: AsyncSession, skill: SkillBase) -> SkillModel:
    print(skill.model_dump())
    db_skill = SkillModel(name=skill.name)
    db.add(db_skill)
    await db.commit()
    await db.refresh(db_skill)
    return db_skill

async def list_skills(db: AsyncSession) -> Sequence[SkillModel]:
    result = await db.execute(select(SkillModel))
    skills = result.scalars().all()
    return skills