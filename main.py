from enum import Enum
from random import *
import time
from pynput import keyboard
from colorama import init, Fore

init(autoreset=True)
controller = keyboard.Controller()
class Choose_Shop(Enum):
    Bottle_Health = 1
    UpDamage = 2
    Healper = 3
    Exit = 4
    Resurect = 5
class  Choose_Person(Enum):
    Archer = 3
    Soldier = 1
    Wizzard = 2
    Tank = 4
    NoName = 4

class Choose_Artefact(Enum):
    Bottle_Health = 2
    UpDamage = 1
    CriticalDamage = 3

class Person:
    damage = 10
    name = ""
    health = 0
    money = 100
    artefact = ""
    ulta = False
    healper = False
    timeReastartUlta = 10
    def __init__(self, artef, health):
        self.health = health
        self.artefact = artef
        if (self.artefact == Choose_Artefact.Bottle_Health):
            self.health *= 1.2
        if (self.artefact == Choose_Artefact.UpDamage):
            self.damage *= 1.1
    def make_kick(self, enemy):
        if self.check_health():
            print(self.name, "бьет" ,enemy.name)
            enemy.health -= self.damage
            self.money += randint(20,40)
            self.crit_kick(enemy)
            self.person_healper(enemy)
            enemy.resetHealth()
    def resetHealth(self):
        if not self.check_health():
            self.health = 0
    def check_health(self):
        return self.health > 0
    def useUlta(self, enemy):
        self.ulta = False
    def info(self):
        if self.health == 0:
            print(f"{self.name} - убит ")
        else:
            print('%s HP = %d' % (self.name, self.health))
    def person_healper(self,enemy):
        if self.healper:
            enemy.health -= 30
            print("Помошник", self.name, "бьет", enemy.name)
    def crit_kick(self, enemy):
        if self.artefact == Choose_Artefact.CriticalDamage and randint(0,10) == 1:
            enemy.health -= 100
            enemy.resetHealth()
            print(self.name, Fore.RED+ "Нанес критический удар", enemy.name)
    def person_resurect(self):
        self.health = 150
        self.healper = False
        self.ulta = False
        print(f"{self.name} - воскрешен")
class Shop:
    deadPersons =[]
    def resurect(self):
        print(Fore.LIGHTCYAN_EX + "Выбери кого хочешь воскресить")
        for person in self.deadPersons:
            print(f"{person.name}")
        try:
            i = int(input())
            if i == 1:
                self.deadPersons[0].person_resurect()
                self.deadPersons.pop(0)
            elif i == 2:
                self.deadPersons[1].person_resurect()
                self.deadPersons.pop(1)
        except:
            print(Fore.LIGHTRED_EX + "Введено невенрное значение!")
    def shopping(self,player, wave):
        while player.money > 150:
            try:
                type = Choose_Shop(int(input(Fore.BLUE + "Выбери предмет: ")))
            except:
                print(Fore.LIGHTRED_EX + "Выбери из предложенных вариантов!")
                continue
            if type == Choose_Shop.Bottle_Health and player.money >= 150:
                player.health += 150
                player.money -= 150
                print(f'{player.name} HP = {player.health}', Fore.LIGHTYELLOW_EX + f' Money = {player.money}')
                continue
            elif type == Choose_Shop.UpDamage and player.money >= 200:
                player.damage *= 1.5
                player.money -= 200
                print(f'{player.name} Damage = {player.damage}', Fore.LIGHTYELLOW_EX + f'Money = {player.money}')
                continue
            elif type == Choose_Shop.Exit: break
            elif type == Choose_Shop.Healper and player.money >= 350 and not player.healper:
                player.healper = True
                player.money -= 350
                print(f'{player.name} Помошник призван', Fore.LIGHTYELLOW_EX + f' Money = {player.money}')
                continue
            elif (type == Choose_Shop.Resurect and
                  player.money >= 450 and
                  wave %4 ==0 and
                  len(self.deadPersons) !=0):
                player.money -= 450
                self.resurect()
                print(f'{player.name}', Fore.LIGHTYELLOW_EX + f' Money = {player.money}')
            else: print(Fore.LIGHTRED_EX + "Ошибка!")
    def print_shop(self, players, wave):
        if (wave % 2 == 0 or wave % 5 == 0):
            print(Fore.LIGHTBLUE_EX + "-----------------Магазин------------------")
            print(Fore.LIGHTYELLOW_EX + "1 - Выпить зелье (HP + 150) = 150 Money\n")
            print(Fore.LIGHTBLUE_EX + "2 - Улучшить оружие = 200 Money\n")
            print(Fore.LIGHTCYAN_EX + "3 - Призвать помошника = 350 Money\n")
            print(Fore.LIGHTMAGENTA_EX +"4 - Выход\n")
            if (wave % 4 == 0):
                print(Fore.LIGHTWHITE_EX + "Доп.слот: 5 - Воскресить союзника = 400 Money\n")
            print(Fore.LIGHTBLUE_EX + "------------------------------------------")
            self.buy(players,wave)
    def buy(self,players,wave):
        self.deadPersons.clear()
        for person in players:
            if person.check_health():
                print(person.name,
                      Fore.GREEN + f"HP = {round(person.health)}",
                      Fore.RED + f"Damage = {round(person.damage)}",
                      Fore.LIGHTYELLOW_EX + f"Money = {round(person.money)}")
                self.shopping(person,wave)
            else:
                self.deadPersons.append(person)
