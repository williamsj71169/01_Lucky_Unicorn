# random
# pay amount to start game
# token - Zebra, Horse, Donkey, Unicorn (display)
# Unicorn = $5
# Zebra/Horse = 50c
# Donkey = Nothing
# max $ is 10
# continue or quit. tell how much money made of lost

import random

play_again = ""
while play_again == "":

    def inter_check(question, low, high, int_float):

        error = "Please enter a number between {} and {}".format(low, high)

        valid = False
        while not valid:
            try:
                print()
                if int_float == "int":
                    response = int(input(question))
                else:
                    response = float(input(question))

                if low <= response <= high:
                    return response
                else:
                    print()
                    print(error)
            except ValueError:
                print()
                print(error)


    amount_won = 0
    amount_lost = 0
    higher_lower = "weirdo"
    yup = "lol"
    other = "yup"

    print()
    print("Welcome")
    print()
    print("When You Pay And Press Enter, You Will Get a Token That Is Worth certain amounts of money.")
    print("You Could Get a: Donkey ($0), Horse or Zebra (50c) or a Unicorn ($5)")

    amount_paying = inter_check("How much do you want to pay to play? (Whole num Between $1 and $10) ", 1, 10, "int")
    print()
    play_again = (input("Push <enter> to confirm you want to pay and play or any other key to quit"))
    print()

    amount_lost += amount_paying

    WORDS = ("Zebra", "Horse", "Donkey", "Unicorn")
    word = random.choice(WORDS)
    correct = word
    print(word)

    if word == "Donkey":
        print("you won NOTHING!!!")

    elif word == "Unicorn":
        print("You won $5!")
        amount_won += 5

    elif word == "Horse" or "Zebra":
        print("You won 50c!")
        amount_won += 0.50

    if amount_lost >= amount_won:
        higher_lower = "lost"

    if amount_won >= amount_lost:
        higher_lower = "won"

    final = amount_won - amount_lost

    if final <= 0:
        other = final * -1

    else:
        other = final

    if other == 0:
        other = "NOTHING"

    print()
    print("You wave won ${:.2f}, and lost ${:.2f}, ".format(amount_won, amount_lost))
    print("so, you have {} ${:.2f}". format(higher_lower, other))
    play_again = (input("Push <enter> to play again or any other key to quit"))
