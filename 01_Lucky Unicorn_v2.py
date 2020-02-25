# random
# pay amount to start game
# token - Zebra, Horse, Donkey, Unicorn (display)
# Unicorn = $5
# Zebra/Horse = 50c
# Donkey = Nothing
# max $ is 10
# continue or quit. tell how much money made of lost

import random

# Main Routine

total = int(input("How much would you like to play with?"))

keep_going = ""
while keep_going == "":

    amount_won = 0
    amount_lost = 0
    yup = "lol"

    print()
    print("Welcome")
    print()
    print("When You Pay And Press Enter, You Will Get a Token That Is Worth certain amounts of money.")
    print("You Could Get a: Donkey ($0), Horse or Zebra (50c) or a Unicorn ($5)")

    amount_paying = ("How much do you want to pay to play? (Whole num Between $1 and $10) ", 1, 10, "int")
    print()
    keep_going = (input("Push <enter> to confirm you want to pay and play or any other key to quit"))
    print()

    WORDS = ["Zebra", "Horse", "Donkey", "Unicorn"]
    word = random.choice(WORDS)
    correct = word
    print(word)

    if word == "Horse" or word == "Zebra":
        print("You won 50c!")
        amount_won += 0.50

    elif word == "Donkey":
        print("you won NOTHING!!!")

    else:
        print("You won $5!")
        amount_won += 5

    final = amount_won - amount_lost

    if final <= 0:
        total = final * -1

    else:
        total = final

    print("You have ${:.2f} to play with".format(total))

    if total < 1:
        print("Sorry you do not have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = (input("Push <enter> to play again or any other key to quit"))

print("Thank you for playing")

'''
unicorn_final = unicorn_count * 5
donkey_final = donkey_count * 0
zebra_horse_final = zebra_horse_count * 0.5
print(unicorn_final)
print(zebra_horse_final)
print(donkey_final)
final = unicorn_final + donkey_final + zebra_horse_final
print(final)
'''

