# ###################################################################################

import os
from components.managers.file_manager import JSON_file # type: ignore
from components.character import Character, Monster, Player # type: ignore
from components.systems.combat import Combat # type: ignore

# ###################################################################################

class Game:
    def __init__(self):
        # data
        self.player=Player("glavio",10,10,2,10,10,[],10,[])
        self.current_event=None
        self.combat=None
        # game state
        self.state:str="exploration" # exploration/combat/menu/game_over
        self.running:bool=False
        self.display:str=""
        # ressources
        self.HELP_FILE, self.CHEAT_FILE, self.ERROR_FILE = JSON_file.GET_BASIC_FILES()

    def apply_conditions(self, conditions):
        pass

    def apply_choice(self, player_input:int): # interpret choices possibilites: battle, conditional choices, magic
        if "combat" in self.current_event.choices[player_input-1]:
            monster = self.current_event.choices[player_input-1]["combat"]
            self.combat=Combat(self.player,Monster(monster[0],monster[1],monster[2],monster[3],monster[4]))
            self.state="combat"

        if "conditions" in self.current_event.choices[player_input-1]:
            self.apply_conditions(self.current_event.choices[player_input-1]["conditions"])
            
        next_event_id =  self.current_event.choices[player_input-1]["next"]
        new_event = JSON_file.load_JSON(next_event_id)
        self.current_event = new_event
        self.current_event.display()

    def get_player_input(self, player_input:str): # safely get user input
        if player_input == "":
            self.current_event.display()
        elif player_input.lower() in "quit":
            self.running=False
        elif player_input.lower() in "help":
            pass #self.HELP_FILE.display()
        elif player_input.lower() in "battlegoblins":
            self.state = "combat"
        elif player_input in "123456789" and len(player_input) <= 1:
            if int(player_input) - 1 < self.current_event.number_of_choices(): # checking if the choice existe
                self.apply_choice(int(player_input))
            else:
                self.current_event.display()
                print("Choice not founded!")
        else:
            self.current_event.display()
            print("Commande not founded. Type 'help' to show commande list")

    def exploration_loop(self):
        player_input = input(" > ")
        os.system("clear")
        self.get_player_input(player_input)
       
    def combat_loop(self):
        self.combat.start()
        if self.player.is_dead():
            self.state="game_over"
            return
        self.state="exploration"
        self.current_event.display()

    def game_over(self):
        os.system("clear")
        print("Aie aie ouille ahahah et c'est perdu ! :)")

    def game_loop(self):
        while self.running:
            if self.state == "exploration":
                self.exploration_loop()
            elif self.state == "combat":
                self.combat_loop()
            elif self.state == "game_over":
                self.game_over()
                self.running=False

    def start(self):
        self.current_event = JSON_file.load_JSON("000")
        self.display = self.current_event.display()      
        self.running=True
        self.game_loop()

# ###################################################################################
