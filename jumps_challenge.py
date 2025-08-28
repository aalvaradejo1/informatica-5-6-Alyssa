def main():
    number = int(input("enter limit number: "))
    step_size = int(input("Enter the step size you want: "))

    start = 1
    while True:
        print(step_size)
        start += step_size
        print (start)
        if start == number:
            print(number)
            break

main() 
