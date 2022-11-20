# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from data import MENU
from helpers import print_report, order, val_input

off = False


def main():

    while not off:
        user_action = val_input("What would you like? (espresso/latte/cappuccino): ", valid=[action for action in actions])

        actions[user_action]()


def turn_off():
    global off
    off = True


actions = {
    "off": turn_off,
    "report": print_report,
}


def add_drink_order_actions():
    for drink in MENU:
        actions[drink] = order(drink)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_drink_order_actions()
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