###########################################
class Boss(Person):
    damage = 65
    def __init__(self):
        self.name = (Fore.RED + "Boss")
        self.health = 1000
class Phoenix(Person):
    damage = 20
    hp = 450
    def __init__(self):
        self.name = (Fore.LIGHTRED_EX + "Phoenix")
        self.health = self.hp

class Soldier(Person):
    damage = 25
    timeReastartUlta = 7
    def __init__(self, artef, name='Noname', health=100):
        self.name = Fore.LIGHTGREEN_EX + (name + "(Soldier)")
        super().__init__(artef, health)
    def useUlta(self, enemy):
        super().useUlta(enemy)
        enemy.health -= 40
        print(self.name,Fore.LIGHTYELLOW_EX +"Нанес супер-удар")

class Wizzard (Person):
    damage = 25
    timeReastartUlta = 9
    def __init__(self, artef, name='Noname', health=100):
        self.name =Fore.MAGENTA+  (name + "(Wizzard)")
        super().__init__(artef, health)
    def useUlta(self, enemy):
        super().useUlta(enemy)
        self.health += 30
        print(self.name,Fore.LIGHTYELLOW_EX + "Выпил зелье")

class Archer(Person):
    damage = 30
    timeReastartUlta = 9
    def __init__(self, artef, name='Noname', health=100):
        self.name = Fore.LIGHTBLUE_EX + (name + "(Arhcer)")
        super().__init__(artef, health)
    def useUlta(self, enemy):
        super().useUlta(enemy)
        enemy.health -= randint(0,3)*self.damage
        print(self.name,Fore.LIGHTYELLOW_EX + "Отправил град стрел")

class Tank(Person):
    damage = 10
    timeReastartUlta = 5
    def __init__(self, artef, name='Noname', health=100):
        self.name =  Fore.LIGHTYELLOW_EX +(name + "(Tank)")
        super().__init__(artef, health)
    def useUlta(self, enemy):
        super().useUlta(enemy)
        self.damage *= 1.25
        print(self.name,Fore.LIGHTYELLOW_EX + "Улучшил оружие")

