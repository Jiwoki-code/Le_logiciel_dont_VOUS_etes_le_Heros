# ###################################################################################

class Character:
    def __init__(self, name:str, habilite:int, endurence:int, damages:int):
        self.name=name
        self.habilite=habilite
        self.endurence=endurence
        self.damages=damages

    def apply(self, value:int, key:str):
        if key == "habilite": self.habilite += value
        elif key == "endurence": self.endurence += value
        elif key == "damages":self.damages += value
        else: print("KeyError")
    
    def is_dead(self):
        return self.endurence <= 0

    def take_damage(self, amount:int):
        self.endurence-=amount

class Player(Character):
    def __init__(self, name: str, habilite: int, endurence: int, damages: int, luck:int, magic:int, magic_words:list, gold:int, items:list):
        super().__init__(name, habilite, endurence, damages)
        self.luck=luck
        self.magic=magic
        self.magic_words=magic_words
        self.gold=gold
        self.items=items

    def apply(self, value: int, key: str):
        if key == "luck": self.luck += value
        elif key == "gold": self.gold += value
        elif key == "magic": self.magic += value
        else: super().apply(value, key)

    def __str__(self):
        return f"Name:{self.name}\nHabilite:{self.habilite}\nEndurence:{self.endurence}\nLuck{self.luck}\nMagic:{self.magic}\nMagic_words:{self.magic_words}\nGold:{self.gold}\nItems:{self.items}"

class Monster(Character):
    def __init__(self,name: str, habilite: int, endurence: int, damages: int, loot):
        super().__init__(name, habilite, endurence, damages)
        self.loot=loot

 ###################################################################################