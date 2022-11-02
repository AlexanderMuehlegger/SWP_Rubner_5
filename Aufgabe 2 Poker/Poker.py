from enum import Enum
from tokenize import Special

class CardType(Enum):
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    Spades = 4

class CardColor(Enum):
    Red = 1
    Black = 2

class SpecialCard(Enum):
    Jack = 1
    Queen = 2
    King = 3
    Ace = 4

class Card:
    def __init__(self, symbol_id, type):
        self.symbol = symbol_id
        self.type = type
        self.color = self.getColor()

    def getColor(self):
        if(self.type is CardType.Hearts or self.type is CardType.Diamonds):
            return CardColor.Red
        elif(self.type is CardType.Spades or self.type is CardType.Clubs):
            return CardColor.Black
        else:
            return -1

    def toString(self):
        return f'Type: {self.type.name}\nColor: {self.color.name}\nSymbol: {self.getComplexSymbol(True)}'

    def getComplexSymbol(self, name):
        if(self.symbol < CARD_SYMBOLS+CARD_SYMBOL_START-len(SpecialCard)):
            return self.symbol
        if(name):
            return SpecialCard(self.symbol-10).name
        return SpecialCard(self.symbol-10)
        

GAMES = 100000
MAX_CARDS = 52
CARD_SYMBOLS = 13
CARD_SYMBOL_START = 2

cards = []

def get_combination(cards):
    pass

def init_cards():
    global cards
    for type in CardType:
        for i in range(CARD_SYMBOL_START, CARD_SYMBOLS+CARD_SYMBOL_START):
            cards.append(Card(i, type))

def init():
    init_cards()

if __name__ == "__main__":
    init()
    for i in cards:
        print(i.toString())
        print("------------------")

