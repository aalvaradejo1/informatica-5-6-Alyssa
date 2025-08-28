def main():
    price = 50
    total_paid = 0
    name = input("Enter your name: ")
    loop(price, total_paid, name)
    
    
    

def loop(price, total_paid, name):
    while price > 0:
        print(f"Amount due: {price}")
        pay = int(input("Insert coin:"))

        if pay == 25 or pay == 10 or pay == 5:
            price = price - pay
            total_paid = total_paid + pay
        else:
            print("Not a coin.")
    
    if total_paid >= 50:
        print(f"Thanks! Here's your coke🥤, {name}.")
        print("  .!.!.")
        print("   ! !   ")
        print("   ; :   ")
        print("  ;   :  ")
        print(" ;_____: ")
        print(" ! Coke! ")
        print(" !_____!")
        print(" :     : ")
        print(" :     ; ")
        print(" .'   '. ")
        print(" :     : ")
        print("  '''''")
        print(f"Here's your change {total_paid - 50}")

main()

