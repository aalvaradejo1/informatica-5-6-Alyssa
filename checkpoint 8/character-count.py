def character_counter(message, dictionary):
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary[character] += 1

    print(dictionary)
    print(len(message))
    #print(sum(dictionary.values()))

    #Alternative 1

    values_list = list(dictionary.values())
    keys_lists = list(dictionary.keys())
    largest = max(values_list)
    print(f"The most repeted character is {keys_lists[largest]}, repated {dictionary[keys_lists[largest]]} times")

    #Alternitive 2

    largest_number_2 = max(dictionary, key=dictionary.get)
    print(f"The most repeted character is {largest_number_2}, repated {dictionary[largest_number_2]} times")
    

message = input("Write a message: ")
dictionary = {}
character_counter(message, dictionary)


