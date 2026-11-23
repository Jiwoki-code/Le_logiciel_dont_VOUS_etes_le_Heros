# ###################################################################################

# What is this programme ?

# A textual-game based on 'the book with wich YOU are the Hero'
# Work with a json librairie of all the events of the book/game

# ###################################################################################

import os
import json
from pathlib import Path

display: str = "hello world" # display all informations
INTERCATIONS_WORDS = ["inventaire","help","aide","123456789"]

# ###################################################################################

class JSON_file: # represent an event
    def __init__(self, json_file):
        self.json_file=json_file
        self.id=json_file["id"]
        self.text=json_file["text"]
        self.choices=json_file["choices"]

    def display(self): # return a string to concatenate with 'display' variable
        index = 1
        display: str = ""
        display += "\n" + self.text + "\n"
        for choice in self.choices:
            display += f"    {index} - {choice["text"]}\n"
            index += 1
        return display

    def available_choices_list(self): # return list of choices
        available_choices: list = []
        for choice in current_event.choices:
            available_choices.append(choice)
        return available_choices

    def number_of_choices(self): # .. how many choices
        number_of_choices: int = 0
        for choice in current_event.choices:
            number_of_choices += 1
        return number_of_choices

# ###################################################################################

# setting folders path assuming:
# GAME_FOLDER/
#   ASSETS_FOLDER
#   CONTENT_FOLDER
#   COMPONENTS_FOLDER
#   main.py
#   README.md

GAME_FOLDER = Path(__file__).parent
CONTENT_FOLDER = GAME_FOLDER / "content"
ASSETS_FOLDER = GAME_FOLDER / "assets"
COMPONENTS_FOLDER = GAME_FOLDER / "components"

def GET_BASIC_FILES():
    file_path = CONTENT_FOLDER / "997.json"
    with file_path.open("r", encoding="utf-8") as file:
        HELP_FILE = JSON_file(json.load(file))
    file_path = CONTENT_FOLDER / "998.json"
    with file_path.open("r", encoding="utf-8") as file:
        CHEAT_FILE = JSON_file(json.load(file))
    file_path = CONTENT_FOLDER / "999.json"
    with file_path.open("r", encoding="utf-8") as file:
        ERROR_FILE = JSON_file(json.load(file))
    return HELP_FILE, CHEAT_FILE, ERROR_FILE
    
HELP_FILE, CHEAT_FILE, ERROR_FILE = GET_BASIC_FILES()

def GET_FILE_PATH(folder_path: Path, file_name: str):
    if folder_path == CONTENT_FOLDER:
        return CONTENT_FOLDER / f"{file_name}.json"
    if folder_path == COMPONENTS_FOLDER:
        return COMPONENTS_FOLDER / f"{file_name}.py"
    if folder_path == ASSETS_FOLDER:
        return ASSETS_FOLDER / f"{file_name}.png"

def load_JSON(file_id: str): # only for JSON files

    file_path = GET_FILE_PATH(CONTENT_FOLDER, file_id)

    try: # except to not find the file
        with file_path.open("r", encoding="utf-8") as file:
            json_file = JSON_file(json.load(file))
    except FileNotFoundError:
        print(f"load_JSON: JSON file not founded!")
        return None
    else:
        print(f"{json_file.id}.json loaded!")
        return json_file

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
            return HELP_FILE.display(), current_event
        case 3:
            return ERROR_FILE.display(), current_event
        case 4:
            new_event = load_JSON(get_choice_id(int(player_input)))
            return new_event.display(), new_event
        case 5:
            return HELP_FILE.display(), current_event

# ###################################################################################

current_event = load_JSON("000")
test_routine: int = 10
display = current_event.display()

while test_routine > 0:

    player_input = input(" > ")
    display, new_event = interact(player_input, current_event)
    current_event = new_event

    os.system("clear")
    print(display)

    test_routine -= 1