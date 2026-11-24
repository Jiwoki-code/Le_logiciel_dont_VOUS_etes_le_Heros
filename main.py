# ###################################################################################

# What is this programme ?

# A textual-game based on 'the book with wich YOU are the Hero'
# Work with a json librairie of all the events of the book/game

# ###################################################################################

import os
from components.managers.file_manager import JSON_file

HELP_FILE, CHEAT_FILE, ERROR_FILE = JSON_file.GET_BASIC_FILES()
display: str = "hello world" # display all informations
INTERCATIONS_WORDS = ["inventaire","help","aide","123456789"]

# ###################################################################################

class Character:
    def __init__(self, name: str, habilite: int, endurence: int, luck: int, damages: int, magic: int,
                  magic_words: list, gold: int, items:list):
        self.name=name
        self.habilite=habilite
        self.endurence=endurence
        self.luck=luck
        self.damages=damages
        self.magic=magic
        self.magic_words=magic_words
        self.gold=gold
        self.items=items

    def __str__(self):
        return f"Name:{self.name}\nHabilite:{self.habilite}\nEndurence:{self.endurence}\nLuck{self.luck}\nMagic:{self.magic}\n{self.magic_words}\nGold:{self.gold}\nItems:{self.items}"

    def is_dead(self):
        return self.endurence <= 0

    def take_damage(self, amount: int):
        self.endurence-=amount

class Monster:
    def __init__(self, name, habilite, endurence, damages, loot):
        self.name=name
        self.habilite=habilite
        self.endurence=endurence
        self.damages=damages
        self.loot=loot

    def is_dead(self):
        return self.endurence <= 0

    def take_damage(self, amount: int):
        self.endurence-=amount

# ###################################################################################

def get_player_input(player_input: str): # safly get user input
    if player_input == "":
        return 1
    if player_input.lower() in "help":
        return 2
    if player_input.lower() in "inventory":
        return 3
    if player_input in "123456789" and len(player_input) <= 1:
        if int(player_input) - 1 < len(current_event.choices): # checking if the choice existe
            return 4
    if not player_input.lower() in INTERCATIONS_WORDS:
        print("Commande not founded. Type 'help' to show commande list")
        return 5

def get_choice_id(choice_index: int): # get the id of the next event
    if choice_index - 1 < current_event.number_of_choices():
        return current_event.choices[choice_index-1]["next"]
    else: # error in json files
        return "999"

def interact(player_input:str, current_event: JSON_file):
    _player_input = get_player_input(player_input)
    match _player_input:
        case 1:
            return current_event.display(), current_event
        case 2:
            return JSON_file.HELP_FILE.display(), current_event
        case 3:
            return JSON_file.ERROR_FILE.display(), current_event
        case 4: # load json file corresponding to choice index
            new_event = JSON_file.load_JSON(get_choice_id(int(player_input)))
            return new_event.display(), new_event
        case 5:
            return JSON_file.HELP_FILE.display(), current_event

# ###################################################################################

current_event = JSON_file.load_JSON("000")

display = current_event.display()

test_routine: int = 10
while test_routine > 0:

    player_input = input(" > ")
    display, new_event = interact(player_input, current_event)
    current_event = new_event
    os.system("clear")
    print(display)

    test_routine -= 1