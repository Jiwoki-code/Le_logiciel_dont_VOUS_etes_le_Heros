# ###################################################################################

import random
import os
import time

# ###################################################################################
class Combat:
    def __init__(self, player, enemy):
        self.player=player
        self.enemy=enemy
        
    def fight_is_going(self):
        return not self.player.is_dead() and not self.enemy.is_dead()

    def input_is_valid(self, player_input):
        valid_input:bool=False
        if player_input == "":
            choice = 1
            valid_input=True
        elif player_input in "chance":
            valid_input=True
            choice = 2
        else:
            valid_input=False
            choice = 0
        return valid_input, choice

    def next_turn(self):
        if not self.fight_is_going():
            return
        player_habilite_test = random.randint(1,6) + random.randint(1,6)
        monster_habilite_test = random.randint(1,6) + random.randint(1,6)
        player_test_result = self.player.habilite + player_habilite_test
        monster_test_result = self.enemy.habilite + monster_habilite_test
        is_in_good_pos:int

        time.sleep(.7)
        print(f"Vous lancez les dées et réalisez {player_habilite_test} à votre test d'habilité!")
        time.sleep(.7)
        print(".")
        time.sleep(.7)
        print(".")
        time.sleep(.7)
        print(f"L'enemie réalise {monster_habilite_test} à son test d'habilité!!")
        time.sleep(.7)
        print("")
        time.sleep(.7)
        print(self.player.name + "  " + str(self.player.habilite) + " + " + str(player_habilite_test) + " = " + str(player_test_result) + " /contre/ " + str(monster_test_result) + " = " + str(self.enemy.habilite) + " + " + str(monster_habilite_test) + "  " + self.enemy.name)
        print("")
        if monster_test_result < player_test_result:
            print("Vous prenez l'avantage dans l'échange..")
            is_in_good_pos = 1
        elif player_test_result < monster_test_result:
            print("L'enemie prend l'avantage dans l'échange..")
            is_in_good_pos = 2
        else:
            print("Personne n'a pris l'avantage dans cette échange.")
            is_in_good_pos = 3
        print("")
        if self.player.luck > 0 and is_in_good_pos != 3:
            print("    - 'chance' : 'tenter votre chance' et ", end="")
            if is_in_good_pos == 1:
                print("essayer de porter un coup puissant")
            elif is_in_good_pos == 2:
                print("essayer de diminuer l'impacte")
        print("    - touche [Entrer]: continuer")
        return is_in_good_pos # 1 - avantage/ 2 - disavantage/ 3 - null

    def apply_result(self, luck_id:int,is_in_good_pos:int):
        os.system("clear")
        damages:int
        if is_in_good_pos == 1:
            target = self.enemy.endurence
            source = self.player.damages
            if luck_id == 3: # None
                damages = source
                target -= source
            if luck_id == 1: # is lucky
                damages = source + 1
                target -= source + 1
                print("Vous tenter votre chance et essayer de porter un coup puissant, se qui fonctionne!")
                print("")
            if luck_id == 2: # is unlucky
                damages = source - 1
                target -= source - 1
                print("Vous tenter votre chance et essayer de porter un coup puissant mais cela ne fonctionne pas!")
                print("")
            print(f"L'enemy subie {damages} dégats, ",end="")
            self.enemy.apply(-damages, "endurence")
            if self.enemy.is_dead():
                print(f"Vous trionpher de {self.enemy.name}!")
            else:
                print(f"l'endurence de {self.enemy.name} est de {self.enemy.endurence}")
            print("")
            print("    - touche [Entrer]: continuer")
            input(" > ")
        elif is_in_good_pos == 2:
            target = self.player.endurence
            source = self.enemy.damages
            if luck_id == 3:
                damages = source
                target -= source
            if luck_id == 1: # is lucky
                damages = source - 1
                target -= source - 1
                print("Vous tenter votre chance et essayer de diminuer l'impacte, se qui fonctionne!")
                print("")
            if luck_id == 2: # is unlucky
                damages = source + 1
                target -= source + 1
                print("Vous tenter votre chance et essayer de diminuer l'impacte mais cela ne fonctionne pas!")
                print("")
            print(f"Vous subissez {damages} dégats, ",end="")
            self.player.apply(-damages, "endurence")
            if self.player.is_dead():
                print(f"{self.enemy.name} a trionpher de vous!")
            else:
                print(f"votre endurence est de {self.player.endurence}")
            print("")
            print("    - touche [Entrer]: continuer")
            input(" > ")
        os.system("clear")

    def combat_loop(self):
        is_in_good_pos = self.next_turn()
        while self.fight_is_going():
            valid_input, choice = self.input_is_valid(input(" > "))
            if valid_input:
                if choice == 2: # use 'chance' commmand
                    luck_id = self.player.get_lucky()
                else:
                    luck_id = 3
                self.apply_result(luck_id, is_in_good_pos)
                is_in_good_pos = self.next_turn()

    def start(self):
        os.system("clear")
        print("Un combat a commencer contre: " + self.enemy.name)
        print(self.enemy.name + " as " + str(self.enemy.endurence) + " endurence and " + str(self.enemy.habilite) + " habilite" + "\n")
        self.combat_loop()
