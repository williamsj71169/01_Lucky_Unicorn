#


import random


# Integer checking function below
def intcheck(question, low, high):
    valid = False
    error = "Please enter an integer between {} and {}".format(low, high)
    print()
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)

# Main routine

# Ask user hpw much they want to play with (min $1, max $10)

print()
print("Welcome")
print()
print("How this game works:")
print()
print(" - Each round costs you $1")
print(" - each round you have a chance to win some of your money back or more than you payed for each round!")
print(" - For each round, you get a token which is worth an amount of money:")
print()
print("Tokens: Donkey ($0), Horse or Zebra (50c) or a Unicorn ($5)")
print()

balance = intcheck("How much money would you like to play with? (Whole dollars between $1 and $10.)", 1, 10)
round_count = 0

keep_going = ""
while keep_going == "":

    # tokens list includes 10 items t prevent too many unicorns being chosen
    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

    # randomly choose a token from our list above
    token = random.choice(tokens)
    print()
    print("*****You got a {}*****".format(token))
    round_count += 1

    # adjust total correctly for a given token
    if token == "unicorn":
        balance += 4  # wins $5
        feedback = "Congratulations you won $5.00"
    elif token == "donkey":
        balance -= 1  # does not win anything
        feedback = "Sorry, you did not win anything this round"
    else:
        balance -= 0.5  # 'wins' 50c, paid $1 so loses 50c
        feedback = "Congratulations you won 50c"

    print()
    print(feedback)
    print("You have ${:.2f} to play with".format(balance))
    print("This is round {}.".format(round_count))
    print()

    # If user has enough money to play, ask if they want to play again
    if balance < 1:
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any other key to quit (With <enter> afterwards)")

# farewell user at the end of the game
print()
print("Thank you for playing")
