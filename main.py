import time
from random import randint
from colorama import init, Fore
from colorama import Back
from colorama import Style

init(autoreset=True)

class Shop:
    def stop(self):
        print(Fore.LIGHTRED_EX + "Недостаточно средств!")
    def shopping(self,pl,list,bool):
        while True:
            if pl.money < 150:
                break
            i = int(input(Fore.MAGENTA + f"{pl.name} выбери предмет для покупки: "))
            if i == 1 and pl.money >= 150:
                pl.health += 150
                pl.money -= 150
                print(Fore.LIGHTGREEN_EX+f"Выпил зелье. HP = {pl.health} \033[36mМoney = {pl.money}")
            elif i == 1 and pl.money < 150:
                self.stop()
            if i == 2 and pl.money >= 200:
                pl.damage *= 1.6
                pl.money -= 200
                print(Fore.BLUE + f"Оружие улучшено. Damage = {pl.damage} \033[36mМoney = {pl.money}")
            elif i == 2 and pl.money < 200:
                self.stop()
            if i ==3 and pl.money >= 350:
                pl.clone = True
                pl.money -= 350
                print(Fore.BLUE + f"Помошник призван \033[36mМoney = {pl.money}")
            elif i == 3 and pl.money < 450:
                self.stop()
            if (i == 4):
                break
            if (i == 5 and bool == True and pl.money >= 400):
                for item in list:
                    if item.life == True:
                        list.remove(item)
                if len(list) == 0:
                    print("Все союзники живы!")
                    bool = False
                else:
                    while True:
                        print(Fore.CYAN + "Выбери союзника для реанимации: ")
                        k = 1
                        for item in list:
                            print(f"{k} - {item.name}")
                            k+=1
                        k = int(input())
                        if k<=3:
                            list[k-1].life = True
                            list[k-1].health = 150
                            print(f"{list[k-1].name} - \033[35mвоскрешен")
                            pl.money -= 400
                            bool = False
                            break
                        else:
                            print(Fore.LIGHTRED_EX +"Выбери из предложенных вариантов союзников!")
            elif (i == 5 and bool == True and pl.money < 400):
                self.stop()
            elif i >=5:
                print(Fore.LIGHTRED_EX +"Выбери из предложенных товаров!")



    def buy(self,pl1,pl2,pl3,wave):
        list = [pl1,pl2,pl3]
        bool = False
        if (wave % 2 == 0 or wave % 5 == 0):
            pl1.clone = False
            pl2.clone = False
            pl3.clone = False
            print(Fore.LIGHTBLUE_EX + "-----------------Магазин------------------")
            print(Fore.LIGHTYELLOW_EX + "1 - Выпить зелье (HP + 150) = 150 Money\n")
            print(Fore.LIGHTBLUE_EX + "2 - Улучшить оружие = 200 Money\n")
            print(Fore.LIGHTCYAN_EX + "3 - Призвать помошника = 350 Money\n")
            print(Fore.LIGHTMAGENTA_EX +"4 - Выход\n")
            if (wave % 4 == 0 or wave %5 ==0):
                print(Fore.LIGHTWHITE_EX + "Доп.слот: 5 - Воскресить союзника = 400 Money\n")
                bool = True
            if pl1.life == True: self.shopping(pl1,list,bool)
            if pl2.life == True: self.shopping(pl2,list,bool)
            if pl3.life == True: self.shopping(pl3,list,bool)




