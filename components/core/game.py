# ###################################################################################

import os
from components.managers.file_manager import JSON_file # type: ignore
from components.character import Character, Monster, Player # type: ignore
from components.systems.combat import Combat # type: ignore

# ###################################################################################

class Game:
    def __init__(self):
        # data
        self.player=Player("glavio",10,10,2,1,1,[],1,[])
        self.current_event=None
        # game state
        self.state:str="combat" # exploration/combat/menu
        self.running:bool=False
        self.display:str=""
        # ressources
        self.HELP_FILE, self.CHEAT_FILE, self.ERROR_FILE = JSON_file.GET_BASIC_FILES()

    def apply_choice(self, player_input:int):

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
        elif player_input.lower() in "inventory":
            pass # display_inventory
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
        combat = Combat(self.player,Monster("Goblin",10,10,2,[]))
        combat.start()

    def game_loop(self):
        while self.running:
            if self.state == "exploration":
                self.exploration_loop()
            elif self.state == "combat":
                self.combat_loop()

    def start(self):
        self.current_event = JSON_file.load_JSON("000")
        self.display = self.current_event.display()
        self.running=True

        self.game_loop()
        pass

# ###################################################################################
