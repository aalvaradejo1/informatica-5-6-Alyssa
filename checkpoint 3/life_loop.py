def main():
    name = input("Enter your name: ")
    print(f"Hello {name}")
    read = input("Have your read your scriptures today? ")
    loop(read, name)
    

def loop(read, name):
    while True:
        if read == "yes":
            print(f"Good job {name}, share something that you learned with your family")
        elif read == "no":
            print(f"{name} what are you waiting for, go read")
        break

          
            



main()