class Person:
    def __init__(self, artef, health):
        self.health = health
        self.ulta = False
        self.artef = artef
        self.life = True
        self.clone = False
        if (self.artef == 2):
            self.health *= 1.2

    def duplicate(self,enemy):
        if self.clone == True and self.life == True:
            enemy.health -= 50
            if enemy.health <= 0:
                enemy.health = 0
            print(f"\033[37mПомошник {self.name} mнанес удар {enemy.name}.")
    def hill(self):
        if (self.life == True):
            self.health += 10
            print(f"{self.name} \033[32mподлечился.")

    def info(self):
        if self.health == 0:
            self.life = False
            print(f"{self.name} \033[36m- убит ")
        else:
            print('%s \033[32mHP = %d  \033[36m' % (self.name, self.health))
    def info_arena(self):
        if self.health == 0:
            self.life = False
            print(f"{self.name} \033[36m- убит ")
        else:
            print('%s \033[32mHP = %d  \033[36mMoney = %d' % (self.name, self.health,self.money))

    def archer(self, enemy, damage):
        if (isinstance(enemy, Archer) == False):
            if (self.artef == 1):
                enemy.health -= damage * 1.1
                print(self.name, "бьет", enemy.name)
            else:
                enemy.health -= damage
                print(self.name, "бьет", enemy.name)
        else:
            j = randint(0, 5)
            if (j == 1):
                print(f"{enemy.name} \033[32m\033[4mуклонился.")
            else:
                if (self.artef == 1):
                    enemy.health -= damage * 1.1
                    print(self.name, "бьет", enemy.name)
                else:
                    enemy.health -= damage
                    print(self.name, "бьет", enemy.name)


class Phoenix(Person):
    damage = 20
    hp = 450
    def __init__(self):
        self.name = (Fore.RED + "Phoenix")
        self.health = self.hp
        self.life = True

    def make_kick(self, enemy):
        if (isinstance(enemy, Archer) == False):
            enemy.health -= self.damage
            print(self.name, "бьет", enemy.name)
        else:
            j = randint(0, 4)
            if (j == 1):
                print(f"{enemy.name} \033[32m\033[4mуклонился")
            else:
                enemy.health -= self.damage
                print(self.name, "бьет", enemy.name)
        if enemy.health < 0:
            enemy.health = 0
        krit = randint(0, 25)
        if (krit == 1):
            enemy.health -= 110
            print(self.name, "\033[31mНанес критический удар", enemy.name)
            if enemy.health < 0:
                enemy.health = 0
    def ulta(self, enemy):
        if (enemy.life == True):
            print(f"{self.name} \033[33mиспользовал свою способность \n"
                  f"{enemy.name} потерял 40 % hp\n"
                  f"{self.name} потерял 25 % hp\n")
            enemy.health *= 0.6
            self.health *=0.75
            if enemy.health < 0:
                enemy.health = 0
    def splash(self, enemy1, enemy2,enemy3):
        enemy1.health -= 150
        enemy2.health -= 150
        enemy3.health -= 150
        if enemy1.health < 0:
            enemy1.health = 0
        if enemy2.health < 0:
            enemy2.health = 0
        if enemy3.health < 0:
            enemy3.health = 0
        print(f"{self.name} \033[31mнанес рассекающий удар")


class Boss(Person):
    __damage = 40
    def __init__(self):
        self.name = (Fore.RED + "Boss")
        self.health = 750
        self.life = True

    def make_kick(self, enemy):
        if (isinstance(enemy, Archer) == False):
            enemy.health -= self.__damage
            print(self.name, "бьет", enemy.name)
        else:
            j = randint(0, 4)
            if (j == 1):
                print(f"{enemy.name} \033[32m\033[4mуклонился")
            else:
                enemy.health -= self.__damage
                print(self.name, "бьет", enemy.name)
        if enemy.health < 0:
            enemy.health = 0
        krit = randint(0, 25)
        if (krit == 1):
            enemy.health -= 110
            print(self.name, "\033[31mНанес критический удар", enemy.name)
            if enemy.health < 0:
                enemy.health = 0

    def ulta(self, enemy):
        ran = randint(0, 15)
        if (ran == 1):
            enemy.health *= 0.4
            print(f"{self.name} \033[33mиспользовал свою способность - {enemy.name} потерял 60 %")
            enemy.health -= 15
        if enemy.health < 0:
            enemy.health = 0
        print(f"{self.name} \033[33m нанес доп.урон ")

    def splash(self, enemy1, enemy2):
        enemy1.health -= 35
        enemy2.health -= 35
        if enemy1.health < 0:
            enemy1.health = 0
        if enemy2.health < 0:
            enemy2.health = 0
        print(f"{self.name} \033[31mнанес рассекающий удар")


