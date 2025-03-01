
import os
import schedule
import time
from datetime import datetime
from dataclasses import dataclass
import json
import shutil
import matplotlib.pyplot as plt
import numpy as np

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

@dataclass
class Point:
    y: int = 0
    x: int = 0

    def __init__(self, x: str, y: float):
        self.x = x
        self.y = y


def make_dir(path):
    dirs = os.path.dirname(path)
    os.makedirs(dirs, exist_ok=True)

def read_data():
    x = []
    y = []

    walk = os.walk(_DOWNLOAD)
    for (root, dirs, files) in walk:
        for file_name in files:
            if '_points.json' in file_name:
                try:
                    print(file_name)
                    path = f"{_DOWNLOAD}{file_name}"
                    with open(path, 'r', encoding="utf-8") as f:
                        data = json.load(f)
                        point = Point(data["x"], data["y"])
                        x.append(point.x)
                        y.append(point.y)

                    move_file_to_loadded(file_name)
                except Exception as e:
                    move_file_to_error(file_name)
                    print(f"Exception {e}")
            else:
                move_file_to_error(file_name)

    work_with_point(x, y)

def work_with_point(x, y):
    x1 = np.array(x)
    y1 = np.array(y)
    plt.scatter(x1, y1, color='blue', label='Group 1')
    plt.show()


def work_with_InventoryItem(obj: InventoryItem):
    print(f"Имя = {obj.name}")
    print(f"Цена = {obj.unit_price}")
    print(f"Количество = {obj.quantity_on_hand}")


def move_file_to_error(file_name):
    shutil.copy2(f"{_DOWNLOAD}{file_name}", f"{_ERROR}{file_name}")
    os.remove(f"{_DOWNLOAD}{file_name}")

def move_file_to_loadded(file_name):
    shutil.copy2(f"{_DOWNLOAD}{file_name}", f"{_LOADDED}{file_name}")
    os.remove(f"{_DOWNLOAD}{file_name}")

def main():
    print("START")
    make_dir(_DOWNLOAD)
    make_dir(_LOADDED)
    make_dir(_ERROR)

    while True:
        read_data()
        time.sleep(10)
        

if __name__ == "__main__":
    main()