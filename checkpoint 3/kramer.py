while True:
    
        greeting = input("write a greeting:")

        if greeting.startswith("hello"):
                print("You get $0 dollars")
        elif greeting.startswith("h"):
                print("You get $20 dollars")
        else:
                print("You get $100 dollars")
                break

