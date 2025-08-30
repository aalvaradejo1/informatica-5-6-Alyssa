def main():
    number = int(input("Enter an integer:"))
    fizzbuzz(number)

def fizzbuzz(number):
    if number % 3 == 0:
        print("Frizz")
    elif number % 5 == 0:
        print("Buzz")
    
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(f"{number}")

main()