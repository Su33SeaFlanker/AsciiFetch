import pathlib
from pathlib import Path
import importlib
from importlib.resources import files
import shutil
import tomllib
import random
import argparse
import os
import subprocess
import sys
import platform
config_dir = (pathlib.Path.home()) / ".config" / "asciifetch"
config_file = config_dir / "config.toml"
config_make = files("asciifetch").joinpath("default_conf.toml")
if(not config_dir.exists()):
    config_dir.mkdir(exist_ok=True, parents=True)
def ensure_conf_exists():
    if(not config_file.exists()):
        shutil.copy(config_make, config_file)
ensure_conf_exists()  
def load_ascii():
    with open(config_file, "rb") as f:
        config = tomllib.load(f)
    return [art.strip() for art in config["ascii_arts"]]
def main():
    ascii_arts = load_ascii()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        action="store_true"
    )
    parser.add_argument(
        "--reset-config",
        action="store_true"
    )
    parser.add_argument(
        "--list-ascii",
        action="store_true"
    )
    parser.add_argument(
        "-s",
        "--specify",
        type=int
    )
    args = parser.parse_args()
    if args.config:
        usersSystem = platform.system()
        if(usersSystem == "Linux"):
            editor = os.environ.get('EDITOR', 'nano')
            subprocess.run([editor, str(config_file)])
            return
        if(usersSystem == "Windows"):
            os.startfile(config_file)
    if args.reset_config:
        print("resetting config")
        shutil.copyfile(config_make, config_file)
        return
    if args.list_ascii:
        for number, art in enumerate(ascii_arts):
            print (f"===================== ASCII ART {number + 1} =====================")
            print (art)
        return
    if args.specify is not None:
        print(ascii_arts[args.specify - 1])
    else:
        print(random.choice(ascii_arts))