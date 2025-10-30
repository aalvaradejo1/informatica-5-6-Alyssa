def main():
    x = int(input("Type a positive integer: "))
    print(f"{x}! = {factorial_calculator(x)}")

def factorial_calculator(n):
    if n <= 0:
        raise ValueError(f"The inpit was negative or zero: {n}")
    else:
        new_n = 1
        for i in range(2, new_n + 1):
            new_n = new_n * i
            return new_n
        
main()
