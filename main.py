# Modules

import os

# Helper Functions


def clear():
    os.system('cls')

# Main Menu


def main_menu():

    os.system('cls')

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

    userInput = int(input('> '))

    if userInput in options:
        options[userInput]()


def new_game():
    os.system('cls')
    print('New game')


def load_game():
    os.system('cls')
    print('Loading game')


def save_game():
    os.system('cls')
    print('Saving game')


def more_info():
    os.system('cls')
    print('Coming Soon...')


def exit_game():
    os.system('cls')
    print('Exiting Game')


main_menu()
