from fastapi import FastAPI
from pathlib import Path
from from_root import from_root, from_here
import common.support as sup
from common.wheels import Motors
import asyncio
import os

# CAMERA_EXE = os.path.abspath("~/Desktop/MyProjects/camerasdk/build/RemoteCli")
# CAMERA_EXE = Path('RemoteCli').resolve()

app = FastAPI()

amiga_motors = Motors()
CAMERA_EXE = from_root("common/RemoteCli")

@app.get("/")
async def root():
    sup.create_new_dir()
    return "Welcome to my app"


@app.get("/image")
async def take_image():
    asyncio.run(sup.capture_image())
    # sup.capture_image()
    # print("\n", CAMERA_EXE, "\n")
    # os.system(CAMERA_EXE)
    
@app.get("/forward")
async def move_forward():
    await amiga_motors.forward()
    # await motor.forward()

@app.get("/reverse")
async def move_reverse():
    await amiga_motors.reverse()