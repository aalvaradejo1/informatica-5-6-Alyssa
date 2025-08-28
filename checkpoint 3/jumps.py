number = int(input("enter a number: "))

start = 2
while True:
    print(start)
    start += 2
    if start == number:
        print(number)
        break 
