dictionary = {
    "color" : "green",
    "age" : 17
}


#Values
print(dictionary.values())
for v in dictionary.values():
    print(v)

#Keys
print(dictionary.keys())
for k in dictionary.keys():
    print(k)

#items
print(dictionary.items())
for i in dictionary.items():
    print(i)


#print Key and Value using methods
# to do
i = 0
for k in dictionary:

    print(f"{dictionary.keys[i]} : {dictionary.value[i]}")
    # print(f"{k} : {dictionary[k]}")


#Get
print_items = {"apples": 5, "cups":2}
print(f"I'm bringging {print_items.get("cups")} cups.")
print(f"I'm bringging {print_items.get("eggs", 0)} eggs.")

#Setting default values
pet_info = {
    "name" : "Puka",
    "age" : 5
}

pet_info.setdefault("color", "black")
print(pet_info)
