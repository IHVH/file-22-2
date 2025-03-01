
import os
import schedule
import time
from datetime import datetime
from dataclasses import dataclass
import json
import random

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
        self.name = name
        self.unit_price = unit_price
        self.quantity_on_hand = quantity_on_hand




_TIME_SECONDS = 5
_I = 0
_DIR_NAME = r"Download\\"

def makedir():
    dirs = os.path.dirname(_DIR_NAME)
    os.makedirs(dirs, exist_ok=True)


def write(i: int, obj: InventoryItem):
    now = datetime.now()
    string_now = now.strftime('%Y-%m-%d_%H-%M-%S')
    file_name = fr"{_DIR_NAME}\{string_now}_{i}.json"
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(obj.__dict__, f)


def work():
    global _I
    _I += 1
    price = random.randint(1000, 99999)
    quant = random.randint(1, 100)
    inv = InventoryItem("NAME", price, quant)
    write(_I, inv)


def main():
    print("START")
    makedir()
    schedule.every(_TIME_SECONDS).seconds.do(work)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()