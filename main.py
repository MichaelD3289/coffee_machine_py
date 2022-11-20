from data import MENU
from helpers import print_report, order, val_input

off = False


def main():
    starting_question = "What would you like? (espresso/latte/cappuccino): "
    while not off:
        user_action = val_input(starting_question, valid=[action for action in actions])

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


if __name__ == '__main__':
    add_drink_order_actions()
    main()
