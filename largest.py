def main():
    list_length = int(input("Enter the length of the list: "))
    number_list = []
    
    for i in range(list_length):
        list_element = int(input("Enter element: "))
        number_list.append(list_element)
    print(number_list)

    file(number_list)

def file(number_list):
    with open("largest.txt", "w") as file:
        for line in file:
            file.write(f"{number_list}")

    


main()