# Made by Nicolas Mendes Nov 12, 2021
import pathlib
import shutil
import os
import sys
from pathlib import Path
from os import remove
from sys import argv

# Shell POSIX path
current_shell_dir = os.path.dirname(sys.argv[0])
fixDirShellPath = current_shell_dir.replace(" ", "\\ ").replace("?", "\\?").replace("&", "\\&").replace(
    "(", "\\(").replace(")", "\\)").replace("*", "\\*").replace("<", "\\<").replace(">", "\\>")
targetShellDirectory = "aarch64"

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

def backupProcess():
    print("Backing up your files...")
    os.mkdir(f"{THIS_PATH}/BACKUP")
    copy_and_overwrite(relative_to_assets("CrossCode.app"),
                       relative_to_target("BACKUP"))
    print("Backup complete!")


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


def find_and_check_compressed():
    # If NWJS.xz exists inside aarch64 folder.
    print("Checking if NWJS is still compressed...")
    if relative_to_assets("NWJS.7z").exists():
        print("NWJS is still compressed... Extracting")
        # Check if /opt/homebrew/bin/brew exists in the system.
        xz_exists = os.path.exists("/opt/homebrew/bin/brew")
        if xz_exists != True:
            print("Homebrew is not installed... Installing brew.")
            os.system(
                '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        else:
            print("Homebrew is installed... Skipping")
        print(f"Found {relative_to_assets('NWJS.7z')}")
        os.system('brew install p7zip')
        os.system(
            f'7za x {str(fixDirShellPath)}/{str(targetShellDirectory)}/NWJS.7z -oaarch64/ ')
        return True

def cleaningProcess():
    print("Cleaning process started!")
    os.system(f'rm -rf {str(fixDirShellPath)}/{str(targetShellDirectory)}')
    remove(argv[0])



print("""
._____          _______          _______ _   _            _____  __  __   __ _  _   
|  __ \   /\   |  __ \ \        / /_   _| \ | |     /\   |  __ \|  \/  | / /| || |  
| |  | | /  \  | |__) \ \  /\  / /  | | |  \| |    /  \  | |__) | \  / |/ /_| || |_ 
| |  | |/ /\ \ |  _  / \ \/  \/ /   | | | . ` |   / /\ \ |  _  /| |\/| | '_ \__   _|
| |__| / ____ \| | \ \  \  /\  /   _| |_| |\  |  / ____ \| | \ \| |  | | (_) | | |  
|_____/_/    \_\_|  \_\  \/  \/   |_____|_| \_| /_/    \_\_|  \_\_|  |_|\___/  |_|  

Welcome to the Mac M1 Aarch64 Patcher

1 - Before you begin, make sure you have at least the version 1.0.0 or above of CrossCode installed.
2 - Drop this script with the folder aarch64 in the same folder as CrossCode.app.
3 - Let's patch it!

If you want to update the NW.js to the latest version, read the readme.md instructions.
""")
userConfirm = input(
    "Do you want to install the Aarch64/ARM64 patch to CrossCode? (Y/n) ").lower()

if userConfirm == "y":
    userBackupRequest = input("[RECOMMENDED] Do you want to backup the game? (Y/n) ").lower()
    if userBackupRequest == "y":
        backupProcess()
    else:
        print("Be advised: this patcher was tested with CrossCode version 1.2 and 1.4.2.\nThis patch can break your game if it is in a different version.")
    print("Checking NWJS files...")
    find_and_check_compressed()
    print("Installing...")
    print("Copying files...")
    patchNWjs()
    patchFrameworks()
    promptCleaning = input("Do you want to erase files? (Y/n) ").lower()
    if promptCleaning == "y":
        cleaningProcess()
    else:
        print("Ok, leaving files there.")
    print("Done!")
else:
    print("Aborting...")
    exit(0)
