def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    symbol = input("Enter the symbol for the operation you want to use(+,-,*)")
    
    operation(symbol, a, b)
        
def operation(n, a, b):
    if n == "+":
        print(f"{a} + {b} = {a + b}")
    if n == "-":
        print(f"{a} - {b} = {a-b}")
    if n == "*":
        print(f"{a} * {b} = {a*b}")

main()