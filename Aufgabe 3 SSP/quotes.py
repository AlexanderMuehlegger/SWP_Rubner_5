import json
import random

with open('quotes.json') as json_file:
    data = json.load(json_file)

def randomQuote():
    return random.choice(list(data.values()))