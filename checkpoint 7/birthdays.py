birthdays = {
    "Gabriel" : "27 Dic 2007",
    "Hyrum" : "14 Feb 2008",
    "Joseph" : "14 Feb 2008"
}


name = input("Enter a name: ")
if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    new_name = name
    print(f"Idon't have any birthday information for {new_name}")
    date = input("Enter the birthday of the new name: ")
    birthdays[new_name] = (date)
    print(f"{name}'s birthday is {birthdays[new_name]}")
    print("Birthday database updated")