class Battle:
    counterRaund = 1
    timeStartRaund = 0
    players = []
    boss = ''
    def PVP(self, players):
        self.players = players
        timeStartUlta = time.time()
        self.timeStartRaund = timeStartUlta
        while self.players[0].check_health() and  self.players[1].check_health():
            self.ControlTimeRaund(time.time() -self.timeStartRaund)
            self.keypress()
            self.generate_ulta(timeStartUlta,  self.players)
        if players[0].health > players[1].health:
            self.who_win(f"{players[0].name} - победил")
        else:
            self.who_win(f"{players[1].name} - победил")

    def PVE(self,players):
        self.players = players
        timeStartUlta = time.time()
        self.timeStartRaund = timeStartUlta
        self.boss = Boss()
        while (self.players[0].check_health() or self.players[1].check_health()) and self.boss.check_health():
            self.ControlTimeRaund(time.time() - self.timeStartRaund)
            self.keypress()
            self.generate_ulta(timeStartUlta, self.players)
        if players[0].health or players[1].health > self.boss.health:
            self.who_win(f"{players[0].name} и {players[0].name} - победили")
        else:
            self.who_win(f"{self.boss.name} - победил")

    def Arena(self,players):
        self.players = players
        self.wave = 1
        timeStartUlta = time.time()
        self.timeStartRaund = timeStartUlta
        self.boss = Phoenix()
        while self.players[0].check_health() or self.players[1].check_health() or self.players[2].check_health():
            self.ControlTimeRaund(time.time() - self.timeStartRaund)
            self.keypress()
            self.generate_ulta(timeStartUlta, self.players)
        self.who_win(Fore.LIGHTCYAN_EX + f"Вы продержались {self.wave} волн")

    def keypress(self):
        with keyboard.Events() as events:
            event = events.get(0.1)
            if event is None:
                pass
            elif event.key == keyboard.Key.ctrl_r:
                self.secondUlta()
            elif event.key == keyboard.Key.ctrl_l:
                self.firstUlta()
            elif event.key == keyboard.Key.num_lock and isinstance(self.boss,Phoenix):
                self.thirdUlta()
    def generate_ulta(self, clock, players):
        clock = time.time() - clock
        for player in players:
            if round(clock) % player.timeReastartUlta == player.timeReastartUlta - 1:
                player.ulta = True
    def who_win(self, result):
        print(result)
    def whoIsAttack(self, total):
        if isinstance(self.boss,Boss):
            attack = randint(1,3)
            if attack == 1 and self.players[0].check_health():self.players[0].make_kick(self.boss)
            elif attack == 2 and self.players[1].check_health():self.players[1].make_kick(self.boss)
            elif attack == 3:self.boss_attack(total)
            elif not self.players[0].check_health():self.players[1].make_kick(self.boss)
            elif not self.players[1].check_health():self.players[0].make_kick(self.boss)
        elif isinstance(self.boss,Phoenix):
            if randint (1,2) == 1:
                for person in total:
                    person.make_kick(self.boss)
            else:self.boss_attack(total)
        else:
            if randint(1,2) == 1:
                self.players[0].make_kick(self.players[1])
            else:
                self.players[1].make_kick(self.players[0])
    def printUltaReady(self, players):
        for player in players:
            if player.ulta == True and player.check_health():
                print(player.name,Fore.LIGHTBLUE_EX + "Ульта Готова")
    def printRaund(self):
        if isinstance(self.boss,Phoenix):
            print(Fore.LIGHTMAGENTA_EX + f'------------- Волна {self.wave} Раунд {self.counterRaund} -------------')
        else:
            print(Fore.LIGHTMAGENTA_EX + f'------------- Раунд {self.counterRaund} -------------')
        self.counterRaund += 1
    def firstUlta(self):
        if self.players[0].ulta == True and self.players[0].check_health():
            time.sleep(0.3)
            if isinstance(self.boss, (Boss,Phoenix)):self.players[0].useUlta(self.boss)
            else: self.players[0].useUlta(self.players[1])
    def secondUlta(self):
        if self.players[1].ulta == True and self.players[1].check_health():
            time.sleep(0.3)
            if isinstance(self.boss, (Boss,Phoenix)):self.players[1].useUlta(self.boss)
            else:self.players[1].useUlta(self.players[0])
    def thirdUlta(self):
        time.sleep(0.3)
        if self.players[2].ulta == True and self.players[2].check_health():self.players[2].useUlta(self.boss)
    def ControlTimeRaund(self,clock):
        if clock >= 1 or self.counterRaund == 1:
            self.printRaund()
            self.whoIsAttack(self.players)
            for player in self.players:
                player.info()
            if isinstance(self.boss,(Boss,Phoenix)): self.boss.info()
            self.printUltaReady(self.players)
            self.phoenix_life()
            self.timeStartRaund = time.time()
    def boss_attack(self, players):
        attack = randint(1,len(players))
        list_players = []
        check_attack = False
        for index in range(len(players)):
            if index + 1 == attack and players[index].check_health():
                self.boss.make_kick(players[index])
                check_attack = True
            elif players[index].check_health():
                list_players.append(players[index])
        if (not check_attack):
            attack = randint(1,len(list_players))
            if attack == 1:
                self.boss.make_kick(list_players[0])
            else:
                self.boss.make_kick(list_players[1])
    def phoenix_life(self):
        if isinstance(self.boss,Phoenix) and not self.boss.check_health():
            Shop().print_shop(self.players, self.wave)
            self.boss.hp *=1.1
            self.boss.damage *=1.1
            self.boss.health = self.boss.hp
            self.wave +=1
            self.counterRaund = 1

