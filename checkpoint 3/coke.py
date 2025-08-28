def main():
    name = input("Enter your name: ")
    total = 50
    coin1 = int(input("The total is 50 cents, enter the first coin:"))


    while True:
        money = total - coin1
        print(f"you still lack {money}")
        
        next_coin = int(input("enter your next coin:"))
        if next_coin <= money:
            more_money = money - next_coin
            print(f"you still lack {more_money}")
        elif more_money == 0:
            print(f"Here is a coke for {name}")
        break



main()
