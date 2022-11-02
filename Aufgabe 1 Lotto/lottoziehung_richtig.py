import random

def init_zahlen():
    for i in range(MIN_ZAHL, MAX_ZAHL-1):
        zahlen_pool.append(i)
    
    random.shuffle(zahlen_pool)


def lotto_ziehung(min, max, draws):
    ziehung = []
    for i in range(draws):
        r_index = random.randrange(0, max-min-1)
        f_number = zahlen_pool[r_index]
        l_index = len(zahlen_pool)-1-i
        zahlen_pool[r_index], zahlen_pool[l_index] = zahlen_pool[l_index], zahlen_pool[r_index]
        ziehung.append(f_number)
    return ziehung

def statistik(ziehung):
    for i in ziehung:
        statistik_dic[i] = statistik_dic.get(i, 0) + 1

def init_statistik(statistik_count, max, min, draws):
    for i in range(statistik_count):
        statistik(lotto_ziehung(min, max, draws))
        

def print_statistik(min, max, dic):
    for i in range(min, max+1):
        print("{}: ".format(i) + str(dic.get(i, 0)))

if __name__ == "__main__":
    MAX_ZAHL = 45
    MIN_ZAHL = 1
    MAX_STATISTIK = 1000
    MAX_DRAWS = 6
    zahlen_pool = []
    statistik_dic = {}

    init_zahlen()
    init_statistik(MAX_STATISTIK, MAX_ZAHL, MIN_ZAHL, MAX_DRAWS)
    print_statistik(MIN_ZAHL, MAX_ZAHL,statistik_dic)
    