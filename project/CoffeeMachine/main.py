MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



# TODO task 1: display the menu to chose what drink user want
#  It also take input as report to share what is currently in the stock and money in the account


def report_calc(current_resources, drink):
    d_milk = MENU[drink]["ingredients"]["milk"]
    d_coffee = MENU[drink]["ingredients"]["coffee"]
    d_water = MENU[drink]["ingredients"]["water"]
    calc_water = current_resources["water"]
    calc_milk = current_resources["milk"]
    calc_coffee = current_resources["coffee"]
    current_resources["water"] = calc_water - d_water
    current_resources["milk"] = calc_milk - d_milk
    current_resources["coffee"] = calc_coffee - d_coffee
    return current_resources


def cost_check(drink):
    cost = float(MENU[drink]["cost"])
    return cost




def coffee_machine():
    need_coffee = True
    money_left_in_machine = 0
    def report_only():
        print("These are the resources left in the machine Water {}, milk {}, coffee {}".format(resources["water"],
                                                                                                resources["coffee"],
                                                                                                resources["milk"]))
        answer = money_left_in_machine
        return answer
    while need_coffee:
        # TODO task 2: User input to choose which drink
        drink_chosen = input("What drink you like: espresso/Latte/cappuccino: ").lower()
        if drink_chosen == "report":
            print(report_only())
            coffee_machine()

        # TODO task 3: Please insert the coin input will ask user with given options
        quarters = int(input("how many quarters? "))
        dimes = int(input("how many dimes?: "))
        nickle = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        # TODO task 4: Once the coin given, calculate if it's more than drink return remaining
        #  and serve the drink. If money not sufficient refund and don't server drink


        def money_calc(quarters_count, dimes_count, nickle_count, pennies_count, drink_price, active_resources, money_left_in_machine, need_coffee):
            q_total = quarters_count * 0.25
            d_total = dimes_count * 0.10
            n_total = nickle_count * 0.05
            p_total = pennies_count * 0.01
            total = float(q_total + d_total + n_total + p_total)
            corrected_float = float("{:.2f}".format(total))
            if corrected_float > drink_price:
                if active_resources["water"] >= MENU[drink_chosen]["ingredients"]["water"] and active_resources["milk"] >= MENU[drink_chosen]["ingredients"]["milk"] and active_resources["coffee"] >= MENU[drink_chosen]["ingredients"]["coffee"]:
                    print(f"Here is your {drink_chosen}. Enjoy!")
                    report_calc(active_resources, drink_chosen)
                    money_left_in_machine += drink_price
                    return corrected_float - drink_price, money_left_in_machine
                else: #active_resources["water"] <= MENU[drink_chosen]["ingredients"]["water"] and active_resources["milk"] <= MENU[drink_chosen]["ingredients"]["milk"] and active_resources["coffee"] <= MENU[drink_chosen]["ingredients"]["coffee"]:
                    print(f"Sorry that's not enough resource  for the drink chosen {drink_chosen}, money refunded.")
                    need_coffee = False
                    exit()
            elif corrected_float < drink_price:
                print(f"Sorry that's not enough money to buy {drink_chosen}, money refunded.")
                need_coffee = False
                return None

        price_of_drink = cost_check(drink_chosen)

        result = money_calc(quarters, dimes, nickle, pennies, price_of_drink, resources, money_left_in_machine, need_coffee)

        # print(type(result))
        if result is not None:
            money_left_in_machine += result[1]
            print(f"This is the money refunded {result[0]}")
            print(f"This is the money left in the machine {result[1]}")

coffee_machine()