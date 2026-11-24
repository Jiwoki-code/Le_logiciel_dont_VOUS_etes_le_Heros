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
            valid_input=True
        elif player_input == "1":
            valid_input=True
        elif player_input == "2":
            valid_input=True
        elif player_input == "3":
            valid_input=True
        else:
            valid_input=False
        return valid_input

    def next_turn(self, player_input):
        player_habilite_test = random.randint(1,6) + random.randint(1,6)
        monster_habilite_test = random.randint(1,6) + random.randint(1,6)

        print(f"Vous lancez les dées et réalisez {player_habilite_test} à votre test d'habilité!")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(f"L'enemie réalise {monster_habilite_test} à son test d'habilité!!\n")
        time.sleep(3)
        print("")
        print(self.player.name + "  " + str(self.player.habilite) + " + " + str(player_habilite_test) + " = " + str(self.player.habilite+player_habilite_test) + " /contre/ " + str(self.enemy.habilite+monster_habilite_test) + " = " + str(self.enemy.habilite) + " + " + str(monster_habilite_test) + "  " + self.enemy.name)



    def combat_loop(self):
        while self.fight_is_going():
            player_input = input(" > ")
            os.system("clear")
            if self.input_is_valid(player_input):
                self.next_turn(player_input)

    def start(self):
        print("Un combat a commencer contre: " + self.enemy.name)
        print(self.enemy.name + " as " + str(self.enemy.endurence) + " endurence and " + str(self.enemy.habilite) + " habilite")
        self.combat_loop()
