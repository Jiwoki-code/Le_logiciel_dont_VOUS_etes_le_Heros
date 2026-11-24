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
        player_habilite_test = random.randint(1,6) + random.randint(1,6)
        monster_habilite_test = random.randint(1,6) + random.randint(1,6)
        player_test_result = self.player.habilite + player_habilite_test
        monster_test_result = self.enemy.habilite + monster_habilite_test
        player_is_in_good_pos:bool

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
            player_is_in_good_pos = True
        elif player_test_result < monster_test_result:
            print("L'enemie prend l'avantage dans l'échange..")
            player_is_in_good_pos = False
        else:
            print("Personne n'a pris l'avantage dans cette échange.")
            player_is_in_good_pos = False
        print("")
        print("    - touche [Entrer]: continuer")
        if self.player.luck > 0:
            print("    - 'chance' : tenter votre chance et ", end="")
            if player_is_in_good_pos:
                print("essayer de porter un coup puissant")
            else:
                print("essayer de diminuer l'impacte")
        return player_is_in_good_pos

    def combat_loop(self):
        self.next_turn()
        while self.fight_is_going():
            valid_input, choice = self.input_is_valid(input(" > "))
            if valid_input:
                if choice == 2:
                    # self.player.get_lucky()
                    pass
                self.next_turn()

    def start(self):
        os.system("clear")
        print("Un combat a commencer contre: " + self.enemy.name)
        print(self.enemy.name + " as " + str(self.enemy.endurence) + " endurence and " + str(self.enemy.habilite) + " habilite" + "\n")
        self.combat_loop()