class Tank(Person):
    damage = 10
    def __init__(self, artef, name='Noname', health=200):
        self.name = (Fore.CYAN + name + " (Tank)")
        super().__init__(artef, health)
        self.money = 100

    def make_kick(self, enemy, time1):
        if (self.life == True):
            self.archer(enemy, self.damage)
            if enemy.health < 0:
                enemy.health = 0
            self.health += 5
            self.money += 7
            krit = randint(0, 10)
            if (self.artef == 3):
                if (krit == 1 and self.life == True):
                    enemy.health -= 100
                    print(self.name, "\033[31mНанес критический удар", enemy.name)
                    if enemy.health < 0:
                        enemy.health = 0
            if (time1 >= 7 and self.ulta == False):
                self.ulta = True
                self.money += 10
                self.damage *= 1.2
                print(f"{self.name} \033[33mиспользовал свою способность - Урон был увеличен на 20%")
            self.duplicate(enemy)


class Archer(Person):
    damage = 40
    def __init__(self, artef, name='Noname', health=75):
        self.name = (Fore.BLUE + name + " (Archer)")
        super().__init__(artef, health)
        self.money = 100

    def make_kick(self, enemy, time1):
        if (self.life == True):
            if (self.artef == 1):
                enemy.health -= self.damage * 1.1
            else:
                enemy.health -= self.damage
            if enemy.health < 0:
                enemy.health = 0
            print(self.name, "бьет", enemy.name)
            self.health += 8
            self.money += randint(4,15)
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
            self.duplicate(enemy)


class Wizzard(Person):
    damage = 25
    def __init__(self, artef, name='Noname', health=75):
        self.name = (Fore.MAGENTA + name + " (Wizzard)")
        super().__init__(artef, health)
        self.money = 100
    def make_kick(self, enemy, time1):
        if (self.life == True):
            self.archer(enemy, self.damage)
            if enemy.health < 0:
                enemy.health = 0
            self.health += 7
            self.money += randint(7,18)
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
                self.money += 10
                enemy.health -= 10
                if enemy.health < 0:
                    enemy.health = 0
                print(f"{self.name} \033[33mиспользовал свою способность - кинул fireball.")
            self.duplicate(enemy)


class Soldier(Person):
    damage = 25
    def __init__(self, artef, name='Noname', health=100):
        self.name = (Fore.GREEN + name + "(Soldier)")
        super().__init__(artef, health)
        self.money = 100
    def make_kick(self, enemy, time1):
        if (self.life == True):
            self.archer(enemy, self.damage)
            if enemy.health < 0:
                enemy.health = 0
            self.health += 10
            self.money += randint(5,16)
            krit = randint(0, 10)
            if (self.artef == 3):
                if (krit == 1):
                    enemy.health -= 110
                    print(self.name, "\033[31mНанес критический удар", enemy.name)
                    if enemy.health < 0:
                        enemy.health = 0
            if (time1 >= 5 and self.ulta == False):
                self.ulta = True
                enemy.health -= 40
                self.money += 10
                if enemy.health < 0:
                    enemy.health = 0
                print(f"{self.name} \033[33mиспользовал свою способность - нанес супер-удар")
            self.duplicate(enemy)


class Battle:
    start = 0
    end = 0
    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = "Сражение не было"
        self.raund = 1

    def battle(self):
        k1 = 0
        k2 = 0
        start = time.time()
        while self.u1.health > 0 and self.u2.health > 0:
            print(Fore.LIGHTMAGENTA_EX + f"-----------------Раунд {self.raund}--------------------")
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
            self.raund += 1
        if self.u1.health > self.u2.health:
            self.result = self.u1.name + "\033[36m- Победил"
        elif self.u2.health > self.u1.health:
            self.result = self.u2.name + "\033[36m- Победил"

    def who_win(self):
        print(self.result)


