from enum import Enum
import random as rand

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

def get_combination(_drawing):
    #Straße
    if(any(x.symbol == 5 or x.symbol == 10 for x in _drawing)):
        _drawing.sort(key=lambda card: card.symbol)
        
        drawing_symbols = [card.symbol for card in _drawing]
        print(drawing_symbols)
        
        if(drawing_symbols.count(drawing_symbols[0]) == 1 \
            and drawing_symbols.count(drawing_symbols[1]) == 1 \
            and drawing_symbols.count(drawing_symbols[2]) == 1 \
            and drawing_symbols.count(drawing_symbols[3]) == 1):

            if(max(drawing_symbols)-min(drawing_symbols) < 5):
                return True
            else:
                return False

        

def init_cards():
    global cards
    for type in CardType:
        for i in range(CARD_SYMBOL_START, CARD_SYMBOLS+CARD_SYMBOL_START):
            cards.append(Card(i, type))

def drawing(count):
    rand.shuffle(cards)
    rand_cards = []
    min = 0
    max = len(cards)-1
    for i in range(count):
        rand_index = rand.randrange(min, max)
        rand_card = cards[rand_index]
        cards[rand_index], cards[max] = cards[max], cards[rand_index]
        max-=1
        rand_cards.append(rand_card)
    return rand_cards

def init():
    init_cards()

def printCards(arr):
    for i in arr:
        print(i.toString())
        print("------------------")

if __name__ == "__main__":
    init()
    # drawing = drawing(5)

    # printCards(drawing)
    # print("\n")

    # get_combination(drawing)
    draw = []
    street = False

    while(not street):
        draw = drawing(5)
        street = get_combination(draw)
        
    printCards(draw)


