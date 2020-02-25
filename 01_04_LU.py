#

#
#
#
#
#
#
#

#
total = 10

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
