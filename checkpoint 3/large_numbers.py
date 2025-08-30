def main():
    n1 = int(input("Number 1:"))
    n2 = int(input("Number 2:"))
    n3 = int(input("Number 3:"))
    n4 = int(input("Number 4:"))

    if n1 > n2 and n1 > n3 and n1 > n4:
        greater = n1
    elif n2 > n3 and n2 > n4:
        greater = n2
    elif n3 > n4:
        greater = n3
    else: 
        greater = n4
    print(f"greater number is {greater}")
main()