class Menu:
    def __init__(self):
        self.modes()
        while True:
            self.mode = input()
            if (self.mode.lower() == "pvp" or self.mode == "2"):
                Battle().PVP(self.createPlayers())
                break
            if (self.mode.lower() == "pve" or self.mode =="1"):
                Battle().PVE(self.createPlayers())
                break
            if (self.mode.lower() == "Arena" or self.mode =="3"):
                Battle().Arena(self.createPlayers())
                break
            else:
                print(Fore.LIGHTRED_EX + "Выбери из предложенных вариантов!")


    def createPlayers(self):
        if self.mode.lower() == self.mode == "Arena" or self.mode =="3":
            player1 = self.createPerson()
            player2 = self.createPerson()
            player3 = self.createPerson()
            return [player1, player2,player3]
        else:
            player1 = self.createPerson()
            player2 = self.createPerson()
            return [player1, player2]

    def modes(self):
        print(Fore.BLUE+'Выберите режим игры:\n',
              Fore.CYAN +'1 - PVE (Бой с боссом)\n',
              Fore.LIGHTGREEN_EX +'2 - PVP (1 на 1)\n',
              Fore.RED+'3 - Arena (3 против Феникса)')
    def printChooseCharecter(self):
        self.random_health()
        print(Fore.LIGHTGREEN_EX+f'1 - Soldier. HP - {self.health_lst[2]}\n'+
              Fore.MAGENTA + f'2 - Wizzard. HP - {self.health_lst[3]}\n' +
              Fore.LIGHTBLUE_EX + f"3 - Archer. HP - {self.health_lst[1]}\n" +
              Fore.LIGHTYELLOW_EX +f"4 - Tank. HP - {self.health_lst[0]}")
    def printChooseArtefact(self):
        print(Fore.LIGHTCYAN_EX+'1.Доп. урон +10%\n'+
              Fore.LIGHTGREEN_EX+"2.Доп. hp +20%\n" +
              Fore.LIGHTRED_EX+"3.Возможность крит.удара")
    def createPerson(self):
        name = input(Fore.LIGHTWHITE_EX + 'Name = ')
        while True:
            try:
                self.printChooseCharecter()
                type = Choose_Person(int(input()))
                self.printChooseArtefact()
                artefact = Choose_Artefact(int(input()))
            except:
                print (Fore.LIGHTRED_EX + f"Выбери цифрой персонажа и артефакт!")
                continue
            if type == Choose_Person.Tank:
                return Tank(artefact,name, self.health_lst[0])
            if type == Choose_Person.Archer:
                return Archer(artefact, name, self.health_lst[1])
            if type == Choose_Person.Soldier:
                return Soldier(artefact, name, self.health_lst[2])
            return Wizzard(artefact, name, self.health_lst[3])
    def random_health(self):
        tank_hp = randint(250,300)
        archer_hp = randint(110, 160)
        soldier_hp = randint(150, 200)
        wizzard_hp = randint(130, 170)
        self.health_lst = [tank_hp, archer_hp, soldier_hp, wizzard_hp]

if __name__ == "__main__":
    menu = Menu()

