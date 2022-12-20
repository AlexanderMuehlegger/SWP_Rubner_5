import random


def main():
    pass


def getZuffalszahlen(_list, anz=10, min=0, max=10):
    for i in range(anz):
        _list.append(random.randint(min, max))

def sortList(input):
    for i in range(len(input)-1):
        for j in range(len(input)-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]

def getAvg(input):
    sum = 0
    for i in range(len(input)):
        sum += input[i]
    return sum / len(input)

def getMedian(input):
    length = len(input)
    if length%2 == 0:
        return getAvg([input[int(length/2+1)],input[int(length/2)]])
    return input[int(length/2)]

if __name__ == "__main__":
    zahlen = []
    getZuffalszahlen(zahlen, 10, 0, 100)
    print(zahlen)
    sortList(zahlen)
    print(zahlen)
    median = getMedian(zahlen)
    avg = getAvg(zahlen)
    print("Median: ", median)
    print("Durchschnitt: ", avg)
    main()