class Pve(Battle):
    start_boss = 0
    end_boss = 0

    def __init__(self, u1, u2):
        super().__init__(u1, u2)
        self.boss = Boss()

    def battle(self):
        k = 0
        start = time.time()
        start_boss = time.time()
        while (self.u1.health > 0 or self.u2.health > 0) and self.boss.health > 0:
            print(Fore.LIGHTMAGENTA_EX + f"-----------------Раунд {self.raund}--------------------")
            n = randint(1, 2)
            end = time.time() - start
            end_boss = time.time() - start_boss
            if n == 1:
                self.u1.make_kick(self.boss, end)
                self.u2.make_kick(self.boss, end)
                time.sleep(1)
            else:
                n = randint(1, 2)
                if n == 1 and self.u1.life == True:
                    self.boss.make_kick(self.u1)
                elif n == 2 and self.u2.life == True:
                    self.boss.make_kick(self.u2)
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
            if (end_boss >= 15):
                if randint(1, 2) == 1 and self.u1.life == True:
                    self.boss.ulta(self.u1)
                elif self.u2.life == True:
                    self.boss.ulta(self.u2)
                start_boss = time.time()
            if randint(0, 17) == 1:
                self.boss.splash(self.u1, self.u2)
            self.u1.info()
            self.u2.info()
            self.boss.info()
            self.raund += 1
        if (self.u1.health or self.u2.health) > self.boss.health:
            self.result = self.u1.name + " и " + self.u2.name + "\033[36m- Победили"
        else:
            self.result = self.boss.name + "\033[36m- Победил"


class Arena(Battle):
    def __init__(self, pl1, pl2, pl3):
        self.pl1 = pl1
        self.pl2 = pl2
        self.pl3 = pl3
        self.result = "Сражение не было"
        self.raund = 1
        self.wave = 1
        self.phoenix = Phoenix()
        self.shop = Shop()

    def battle(self):
        k = 0
        start = time.time()
        start_boss = time.time()
        while self.pl1.life == True or self.pl2.life == True or self.pl3.life == True:
            print(Fore.LIGHTMAGENTA_EX + f"------------Волна {self.wave} Раунд {self.raund}------------------")
            if self.raund == 1:
                start_boss = time.time()
            n = randint(1, 2)
            end = time.time() - start
            end_boss = time.time() - start_boss
            if n == 1 and self.phoenix.life == True:
                self.pl1.make_kick(self.phoenix, end)
                self.pl2.make_kick(self.phoenix, end)
                self.pl3.make_kick(self.phoenix, end)
            else:
                n = randint(1, 3)
                if n == 1 and self.pl1.life == True:
                    self.phoenix.make_kick(self.pl1)
                elif n == 2 and self.pl2.life == True:
                    self.phoenix.make_kick(self.pl2)
                elif n == 3 and self.pl3.life == True:
                    self.phoenix.make_kick(self.pl3)
                elif self.pl1.life == False:
                    n = randint(1,2)
                    if n == 1 and self.pl2.life == True:
                        self.phoenix.make_kick(self.pl2)
                    else:
                        self.phoenix.make_kick(self.pl3)
                elif self.pl2.life == False:
                    n = randint(1,2)
                    if n == 1 and self.pl3.life == True:
                        self.phoenix.make_kick(self.pl3)
                    else:
                        self.phoenix.make_kick(self.pl1)
                elif self.pl3.life == False:
                    n = randint(1,2)
                    if n == 1 and self.pl1.life == True:
                        self.phoenix.make_kick(self.pl1)
                    else:
                        self.phoenix.make_kick(self.pl2)
                k += 1
                time.sleep(1)
            if k == 3:
                self.pl1.hill()
                self.pl2.hill()
                self.pl3.hill()
                k = 0
            if end >= 10 and self.pl1.ulta == True and self.pl2.ulta == True and self.pl3.ulta == True:
                self.pl1.ulta = False
                self.pl2.ulta = False
                self.pl3.ulta = False
                start = time.time()
            if end_boss >= 15 and self.wave >= 3 and self.phoenix.life == True:
                i = randint(1, 3)
                if i == 1:
                    self.phoenix.ulta(self.pl1)
                elif i ==2:
                    self.phoenix.ulta(self.pl2)
                elif i == 3:
                    self.phoenix.ulta(self.pl3)
                start_boss = time.time()
            if randint(0, 20) == 1 and self.wave >= 4 and self.phoenix.life == True:
                self.phoenix.splash(self.pl1, self.pl2,self.pl3)
            self.info()
        self.result = Fore.LIGHTCYAN_EX + f"Вы Продержались {self.wave} волн";

    def info (self):
        self.pl1.info_arena()
        self.pl2.info_arena()
        self.pl3.info_arena()
        self.phoenix.info()
        if self.phoenix.life == False:
            self.phoenix.life = True
            self.phoenix.hp *= 1.08
            self.phoenix.damage *= 1.10
            self.phoenix.health = self.phoenix.hp
            self.shop.buy(self.pl1, self.pl2, self.pl3, self.wave)
            self.wave += 1
            self.raund = 0
        self.raund += 1

