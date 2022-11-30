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