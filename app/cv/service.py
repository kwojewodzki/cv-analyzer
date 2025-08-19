from sqlalchemy.ext.asyncio import AsyncSession
from models import SkillModel
from schemas import SkillBase

async def create_skill(db: AsyncSession, skill: SkillBase) -> SkillModel:
    db_skill = SkillModel(skill.model_dump())
    db.add(db_skill)
    await db.commit()
    await db.refresh(db_skill)
    return db_skill