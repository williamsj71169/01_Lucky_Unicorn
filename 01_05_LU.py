#

#
#
#
#


#
total = int(input("How much would you like to play with? "))

keep_going = ""
while keep_going == "":

    #
    token = input("enter a token: ")

    #
    if token == "unicorn":
        total += 5
        feedback = "Congratulations you won $5.00"
    elif token == "donkey":
        total -= 1
        feedback = "Sorry, you did not win anything this round"
    else:
        total -= 0.5
        feedback = "Congratulations you won 50c"

    print()

    print(feedback)
    print("You have {} to play with".format(total))

    if total < 1:
        print("Sorry you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any other key to quit")

print("Thank you for playing")
