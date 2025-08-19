import asyncio
from .cv import router as cv_router

from fastapi import FastAPI

app = FastAPI()

app.include_router(cv_router.router)

@app.get("/delay")
async def delay():
    await asyncio.sleep(10)
    return {"message": "Hello World"}

@app.get("/")
async def root():
    return {"message": "Hello Async World"}

