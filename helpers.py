from data import resources, MENU, COINS


def print_report():
    for resource, meta in resources.items():
        if meta["unit"] == "$":
            print(f"{resource.title()}: {meta['unit']}{'{:.2f}'.format(meta['amount'])}")
            continue
        print(f"{resource.title()}: {meta['amount']}{meta['unit']}")


def order(drink):
    def item_order():
        can_make = check_resources(drink)
        if not can_make[0]:
            print(f"Sorry there is not enough {can_make[1]}.")
            return
        payment_accepted = take_payment(drink)
        if not payment_accepted:
            print(f"Sorry that's not enough money. Money refunded")
            return
        subtract_drink_resources(drink)
        print(f"Here is your {drink} ☕. Enjoy!")
    return item_order


def check_resources(drink):
    have_enough = True
    missing_item = ""
    for name, amount_needed in MENU[drink]["ingredients"].items():
        if amount_needed > resources[name]["amount"]:
            have_enough = False
            missing_item = name

    return [have_enough, missing_item]


def take_payment(drink):
    print("Please insert coins.")
    coin_total = 0
    for coin in COINS:
        amount = int(val_input(f"How many {coin}?: ", valid=[str(num) for num in range(0, 101)]))
        coin_total += amount * COINS[coin]

    if coin_total >= MENU[drink]["cost"]:
        change = coin_total - MENU[drink]["cost"]
        adjust_resource("money", MENU[drink]["cost"], '+')
        print(f"Here is ${'{:.2f}'.format(change)} in change.")
        return True

    return False


def adjust_resource(resource, amount, operation):
    """given resource, amount and operation('+' or '-) will adjust machines general resources"""
    if operation == "-":
        resources[resource]["amount"] -= amount
        return

    resources[resource]["amount"] += amount


def subtract_drink_resources(drink):
    for name, amount in MENU[drink]["ingredients"].items():
        adjust_resource(name, amount, '-')


def val_input(question: str, error: str = "Invalid - Try again: ", **valid_inputs: list) -> str:
    """
    function that requires user to type valid input. Will display error on invalid input and require user type another answer

    NOTE: This function will return their input as a string. If a different data type is needed the return value will need to be cast as that data type. keycontrainsts list items must be of type string. No data conversion for comparison evaluation will be done.

    ARGS:
    question (str): question that will be displayed to the user to ask for the input

    error (str) optional: message displayed to let the user their input was invalid

    valid_inputs (strlist): any number of arguments may be given. Use key=value (Ex: valid=["1","2","3","4","5"])

    RETURN: feedback (str): string representing what the user typed
    """
    response = input(question)
    while True:

        matches_valid_options = False

        for option in valid_inputs:
            if response in valid_inputs[option]:
                matches_valid_options = True
                break

        if matches_valid_options:
            return response
            break

        response = input(error)