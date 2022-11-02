import random

zahlen_pool = []
zahlen_pool_used = []
ziehungen = []

statistik_dic = {

}

MAX_ZAHL = 45

for x in range(1, MAX_ZAHL+1):
    zahlen_pool.append(x)

random.shuffle(zahlen_pool)

def lotto_ziehung(pool):
    if len(pool) <= 0:
        print("finished")
        return False
    
    index = random.randint(0, len(pool)-1)
    ziehung = pool[index]

    pool.pop(index)
    ziehungen.append(ziehung)

def statistik(ziehung):
    global statistik_dic
    print(ziehung)
    for x in ziehung:
        statistik_dic[x] = statistik_dic.get(x, 0) + 1

def print_statistik():
    global statistik_dic
    for x in range(1, MAX_ZAHL+1):
        print("{}: ".format(x) +  str(statistik_dic[x]))

zahlen_pool_used = zahlen_pool.copy()

for x in range(1000):
    for y in range(6):
        lotto_ziehung(zahlen_pool_used)
    statistik(ziehungen)
    ziehungen = []
    zahlen_pool_used = zahlen_pool.copy()

print_statistik()
