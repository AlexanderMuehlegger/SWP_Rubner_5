from enum import Enum
from tabulate import tabulate

class Status(Enum):
    Running = 1
    Paused = 2
    Stopped = 3

class SSP(Enum):
    Schere = 1
    Stein = 2
    Papier = 3
    Spock = 4
    Echse = 5

    def __str__():
        data = []
        for e in SSP:
            data.append([e.name, e.value])
        print()
        print(tabulate(data, headers=("Symbol", "Value"), numalign="center"))
        print()

class Error(Enum):
    NoNum = 100
