def main():
    password = input("Set a password: ")
    input("Press enter to log in")
    check_password(password)
    print("The program has ended")


def check_password(password):
    guess = input("Guess the password: ")

    if guess == password:
        print("You have guessed the password!")
    if guess != password:
        print("The password is incorrect:(")

    
        

    

main()