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
        amount = int(input(f"How many {coin}?: "))
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