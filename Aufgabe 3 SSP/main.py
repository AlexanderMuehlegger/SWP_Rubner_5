from enum import Enum
from tabulate import tabulate
import random
import quotes

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
    

class TColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Log:
    def w(msg):
        print(f"{TColors.WARNING}{msg}{TColors.ENDC}")

    def e(msg):
        print(f"{TColors.FAIL}{msg}{TColors.ENDC}")
    
    def s(msg):
        print(f"{TColors.OKGREEN}{msg}{TColors.ENDC}")

class SSP_Game:

    win = {
        SSP.Schere: [SSP.Papier, SSP.Echse],
        SSP.Papier: [SSP.Stein, SSP.Spock],
        SSP.Stein: [SSP.Echse, SSP.Schere],
        SSP.Echse: [SSP.Spock, SSP.Papier],
        SSP.Spock: [SSP.Schere, SSP.Stein]
    }

    min_ssp = 1
    max_ssp = 5

    def __init__(self):
        self.status = Status.Stopped
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

        #FIXME: I am broken
        resetCommand = Command(-1, self.reset, "Resets current Statistic", "-r")
        self.commandHandler.addCommand(resetCommand)

        difficultyCommand = Command(-1, self.setDifficulty, "Sets new Difficulty", "-d")
        self.commandHandler.addCommand(difficultyCommand)
        
    

    def start(self):
        self.printInfo()
        self.setDifficulty()
        self.status = Status.Running
        self.play()
    
    def setDifficulty(self):
        while True:
            chosenDifficulty = self.processInput("Enter Difficulty 1-3:\n> ")
            if str(chosenDifficulty).isdigit():
                if int(chosenDifficulty) in range(1, 3+1):
                    self.currDifficulty = chosenDifficulty
                    break
                else:
                    Log.e("Number out of bounds!")
            else:
                Log.e("Only Numbers are allowed!")

    def reset(self):
        self.status = Status.Paused
        self.statisticRes = StatisticRes()
        self.statisticSymb = StatisticSymb()
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
                    Log.w("Game Paused! - Please Wait!")
                    paused_msg = True
                continue
            
            paused_msg = False

            print(f"Enter digit between {min}-{max}: (Difficulty: {self.currDifficulty})")
            player_pick = self.processInput()

            try:
                if player_pick == '' or Error(player_pick) is Error.NoNum:
                    continue
            except:
                pass

            if int(player_pick) not in range(min, max+1):
                Log.e("OUT OF BOUNDS")
                continue

            comp_pick = self.getComp(player_pick)
            
            print(comp_pick)
            print("\nPLayer: ", SSP(player_pick).name)
            print("Computer: ", SSP(comp_pick).name)
            print()

            comp_pick = SSP(comp_pick)
            player_pick = SSP(player_pick)

            self.statisticSymb.player_stat[player_pick] = self.statisticSymb.player_stat.get(player_pick, 0) + 1
            self.statisticSymb.comp_stat[comp_pick] = self.statisticSymb.comp_stat.get(comp_pick, 0) + 1
            
            if comp_pick == player_pick:
                self.statisticRes.draw += 1
                print("Draw!")
                continue

            if player_pick in SSP_Game.win[comp_pick]:
                self.statisticRes.comp += 1
                if(self.currDifficulty == 3):
                    print(f"Computer won! - {quotes.randomQuote()}")
                else:
                    print("Computer won!")
                continue
            
            if comp_pick in SSP_Game.win[player_pick]:
                self.statisticRes.player += 1
                print("Player won!")
                continue
    
    def getComp(self, player_pick):
        if self.currDifficulty == 1:
            return random.randrange(SSP_Game.min_ssp, SSP_Game.max_ssp+1)
        elif self.currDifficulty == 2:
            dic = self.statisticSymb.player_stat
            print(dic)
            dic_max = max(dic, key=dic.get, default=-1)
            if dic_max == -1:
                return random.randrange(SSP_Game.min_ssp, SSP_Game.max_ssp+1)
            else:
                return SSP_Game.getWinningSymb(dic_max)
        elif self.currDifficulty == 3:
            return SSP_Game.getWinningSymb(player_pick)

        return SSP.Echse

    def getWinningSymb(symb):
        win_dic = SSP_Game.win
        symb = SSP(symb)
        if any(symb in (match := dic_list) for dic_list in SSP_Game.win.values()):
            return list(win_dic.keys())[list(win_dic.values()).index(match)].value


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
            id = [x for x in self.commands if x.command == command][0].id
        except IndexError:
            return -1
        
        if isinstance(id, list):
            Log.w("Specify Command!")
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