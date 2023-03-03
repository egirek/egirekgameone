import time
from random import randint
from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)

class Person:
    def __init__(self,artef,health):
        self.health = health
        self.ulta = False
        self.artef = artef
        self.life = True
    def hill(self):
        self.health += 10
        print(f"{self.name} \033[32mподлечился.")

    def info (self):
        if self.health == 0:
            print(f"{self.name} \033[36m- убит ")
        else:
            print('%s \033[32mHP = %d' % (self.name, self.health))

class Boss:
    __damage = 40
    def __init__(self):
        self.name = (Fore.RED + "Boss")
        self.health = 750
        self.ulta = False
        self.life = True

    def make_kick(self, enemy, time1):
        if (isinstance(enemy, Archer) == False):
            enemy.health -= self.__damage
        else:
            j = randint(0, 4)
            if (j == 1):
                print(f"{enemy.name} \033[32m\033[4mуклонился")
            else:
                enemy.health -= self.__damage
        if enemy.health < 0:
            enemy.health = 0
        krit = randint(0, 25)
        if (krit == 1):
            enemy.health -= 110
            print(self.name, "\033[31mНанес критический удар", enemy.name)
            if enemy.health < 0:
                enemy.health = 0
        print(self.name, "бьет", enemy.name)
        if (time1 >= 15 and self.ulta == False):
            self.ulta = True
            ran = randint(0, 15)
            if (ran == 1):
                enemy.health *= 0.4
                print(f"{self.name} \033[33mиспользовал свою способность - "
                      f"{enemy.name} потерял 60 %")
            enemy.health -= 15
            if enemy.health < 0:
                enemy.health = 0
            print(f"{self.name} \033[33m нанес доп.урон ")
    def splash (self,enemy1,enemy2):
        enemy1.health -= 35
        enemy2.health -= 35
        if enemy1.health < 0:
            enemy1.health = 0
        if enemy2.health < 0:
            enemy2.health = 0
        print(f"{self.name} \033[31mнанес рассекающий удар")
    def info (self):
        print('%s \033[32mHP = %d' % (self.name, self.health))

class Tank(Person):
    __damage = 10
    def __init__(self, artef, name='Noname', health=200):
        self.name = (Fore.CYAN + name + " (Tank)")
        super().__init__(artef,health)
        if (self.artef == 2):
            self.health *= 1.2

    def make_kick(self, enemy, time1):
        if (isinstance(enemy, Archer) == False):
            if (self.artef == 1):
                enemy.health -= self.__damage * 1.1
            else:
                enemy.health -= self.__damage
        else:
            j = randint(0, 5)
            if (j == 1):
                print(f"{enemy.name} \033[32m\033[4mуклонился.")
            else:
                if (self.artef == 1):
                    enemy.health -= self.__damage * 1.1
                else:
                    enemy.health -= self.__damage
        if enemy.health < 0:
            enemy.health = 0
        self.health += 5
        print(self.name, "бьет", enemy.name)
        krit = randint(0, 10)
        if (self.artef == 3):
            if (krit == 1 and self.life == True):
                enemy.health -= 100
                print(self.name, "\033[31mНанес критический удар", enemy.name)
                if enemy.health < 0:
                    enemy.health = 0
        if (time1 >= 10 and self.ulta == False):
            self.ulta = True
            self.__damage *= 1.2
            print(f"{self.name} \033[33mиспользовал свою способность - Урон был увеличен на 20%")

class Archer(Person):
    __damage = 30
    def __init__(self, artef, name='Noname', health=75):
        self.name = (Fore.BLUE + name + " (Archer)")
        super().__init__(artef, health)
        if (self.artef == 2):
            self.health *= 1.2
          
    def make_kick(self, enemy, time1):
        if (self.artef == 1):
            enemy.health -= self.__damage * 1.1
        else:
            enemy.health -= self.__damage
        if enemy.health < 0:
            enemy.health = 0
        print(self.name, "бьет", enemy.name)
        self.health += 8
        krit = randint(0, 10)
      
        if (self.artef == 3):
            if (krit == 1):
                enemy.health -= 100
                print(self.name, "\033[31mНанес критический удар", enemy.name)
                if enemy.health < 0:
                    enemy.health = 0
        if (time1 >= 10 and self.ulta == False):
            self.ulta = True
            enemy.health -= 30 * randint(1, 3)
            if enemy.health < 0:
                enemy.health = 0
            print(f"{self.name} \033[33mиспользовал свою способность - отправил град стрел")

