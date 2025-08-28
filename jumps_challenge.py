def main():
    number = int(input("enter limit number: "))
    step_size = int(input("Enter the step size you want: "))

    start = step_size
    
    while True:
        print(step_size)
        start += step_size
        print (start)
        
        if start == number:
            print(number)
        else:
            break

main() 
