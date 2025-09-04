def main():
    number = int(input("Enter a positive integer number: "))

    multi(number)

def multi(num): 
    m = 1

    while m <= 10:
        if num > 0:
            
            table = num * m
            print(f"{num} x {m} = {table}")
            m += 1
            
        else:
            print("try again with an integer number")
            break

main()  