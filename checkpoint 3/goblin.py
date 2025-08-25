import random
print("Welcome to the goblin game")
print("The best game ever")
player_name = input("Write your name: ")
print(player_name, "can you find the goblin?")
print("|_|"*5)

goblin_position = random.randint(1,5)
keep_trying = True
while keep_trying:
    guessed_position = int(input("Can you guess where the goblin is?"))

    if guessed_position == goblin_position:
        print("You found the goblin!")
        keep_trying = False
    else:
        print("No, the goblin is still out there")