class Wizzard(Person):
    __damage = 20
    def __init__(self, artef, name='Noname', health=75):
        self.name = (Fore.MAGENTA + name + " (Wizzard)")
        super().__init__(artef, health)
        if (self.artef == 2):
            self.health *= 1.2
    def make_kick(self, enemy, time1):
        if (isinstance(enemy, Archer) == False):
            if (self.artef == 1):
                enemy.health -= self.__damage * 1.1
            else:
                enemy.health -= self.__damage
        else:
            j = randint(0, 4)
            if (j == 1):
                print(f"{enemy.name} \033[32m\033[4mуклонился.")
            else:
                if (self.artef == 1):
                    enemy.health -= self.__damage * 1.1
                else:
                    enemy.health -= self.__damage
                  
        if enemy.health < 0:
            enemy.health = 0
        print(self.name, "бьет", enemy.name)
        self.health += 7
        krit = randint(0, 10)
        if (self.artef == 3):
            if (krit == 1):
                enemy.health -= 100
                print(self.name, "\033[31mНанес критический удар", enemy.name)
                if enemy.health < 0:
                    enemy.health = 0
        if (time1 >= 7 and self.ulta == False):
            self.ulta = True
            self.health += 15
            enemy.health -= 10
            if enemy.health < 0:
                enemy.health = 0
            print(f"{self.name} \033[33mиспользовал свою способность - кинул fireball.")

class Soldier(Person):
    __damage = 25
    def __init__(self, artef, name='Noname', health=100):
        self.name = (Fore.GREEN + name + "(Soldier)")
        super().__init__(artef,health)
        if (self.artef == 2):
            self.health *= 1.2

    def make_kick(self, enemy, time):
        if (isinstance(enemy, Archer) == False):
            if (self.artef == 1):
                enemy.health -= self.__damage * 1.1
            else:
                enemy.health -= self.__damage
        else:
            j = randint(0, 6)
            if (j == 1):
                print(f"{enemy.name} \033[32m\033[4mуклонился")
            else:
                if (self.artef == 1):
                    enemy.health -= self.__damage * 1.1
                else:
                    enemy.health -= self.__damage
        if enemy.health < 0:
            enemy.health = 0
        print(self.name, "бьет", enemy.name)
        self.health += 10
        krit = randint(0, 10)
        if (self.artef == 3):
            if (krit == 1):
                enemy.health -= 100
                print(self.name, "\033[31mНанес критический удар", enemy.name)
                if enemy.health < 0:
                    enemy.health = 0
        if (time >= 5 and self.ulta == False):
            self.ulta = True
            enemy.health -= 40
            if enemy.health < 0:
                enemy.health = 0
            print(f"{self.name} \033[33mиспользовал свою способность - нанес супер-удар")

class Battle:
    start = 0
    end = 0
    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = "Сражение не было"

    def battle(self):
        k1 = 0
        k2 = 0
        start = time.time()
        while self.u1.health > 0 and self.u2.health > 0:
            n = randint(1, 2)
            end = time.time() - start
            if n == 1:
                self.u1.make_kick(self.u2, end)
                k2 += 1
                time.sleep(1)
            else:
                self.u2.make_kick(self.u1, end)
                k1 += 1
                time.sleep(1)
            if (k1 == 3):
                self.u1.hill()
                k1 = 0
            if (k2 == 3):
                self.u2.hill()
                k2 = 0
            if (end >= 10 and self.u1.ulta == True and self.u2.ulta == True):
                self.u1.ulta = False
                self.u2.ulta = False
                start = time.time()
            self.u1.info()
            self.u2.info()
            print("--------------------------------------------------")
        if self.u1.health > self.u2.health:
            self.result = self.u1.name + "\033[36m- Победил"
        elif self.u2.health > self.u1.health:
            self.result = self.u2.name + "\033[36m- Победил"

    def who_win(self):
        print(self.result)