def generator(player):
    hp1 = randint(150, 200)
    hp2 = randint(130, 170)
    hp3 = randint(110, 160)
    hp4 = randint(250, 300)
    while True:
        print("Выбери персонажа:")
        print(Style.BRIGHT + Fore.GREEN + f"1 - Soldier. HP - {hp1}")
        print(Style.BRIGHT + Fore.MAGENTA + f"2 - Wizzard. HP - {hp2}")
        print(Style.BRIGHT + Fore.BLUE + f"3 - Archer. HP - {hp3}")
        print(Style.BRIGHT + Fore.CYAN + f"4 - Tank. HP - {hp4}")
        i = int(input())
        if i > 4:
            print(Style.BRIGHT + Fore.RED + "\033[3m\033[4mВыбери персонажа из предложенных вариантов!")
            continue
        print("Выбери артефакт: ")
        print(Style.BRIGHT + Fore.YELLOW + "1.Доп. урон +10%")
        print(Style.BRIGHT + Fore.CYAN + "2.Доп. hp +20%")
        print(Style.BRIGHT + Fore.RED + "3.Возможность крит.удара")
        ar = int(input())
        if ar > 3:
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
while True:
    print(Fore.CYAN + "Выберите режим игры:\n")
    print(Fore.YELLOW + "\033[1m1 - PVE (Бой с боссом)")
    print(Fore.BLUE + "\033[1m2 - PVP (1 на 1)")
    print(Fore.MAGENTA + "\033[1m3 - Arena (3 против Феникса)")
    game_ragimens = int(input())
    if game_ragimens >= 4:
        print(Style.BRIGHT + Fore.RED + "\033[3m\033[4mВыбери режим игры из предложенных вариантов!")
    else:
        break
player1 = input(Fore.CYAN + "\033[4m\033[3mПервый игрок: ")
first = generator(player1)
player2 = input(Fore.YELLOW + "\033[4m\033[3mВторой игрок: ")
second = generator(player2)
if game_ragimens == 3:
    player3 = input(Fore.LIGHTMAGENTA_EX + "\033[4m\033[3mТретий игрок: ")
    third = generator(player3)
    b = Arena(first, second,third)
    b.battle()
    b.who_win()
if game_ragimens == 2:
    b = Battle(first, second)
    b.battle()
    b.who_win()
elif game_ragimens == 1:
    b = Pve(first, second)
    b.battle()
    b.who_win()
