class StatisticRes: #Result
    def __init__(self):
        self.draw = 0
        self.player = 0
        self.comp = 0

class StatisticSymb:
    def __init__(self):
        self.player_stat = {}
        self.comp_stat = {}
        self.init()
    
    def init(self):
        self.player_stat
    
    def getFullStat(self):
        stat = {}
        
        for x in self.comp_stat:
            stat[x] = self.comp_stat[x]
        
        for x in self.player_stat:
            stat[x] = self.player_stat.get(x, 0)

        return stat

    def getPlayer_stat_count(self):
        _sum = 0
        for i in self.player_stat.keys():
            _sum += self.player_stat.get(i, 0)
        return _sum
