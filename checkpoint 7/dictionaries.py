capitals = {
    "Mexico" : "Mexico City",
    "Canada" : "Ottawa",
    "Brazil" : "Brasilia"
}

capitals["Italy"] = "Rome"    #Add a new key and value
del capitals["Brazil"]         # Delete a key and value
capitals.pop("Canada")    # Another method to delete a key and value
capitals.clear()         # Delete the whole dictionary

# houses = {
#     "Hermione" : "Griffindor",
#     "Harry" : "Griffindor",
#     "Ron" : "Griffindor",
#     "Draco" : "Slytherin"
# }

# for students in houses:
#     print(f"{students}: {houses[students]}")


students = [
    {"name" : "Hermione", "house" : "Griffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Griffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Griffindor", "patronus" : "Jack Russell terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
]

for element in students:
    print(f"{element["name"]}, {element["house"]}, {element["patronus"]}")