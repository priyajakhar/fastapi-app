from fastapi import FastAPI
from pathlib import Path
from from_root import from_root, from_here
import os

# CAMERA_EXE = os.path.abspath("~/Desktop/MyProjects/camerasdk/build/RemoteCli")
# CAMERA_EXE = Path('RemoteCli').resolve()

app = FastAPI()

CAMERA_EXE = from_root("RemoteCli")

@app.get("/")
async def root():
    return "Welcome to my app"


@app.get("/image")
async def take_image():
    print(CAMERA_EXE)
    os.system(CAMERA_EXE)
