# Made by Nicolas Mendes Nov 12, 2021
import pathlib
from pathlib import Path
import shutil
import os
import sys

# Dynamic File Path Solution
THIS_PATH = pathlib.Path(__file__).parent.absolute()
ASSETS_PATH = THIS_PATH / Path("aarch64")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def relative_to_target(path: str) -> Path:
    return THIS_PATH / Path(path)


def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)


def patchNWjs():
    # Copy files from ./aarch64/MacOS to CrossCode.app/Contents
    print(
        f"Copying files from {relative_to_assets('MacOS/nwjs')} to {relative_to_target('CrossCode.app/Contents/MacOS/nwjs')}")

    shutil.copy(relative_to_assets("MacOS/nwjs"),
                relative_to_target("CrossCode.app/Contents/MacOS/nwjs"))


def patchFrameworks():
    # Copy files from ./aarch64/Frameworks to CrossCode.app/Contents/Frameworks
    print(
        f"Copying files from {relative_to_assets('Frameworks')} to {relative_to_target('CrossCode.app/Contents/Frameworks')}")
    copy_and_overwrite(relative_to_assets("Frameworks"),
                       relative_to_target("CrossCode.app/Contents/Frameworks"))


print("""
._____          _______          _______ _   _            _____  __  __   __ _  _   
|  __ \   /\   |  __ \ \        / /_   _| \ | |     /\   |  __ \|  \/  | / /| || |  
| |  | | /  \  | |__) \ \  /\  / /  | | |  \| |    /  \  | |__) | \  / |/ /_| || |_ 
| |  | |/ /\ \ |  _  / \ \/  \/ /   | | | . ` |   / /\ \ |  _  /| |\/| | '_ \__   _|
| |__| / ____ \| | \ \  \  /\  /   _| |_| |\  |  / ____ \| | \ \| |  | | (_) | | |  
|_____/_/    \_\_|  \_\  \/  \/   |_____|_| \_| /_/    \_\_|  \_\_|  |_|\___/  |_|  

Welcome to the Mac M1 Aarch64 Patcher

1 - Before you begin, make sure you have at least the version 1.0.0 and above of CrossCode installed.
2 - Drop this script with the folder aarch64 in the same folder as CrossCode.app.
3 - Don't forget to extract the NWJS.xz files inside aarch64 (i.e MacOS, Frameworks...)

If you want to update the NW.js to the latest version, read the readme.md instructions.
""")
userConfirm = input(
    "Do you want to install the Aarch64/ARM64 patch to CrossCode? (Y/n) ").lower()

if userConfirm == "y":
    print("Installing...")
    print("Copying files...")
    patchNWjs()
    patchFrameworks()
    print("Done!")
else:
    print("Aborting...")
    exit(0)
