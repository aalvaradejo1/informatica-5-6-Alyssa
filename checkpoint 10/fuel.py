def main():
    percentage("Enter the fraction of how much fuel you have left: ")
    

def percentage(promt):
    while True:
        try:
            fraction = input(promt).split("/")
            num = int(fraction[0])
            den = int(fraction[1])
            percent = round(num / den * 100)
        
            if 1 < percent < 99:
                print(f"You have {percent} % of fuel left")
                break
            elif percent <= 1:
                percent = "E"
                print(f"Tank: {percent}")
                break
            elif 101 > percent >= 99:
                percent = "F"
                print(f"Tank: {percent}")
                break
            elif num > den:
                print("Invalid, try again")
                pass
        except (ValueError, IndexError, ZeroDivisionError):
            print("Invalid, try again")
            pass
main()
