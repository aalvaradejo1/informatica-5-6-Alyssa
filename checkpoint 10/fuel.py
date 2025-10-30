def main():
    fuel_left = input("Enter the fraction of how much fuel you have left: ").split("/")
    percentage(fuel_left)

def percentage(fuel_left):
    # print(fuel_left)
    num = int(fuel_left[0])
    den = int(fuel_left[1])
    
    percent = round(num / den * 100)
    
    if 1 < percent < 99:
        print(f"You hvae {percent} % of fuel left")

main()
