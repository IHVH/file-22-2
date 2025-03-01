
import os
import schedule
import time
from datetime import datetime
from dataclasses import dataclass
import json
import shutil


_DOWNLOAD = "Download\\"
_LOADDED = "Loaded\\"
_ERROR = "Error\\"


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand


def make_dir(path):
    dirs = os.path.dirname(path)
    os.makedirs(dirs, exist_ok=True)

def read_data():
    walk = os.walk(_DOWNLOAD)
    for (root, dirs, files) in walk:
        for file_name in files:
            if '.json' in file_name:
                print(file_name)
            else:
                move_file_to_error(file_name)


def move_file_to_error(file_name):
    shutil.copy2(f"{_DOWNLOAD}{file_name}", f"{_ERROR}{file_name}")
    os.remove(f"{_DOWNLOAD}{file_name}")


def main():
    print("START")
    make_dir(_DOWNLOAD)
    make_dir(_LOADDED)
    make_dir(_ERROR)


    while True:
        read_data()
        time.sleep(1)


if __name__ == "__main__":
    main()