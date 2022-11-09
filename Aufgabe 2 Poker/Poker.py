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
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

class Statistic():
    royal_flush = 0
    straight_flush = 0
    flush = 0
    vierling = 0
    strasse = 0
    drilling = 0
    paar = 0
    full_house = 0
    double_paar = 0
    high_hand = 0

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
            return SpecialCard(self.symbol).name
        return SpecialCard(self.symbol)
        

GAMES = 1000000
MAX_CARDS = 52
CARD_SYMBOLS = 13
CARD_SYMBOL_START = 2
statistic = Statistic()

cards = []

def get_combination(_drawing):
    global statistic
    _drawing.sort(key=lambda card: card.symbol)

    drawing_symbols = [card.symbol for card in _drawing]

    #Straße
    if(any(x.symbol == 5 or x.symbol == 10 for x in _drawing)):
         
        if(drawing_symbols.count(drawing_symbols[0]) == 1 \
            and drawing_symbols.count(drawing_symbols[1]) == 1 \
            and drawing_symbols.count(drawing_symbols[2]) == 1 \
            and drawing_symbols.count(drawing_symbols[3]) == 1):

            if(max(drawing_symbols)-min(drawing_symbols) < 5):
                #straight flush
                if all(map(lambda card: card.type == _drawing[0].type, _drawing[1:])):
                    #royal flush
                    if _drawing[-1].symbol == SpecialCard.Ace.value:
                        statistic.royal_flush += 1; return

                    statistic.straight_flush += 1
                    return
                statistic.strasse += 1; return
    #flush
    if all(map(lambda card: card.type == _drawing[0].type, _drawing[1:])):
        statistic.flush += 1; return
    

    most_frequent = max(drawing_symbols, key=drawing_symbols.count)
    highest_occurence = drawing_symbols.count(most_frequent)
    
    if highest_occurence >= 2:
        if highest_occurence >= 3:
            if highest_occurence == 4:
                statistic.vierling += 1; return
            #Full house
            filtered_draw = list(filter(lambda symbol: symbol != most_frequent, drawing_symbols))
            if filtered_draw.count(max(filtered_draw, key=filtered_draw.count)) == 2:
                statistic.full_house += 1; return
            statistic.drilling += 1; return
        

        filtered_draw = list(filter(lambda symbol: symbol != most_frequent, drawing_symbols))
        if filtered_draw.count(max(filtered_draw, key=filtered_draw.count)) == 2:
            statistic.double_paar += 1; return
        statistic.paar += 1; return
    statistic.high_hand += 1


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

    card = [
        Card(5, CardType.Hearts),
        Card(6, CardType.Hearts),
        Card(7, CardType.Hearts),
        Card(8, CardType.Hearts),
        Card(9, CardType.Hearts),
    ]

    prop = Statistic()
    prop.high_hand = 50.117
    prop.paar = 42.256
    prop.double_paar = 4.753
    prop.drilling = 2.112
    prop.strasse = 0.392
    prop.flush = 0.196
    prop.full_house = 0.144
    prop.vierling = 0.024
    prop.straight_flush = 0.0013
    prop.royal_flush = 0.000154

    # get_combination(card)

    for i in range(GAMES):
        get_combination(drawing(5))

    stat = vars(statistic)
    statistic_list = sorted(stat, key=stat.get, reverse=True)
    print(stat)
    for x in statistic_list:
        print("{0}: {1} -> {2:.3f}% (calculated) | {3}% (googled)".format(x,stat[x], (stat[x]/GAMES*100), vars(prop)[x]))
    
