# import random

# coin = random.choice(["heads", "tails"])
# print(coin)

# number = random.randint(1,10)
# print(number)

# cards = ["jack", "queen", "king", "ace"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

# import statistics
# print(statistics.mean([100,90]))

import cowsay
import sys
try:
    cowsay.cow("hello, my name is", sys.argv[1])
except IndexError:
    #print("Too few arguments")
    sys.exit()

