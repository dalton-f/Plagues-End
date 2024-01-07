# Modules

import os
import random
import sys

# Helper Functions


def clear():
    os.system('cls')

# Main Menu


def main_menu():

    clear()

    options = {
        0: new_game,
        1: load_game,
        2: save_game,
        3: more_info,
        4: exit_game
    }

    print('0 - New Game')
    print('1 - Load Game')
    print('2 - Save Game')
    print('3 - More Info')
    print('4 - Exit')

    userInput = int(input('\n> '))

    clear()

    if userInput in options:
        options[userInput]()


def new_game():
    print('New game')


def load_game():
    print('Loading game')


def save_game():
    print('Saving game')


def more_info():
    print("In this game, you'll navigate through a post-apocalyptic world affected by a deadly virus outbreak.")
    print("Your goal is to survive and discover who you truly are.")
    print("Be careful with your choices as they may affect the outcome of the game.")


def exit_game():
    # TODO: generate random exit message using random module
    print('Embrace the unkown. Farewell, Survivor')
    sys.exit()


main_menu()
