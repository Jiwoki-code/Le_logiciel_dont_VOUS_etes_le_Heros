# ###################################################################################
# GAME_FOLDER/
#   ASSETS_FOLDER
#   CONTENT_FOLDER
#   COMPONENTS_FOLDER
#   main.py
#   README.md

import json
from pathlib import Path

GAME_FOLDER = Path(__file__).parent.parent.parent
CONTENT_FOLDER = GAME_FOLDER / "content"
ASSETS_FOLDER = GAME_FOLDER / "assets"
COMPONENTS_FOLDER = GAME_FOLDER / "components"

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
        for choice in self.choices:
            available_choices.append(choice)
        return available_choices

    def number_of_choices(self): # .. how many choices
        number_of_choices: int = 0
        for choice in self.choices:
            number_of_choices += 1
        return number_of_choices
    
    def load_JSON(file_id: str): # only for JSON files

        file_path = CONTENT_FOLDER / f"{file_id}.json"

        try: # except to not find the file
            with file_path.open("r", encoding="utf-8") as file:
                json_file = JSON_file(json.load(file))
        except FileNotFoundError:
            print(f"load_JSON: JSON file not founded!")
            return None
        else:
            print(f"{file_id}.json loaded!")
            return json_file

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