class Pve:
    start = 0
    end = 0
    start_boss = 0
    end_boss = 0

    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = "Сражения не было"
        self.boss = Boss()
      
    def battle(self):
        k = 0
        start = time.time()
        start_boss = time.time()
        while (self.u1.health > 0 or self.u2.health > 0) and self.boss.health > 0:
            n = randint(1, 2)
            end = time.time() - start
            end_boss = time.time() - start_boss
            if n == 1:
                if self.u1.life == True and self.u2.life == True:
                    self.u1.make_kick(self.boss, end_boss)
                    self.u2.make_kick(self.boss, end_boss)
                elif self.u2.life == False:
                    self.u1.make_kick(self.boss, end_boss)
                    print (f"{self.u2.name} убит")
                elif self.u1.life == False:
                    self.u2.make_kick(self.boss, end_boss)
                    print(f"{self.u1.name} убит")
                time.sleep(1)
            else:
                n = randint(1, 2)
                if n == 1 and self.u1.life == True:
                    self.boss.make_kick(self.u1, end)
                elif n == 2 and self.u2.life == True:
                    self.boss.make_kick(self.u2, end)
                k += 1
                time.sleep(1)
            if (k == 3):
                self.u1.hill()
                self.u2.hill()
                k = 0
            if (end >= 10 and self.u1.ulta == True and self.u2.ulta == True):
                self.u1.ulta = False
                self.u2.ulta = False
                start = time.time()
            if (end_boss >= 20 and self.boss.ulta == True):
                self.boss.ulta = False
                start_boss = time.time()
            k = randint(0,15)
            if k == 1:
                self.boss.splash(self.u1,self.u2)
            self.u1.info()
            self.u2.info()
            self.boss.info()
            print("--------------------------------------------------")
        if (self.u1.health or self.u2.health) > self.boss.health:
            self.result = self.u1.name + " и " + self.u2.name + "\033[36m- Победили"
        else:
            self.result = self.boss.name + "\033[36m- Победил"

    def who_win(self):
        print(self.result)

def generator(player):
    hp1 = randint(150, 200)
    hp2 = randint(130, 170)
    hp3 = randint(100, 150)
    hp4 = randint(250, 300)
    while True:
        print("Выбери персонажа:")
        print(Style.BRIGHT + Fore.GREEN + f"1 - Soldier. HP - {hp1}")
        print(Style.BRIGHT + Fore.MAGENTA + f"2 - Wizzard. HP - {hp2}")
        print(Style.BRIGHT + Fore.BLUE + f"3 - Archer. HP - {hp3}")
        print(Style.BRIGHT + Fore.CYAN + f"4 - Tank. HP - {hp4}")
        i = int(input())
        if i>4:
            print(Style.BRIGHT + Fore.RED + "\033[3m\033[4mВыбери персонажа из предложенных вариантов!")
            continue
        print("Выбери артефакт: ")
        print(Style.BRIGHT + Fore.YELLOW + "1.Доп. урон +10%")
        print(Style.BRIGHT + Fore.CYAN + "2.Доп. hp +20%")
        print(Style.BRIGHT + Fore.RED + "3.Возможность крит.удара")
        ar = int(input())
        if ar>3:
            print(Style.BRIGHT + Fore.RED + "\033[3m\033[4mВыбери артефакт из предложенных вариантов!")
            continue
        if (i == 1):
            return Soldier(ar, player, hp1)
        elif (i == 2):
            return Wizzard(ar, player, hp2)
        elif (i == 3):
            return Archer(ar, player, hp3)
        elif (i == 4):
            return Tank(ar, player, hp4)

