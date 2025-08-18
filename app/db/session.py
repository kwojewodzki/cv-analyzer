from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost:5432/cvdb")

engine = create_async_engine(DATABASE_URL, echo=True)

# SessionLocal (dla async)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Dependency dla FastAPI
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session