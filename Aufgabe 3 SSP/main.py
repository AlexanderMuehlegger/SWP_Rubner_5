from tabulate import tabulate
import random
import quotes
from enums import SSP, Error, Status
from commands import Command, CommandHandler
from statistics_1 import StatisticRes, StatisticSymb
from terminal import Log
import requests
import json
from rich.console import Console
from rich.progress import track
import time

class SSP_Game:

    win = {
        SSP.Schere: [SSP.Papier, SSP.Echse],
        SSP.Papier: [SSP.Stein, SSP.Spock],
        SSP.Stein: [SSP.Echse, SSP.Schere],
        SSP.Echse: [SSP.Spock, SSP.Papier],
        SSP.Spock: [SSP.Schere, SSP.Stein]
    }

    server_url = "http://127.0.0.1:5000/api/"

    min_ssp = 1
    max_ssp = 5
    console = Console()

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

        statisticCommand = Command(-1, self.printStatistic, "Print current statistic", "-p")
        self.commandHandler.addCommand(statisticCommand)

        saveStatisticCommand = Command(-1, self.saveStatistic, "Saves and resets current statistic", "-s")
        self.commandHandler.addCommand(saveStatisticCommand)

        resetCommand = Command(-1, self.reset, "Resets current Statistic", "-r")
        self.commandHandler.addCommand(resetCommand)

        difficultyCommand = Command(-1, self.setDifficulty, "Sets new Difficulty", "-d")
        self.commandHandler.addCommand(difficultyCommand)
        
        printSymbolCommand = Command(-1, self.printSymb, "Prints numbers of Symbols", "-symb")
        self.commandHandler.addCommand(printSymbolCommand)
    

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
        Log.s("Reset Complete!")
        self.status = Status.Running
        self.setDifficulty()

    def printInfo(self):
        print("".ljust(50, "-"))
        print("Schere, Stein, Papier, Spock, Echse".center(50, " "))
        print("See all commands with -h".center(50, " "))
        print("".ljust(50, "-"))
        self.printSymb()

    def printHelp(self):
        print()
        toprint = []
        for x in self.commandHandler.commands:
            toprint.append(x.getOutputList())
        print(tabulate(toprint, headers=['Command', 'Description']))
        print()
    
    def printSymb(self):
        SSP.__str__()

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

        

    def saveStatistic(self):
        name = self.processInput('Username: ', noNum=True)
        data = {
            "username": str(name),
            "statistics": {
                "Schere": self.statisticSymb.player_stat.get(SSP.Schere, 0),
                "Stein": self.statisticSymb.player_stat.get(SSP.Stein, 0),
                "Papier": self.statisticSymb.player_stat.get(SSP.Papier, 0),
                "Echse": self.statisticSymb.player_stat.get(SSP.Echse, 0),
                "Spock": self.statisticSymb.player_stat.get(SSP.Spock, 0),
            },
            "result": {
                "Computer": self.statisticRes.comp,
                "Player": self.statisticRes.player,
                "Draw": self.statisticRes.draw
            }
        }
        json_data = json.dumps(data)
        result = ""
        try:
            result = requests.post(SSP_Game.server_url + "saveStatistic", data=json_data)
        except:
            with SSP_Game.console.status("[bold yellow]Connecting to Server...", spinner='line') as status:
                for i in range(10):
                    time.sleep(.6)
            SSP_Game.console.print(":x: [red]Connection to server failed!")    
            return

        
        for i in track(range(10), description="Saving..."):
            time.sleep(.5)
        result = result.json()
        if 'ERROR' in result:
            SSP_Game.console.print(":x: [red] Something went wrong turing saving!")
        elif 'Response' in result:
            SSP_Game.console.print(':white_check_mark: [green] Data saved successfully!')
        self.reset()

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
            
            dic = self.statisticSymb.player_stat.copy()

            if not dic:
                return random.randrange(SSP_Game.min_ssp, SSP_Game.max_ssp+1)

            max_symb = self.statisticSymb.getPlayer_stat_count()
            dic_max = []
            for i in range(3):
                dic_max.append(max(dic, key=dic.get, default=-1))
                if -1 == dic_max[-1]:
                    del dic_max[-1]
                    continue
                else:
                    if dic_max[-1] != -1:
                        del dic[dic_max[-1]]

            prop_win = []
            dic = self.statisticSymb.player_stat.copy()

            for i in dic_max:
                prop_win.append(SSP_Game.getWinningSymb(i))
            
            rngNum = random.uniform(0, 1)
            
            for i in range(len(dic_max)):
                if dic[dic_max[i]]/max_symb <= rngNum:
                    return SSP_Game.getWinningSymb(prop_win[i])

            return prop_win[0]
            
        elif self.currDifficulty == 3:
            return SSP_Game.getWinningSymb(player_pick)

        return SSP.Echse

    def getWinningSymb(symb):
        win_dic = SSP_Game.win
        symb = SSP(symb)
        if any(symb in (match := dic_list) for dic_list in SSP_Game.win.values()):
            return list(win_dic.keys())[list(win_dic.values()).index(match)].value


    def processInput(self, msg='> ', noNum=False):
        text = input(msg)
        if self.commandHandler.runCommand(text) == 1:
            return ""
        
        if noNum:
            return text

        try:
            text = int(text)
        except:
            return Error.NoNum
        return text


def main():
    console = Console()
    game = SSP_Game()
    game.start()


if __name__ == "__main__":
    main()