# ###################################################################################

# What is this programme ?

# A textual-game based on 'the book with wich YOU are the Hero'
# Work with a json librairie of all the events of the book/game

# ###################################################################################

from components.core.game import Game

# ###################################################################################

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()