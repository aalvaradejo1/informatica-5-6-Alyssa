def main():
    number = int(input("Enter an integer:"))

    if number != 2 and number % 2 != 0 and number % number == 0:
        print("Prime ")
    elif number != 3 and number % 3 != 0 and number % number == 0:
        print("Prime ")
    elif number != 4 and number % 4 != 0 and number % number == 0:
        print("Prime ")
    elif number != 5 and number % 5 != 0 and number % number == 0:
        print("Prime ")
    elif number != 6 and number % 6 != 0 and number % number == 0:
        print("Prime ")
    elif number != 7 and number % 7 != 0 and number % number == 0:
        print("Prime ")
    elif number != 8 and number % 8 != 0 and number % number == 0:
        print("Prime ")
    elif number != 9 and number % 9 != 0 and number % number == 0:
        print("Prime ")
    elif number != 10 and number % 10 != 0 and number % number == 0:
        print("Prime ")

    fizzbuzz(number)

def fizzbuzz(number):
    if number % 3 == 0:
        print("Frizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(f"{number}")

main()