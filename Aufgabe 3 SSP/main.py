from enum import Enum
from tabulate import tabulate
import random

class Status(Enum):
    Running = 1
    Paused = 2
    Stopped = 3

class SSP(Enum):
    Schere = 1
    Stein = 2
    Papier = 3

class Error(Enum):
    NoNum = 100

class Statistic:
    draw = 1
    player = 1
    comp = 1

class SSP_Game:

    min_ssp = 1
    max_ssp = 3

    def __init__(self):
        self.status = Status.Stopped
        self.init()
    
    def init(self):
        self.statistic = Statistic()
        self.commandHandler = CommandHandler()

        exitCommand = Command(-1, exit, "Exit Programm", "exit")
        self.commandHandler.addCommand(exitCommand)

        printCommand = Command(-1, self.printHelp, "Print Help", "-h")
        self.commandHandler.addCommand(printCommand)

        statisticCommand = Command(-1, self.printStatistic, "Stop Game and print Statistic", "-s")
        self.commandHandler.addCommand(statisticCommand)


    def start(self):
        self.printInfo()
        print("Press Enter if ready to start!")
        self.processInput()
        self.status = Status.Running
        self.play()

    def printInfo(self):
        print("".ljust(50, "-"))
        print("Schere, Stein, Papier".center(50, " "))
        print("See all command with -h".center(50, " "))
        print("".ljust(50, "-"))

    def printHelp(self):
        print()
        toprint = []
        for x in self.commandHandler.commands:
            toprint.append(x.getOutputList())
        print(tabulate(toprint, headers=['Command', 'Description']))
        print()
    
    def printStatistic(self):
        stat = vars(self.statistic)
        draws = sorted(stat, key=stat.get, reverse=True)
        sum = 0
        for x in draws:
            sum += stat[x]

        if sum == 0:
            return

        data = []
        
        for x in draws:
            data.append([x, stat[x], stat[x]/sum*100])

        print()
        print(tabulate(data, headers=['Outcome', 'Count', 'Procentage (%)']))
        print()

    def play(self):
        max = self.max_ssp
        min = self.min_ssp
        while(self.status is Status.Running):
            print("Enter digit between {0}-{1}:".format(min, max))
            guess = self.processInput()

            try:
                if guess == '' or Error(guess) is Error.NoNum:
                    continue
            except:
                pass

            if guess < min or guess > max:
                print("OUT OF BOUNDS")
                continue

            draw = random.randrange(min, max+1)

            print("\nPLayer: ", SSP(guess).name)
            print("Computer: ", SSP(draw).name)
            print()

            if draw == guess:
                self.statistic.draw += 1
                print("Draw!")
                continue

            draw = SSP(draw)
            guess = SSP(guess)

            if (draw == SSP.Schere and guess == SSP.Papier):
                self.statistic.comp += 1
                print("Computer won")
                continue

            if (draw == SSP.Papier and guess == SSP.Stein):
                self.statistic.comp += 1
                print("Computer won")
                continue

            if (draw == SSP.Stein and guess == SSP.Schere):
                self.statistic.comp += 1
                print("Computer won")
                continue
            
            print("Player won")
            self.statistic.player += 1

    def processInput(self, msg='> '):
        text = input(msg)
        if self.commandHandler.runCommand(text) == 1:
            return ""
            
        try:
            text = int(text)
        except:
            return Error.NoNum
        return text

class Command:
    def __init__(self, id, method, description, command):
        self.id = id
        self.method = method
        self.description = description
        self.command = command

    def run(self):
        self.method()
    
    def __str__(self):
        print("Description: {0}\nCommand: {1}\n".format(self.description, self.command))
    
    def getOutputList(self):
        return [self.command, self.description]

class CommandHandler:
    def __init__(self):
        self.commands = []
    
    def runCommand(self, command):
        try:
            id = [x for x in self.commands if x.command == command][0].id
        except IndexError:
            return -1
            
        self.commands[id].run()
        return 1
    
    def addCommand(self, command):
        command.id = len(self.commands)
        self.commands.append(command)

def main():
    game = SSP_Game()
    game.start()

if __name__ == "__main__":
    main()