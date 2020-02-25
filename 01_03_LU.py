#
#

#
#
#
#
#
#
#

import random

HOW_MUCH = 50
tokens = ["horse","horse","horse",
          "zebra","zebra","zebra",
          "donkey","donkey","donkey", "unicorn"]

unicorn_count = 0
zebra_horse_count = 0
donkey_count = 0

for item in range(1, HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        unicorn_count += 1

    elif chosen == "donkey":
        donkey_count += 1

    else:
        zebra_horse_count += 1
        
    print(chosen)

# Money calculations
winnings = unicorn_count * 5 + zebra_horse_count * 0.5

print("**** Win / Loss Calculations ****")
print("# Unicorns: {}".format(unicorn_count))
print("# zebra_horse: {}".format(zebra_horse_count))
print("# donkey: {}".format(donkey_count))

print()
print("You spent ${}". format(HOW_MUCH))
print("You go home with ${:.2f}".format(winnings))
