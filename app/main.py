import asyncio
import time

from fastapi import FastAPI

app = FastAPI()

@app.get("/delay")
async def delay():
    await asyncio.sleep(10)
    return {"message": "Hello World"}

@app.get("/")
async def root():
    #await asyncio.sleep(10)
    return {"message": "Hello Async World"}

