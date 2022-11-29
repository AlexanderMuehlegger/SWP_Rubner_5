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
    Spock = 4
    Echse = 5

    def __str__():
        data = []
        for e in SSP:
            data.append([e.name, e.value])
        print(tabulate(data, headers=("Name", "Value"), numalign="center"))

class Error(Enum):
    NoNum = 100

class StatisticRes: #Result
    def __init__(self):
        self.draw = 1
        self.player = 1
        self.comp = 1

class StatisticSymb:
    def __init__(self):
        self.player_stat = {}
        self.comp_stat = {}
    
    def getFullStat(self):
        stat = {}
        
        for x in self.comp_stat:
            stat[x] = self.comp_stat[x]
        
        for x in self.player_stat:
            stat[x] = self.player_stat.get(x, 0) +  self.player_stat[x]

        return stat

class SSP_Game:

    win = {
        SSP.Schere: [SSP.Papier, SSP.Echse],
        SSP.Papier: [SSP.Stein, SSP.Spock],
        SSP.Stein: [SSP.Echse, SSP.Schere],
        SSP.Echse: [SSP.Spock, SSP.Papier],
        SSP.Spock: [SSP.Schere, SSP.Stein]
    }

    min_ssp = 1
    max_ssp = 3

    def __init__(self):
        self.status = Status.Stopped
        SSP.__str__()
        self.init()
    
    def init(self):
        self.statisticRes = StatisticRes()
        self.statisticSymb = StatisticSymb()
        self.commandHandler = CommandHandler()

        exitCommand = Command(-1, exit, "Exit Programm", "exit")
        self.commandHandler.addCommand(exitCommand)

        printCommand = Command(-1, self.printHelp, "Print Help", "-h")
        self.commandHandler.addCommand(printCommand)

        statisticCommand = Command(-1, self.printStatistic, "Stop Game and print Statistic", "-s")
        self.commandHandler.addCommand(statisticCommand)

        resetCommand = Command(-1, self.reset, "Resets current Statistic", "-r")
        self.commandHandler.addCommand(resetCommand)
    

    def start(self):
        self.printInfo()
        print("Press Enter if ready to start!")
        self.processInput()
        self.status = Status.Running
        self.play()
    
    def reset(self):
        self.status = Status.Paused
        self.statisticRes = StatisticRes()
        self.init_SymbStat()
        print("Reset Complete!")
        self.status = Status.Running

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
        stat_res = vars(self.statisticRes)
        draws = sorted(stat_res, key=stat_res.get, reverse=True)
        summ = 0

        for x in stat_res:
            summ += stat_res[x]

        if summ == 0:
            return

        data_res = []
        
        for x in draws:
            data_res.append([x, stat_res[x], round(stat_res[x]/summ*100, 2)])
        
        data_symb = []
        stat_symb = self.statisticSymb.getFullStat()

        for x in stat_symb:
            data_symb.append([x.name, stat_symb[x], round(stat_symb[x]/summ*100, 2)]) #

        print()
        print(tabulate(data_res, headers=['Outcome', 'Count', 'Procentage (%)']))
        print()

        print()
        print(tabulate(data_symb, headers=['Symbol', 'Count', 'Percentage (%)']))
        print()


    def play(self):
        max = self.max_ssp
        min = self.min_ssp
        paused_msg = False
        while(self.status is not Status.Stopped):
            if self.status is Status.Paused:
                if  paused_msg == False:
                    print("Game Paused! - Please Wait!")
                    paused_msg = True
                continue
            
            paused_msg = False

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
                self.statisticRes.draw += 1
                print("Draw!")
                continue

            draw = SSP(draw)
            guess = SSP(guess)

            self.statisticSymb.player_stat[draw] = self.statisticSymb.player_stat.get(draw, 0) + 1
            self.statisticSymb.comp_stat[guess] = self.statisticSymb.comp_stat.get(guess, 0) + 1


            print(SSP.win)
            if guess in self.win[draw]:
                self.statisticRes.player += 1
                continue
            
            if draw in self.win[guess]:
                self.statisticRes.comp += 1
                continue

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
        if len(command) == 0:
            return
        try:
            id = [x for x in self.commands if x.command.__contains__(command)][0].id
        except IndexError:
            return -1
        
        if isinstance(id, list):
            print("Specify Command!")
            return

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