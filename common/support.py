from pathlib import Path
from from_root import from_root, from_here
from datetime import date
import time
import threading
import asyncio
import os


STATE = "NC"
CAM_EXT = "Y"
CAM_DIR = from_root("common")
IMAGES_DIR = CAM_DIR / f"{STATE}_{date.today()}"
CAMERA_EXE = from_root("common/RemoteCli")


def create_new_dir():
    # os.chdir(CAM_DIR)
    # if IMAGES_DIR not in os.listdir():
    #         os.mkdir(IMAGES_DIR)
    Path(IMAGES_DIR).mkdir(parents=True, exist_ok=True)


async def capture_image():
    print(CAMERA_EXE)
    # os.system(CAMERA_EXE)
    time.sleep(5)
    ts = str(int(time.time()))
    # threading.Thread(target=rename_image(ts)).start()
    # threading.Thread(target=self.file_rename(t, img_no)).start()

    # asyncio.run(trigger_cam())
    await rename_image(ts)
    # await asyncio.sleep(5)


async def rename_image(timestamp):
    # time.sleep(4)
    await asyncio.sleep(4)
    print("renaming images..")
    for file_name in os.listdir(IMAGES_DIR):
        print(file_name)
        if file_name.startswith(STATE + CAM_EXT):
            if file_name.endswith('.JPG'):
                new_name = f"{STATE}_{timestamp}.JPG"
            elif file_name.endswith('.ARW'):
                new_name = f"{STATE}_{timestamp}.ARW"
            print(file_name, new_name)
            # os.rename(file_name, new_name)

# create_new_dir()
# capture_image()
# rename_image()