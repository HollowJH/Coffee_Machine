inventory = [400, 540, 120, 9, 550]


def prepare(water, milk, beans, cost):
    inventory[0] -= water
    inventory[1] -= milk
    inventory[2] -= beans
    inventory[3] -= 1
    inventory[-1] += cost


def inv():
    return f"""The coffee machine has:
{inventory[0]} of water
{inventory[1]} of milk
{inventory[2]} of coffee beans
{inventory[3]} of disposable cups
${inventory[4]} of money\n"""


def check(water, milk, beans):
    if inventory[0] < water:
        print("Sorry, not enough water!")
    elif inventory[1] < milk:
        print("Sorry, not enough milk!")
    elif inventory[2] < beans:
        print("Sorry, not enough beans!")
    else:
        return True


while True:
    option = input("Write action (buy, fill, take, remaining, exit):\n")
    if option == "buy":
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee == "1":
            if check(250, 0, 16):
                print("I have enough resources, making you a coffee!\n")
                prepare(250, 0, 16, 4)
        elif coffee == "2":
            if check(350, 75, 20):
                print("I have enough resources, making you a coffee!\n")
                prepare(350, 75, 20, 7)
        elif coffee == "3":
            if check(200, 100, 12):
                print("I have enough resources, making you a coffee!\n")
                prepare(200, 100, 12, 6)
        elif coffee == "back":
            continue
    elif option == "fill":
        inventory[0] += int(input("Write how many ml of water do you want to add:\n"))
        inventory[1] += int(input("Write how many ml of milk do you want to add:\n"))
        inventory[2] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        inventory[3] += int(input("Write how many disposable cups of coffee do you want to add:\n"))
    elif option == "take":
        print(f"I gave you ${inventory[-1]}\n")
        inventory[-1] = 0
    elif option == "remaining":
        print("\n" + inv())
    elif option == "exit":
        break