class Pve1:
    start = 0
    end = 0
    start_boss = 0
    end_boss = 0

    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = "Сражения не было"
        self.boss = Boss()

    def battle(self):
        k = 0
        start = time.time()
        start_boss = time.time()
        while (self.u1.health > 0 or self.u2.health > 0) and self.boss.health > 0:
            n = randint(1, 2)
            end = time.time() - start
            end_boss = time.time() - start_boss
            if n == 1:
                if self.u1.life == True and self.u2.life == True:
                    self.u1.make_kick(self.boss, end_boss)
                    self.u2.make_kick(self.boss, end_boss)
                elif self.u2.life == False:
                    self.u1.make_kick(self.boss, end_boss)
                    print (f"{self.u2.name} убит")
                elif self.u1.life == False:
                    self.u2.make_kick(self.boss, end_boss)
                    print(f"{self.u1.name} убит")
                time.sleep(1)
            else:
                n = randint(1, 2)
                if n == 1 and self.u1.life == True:
                    self.boss.make_kick(self.u1, end)
                elif n == 2 and self.u2.life == True:
                    self.boss.make_kick(self.u2, end)
                k += 1
                time.sleep(0.5)
            if (k == 3):
                self.u1.hill()
                self.u2.hill()
                k = 0
            if (end >= 10 and self.u1.ulta == True and self.u2.ulta == True):
                self.u1.ulta = False
                self.u2.ulta = False
                start = time.time()
            if (end_boss >= 50 and self.boss.ulta == True):
                self.boss.ulta = False
                start_boss = time.time()
            k = randint(0,33)
            if k == 1:
                self.boss.splash(self.u1,self.u2)
            self.u1.info()
            self.u2.info()
            self.boss.info()
            print("--------------------------------------------------")
        if (self.u1.health or self.u2.health) > self.boss.health:
            self.result = self.u1.name + " и " + self.u2.name + "\033[36m- Победили"
        else:
            self.result = self.boss.name + "\033[36m- Победил"

    def who_win(self):
        print(self.result)

def generator(player):
    hp1 = randint(150, 200)
    hp2 = randint(130, 170)
    hp3 = randint(100, 150)
    hp4 = randint(250, 300)
    while True:
        print("Выбери персонажа:")
        print(Style.BRIGHT + Fore.GREEN + f"1 - Soldier. HP - {hp1}")
        print(Style.BRIGHT + Fore.MAGENTA + f"2 - Wizzard. HP - {hp2}")
        print(Style.BRIGHT + Fore.BLUE + f"3 - Archer. HP - {hp3}")
        print(Style.BRIGHT + Fore.CYAN + f"4 - Tank. HP - {hp4}")
        i = int(input())
        if i>4:
            print(Style.BRIGHT + Fore.RED + "\033[3m\033[4mВыбери персонажа из предложенных вариантов!")
            continue
        print("Выбери артефакт: ")
        print(Style.BRIGHT + Fore.YELLOW + "1.Доп. урон +10%")
        print(Style.BRIGHT + Fore.CYAN + "2.Доп. hp +20%")
        print(Style.BRIGHT + Fore.RED + "3.Возможность крит.удара")
        ar = int(input())
        if ar>3:
            print(Style.BRIGHT + Fore.RED + "\033[3m\033[4mВыбери артефакт из предложенных вариантов!")
            continue
        if (i == 1):
            return Soldier(ar, player, hp1)
        elif (i == 2):
            return Wizzard(ar, player, hp2)
        elif (i == 3):
            return Archer(ar, player, hp3)
        elif (i == 4):
            return Tank(ar, player, hp4)

# ---------main----------
print(Fore.CYAN + "Выберите режим игры:\n")
print(Fore.YELLOW + "\033[1m1 - PVE Boss 1 (Бой с боссом)")
print(Fore.YELLOW + "\033[1m2 - PVE Boss 2 (Бой с боссом)")
print(Fore.BLUE + "\033[1m3 - PVP (1 на 1)")
game_ragime = int(input())
player1 = input(Fore.CYAN + "\033[4m\033[3mПервый игрок: ")
first = generator(player1)
player2 = input(Fore.YELLOW + "\033[4m\033[3mВторой игрок: ")
second = generator(player2)
if game_ragime == 3:
    b = Battle(first, second)
    b.battle()
    b.who_win()
elif game_ragime == 1:
    b = Pve(first, second)
    b.battle()
    b.who_win()
elif game_ragime == 2:
    b = Pve1(first, second)
    b.battle()
    b.who_win()