def main():
    food_dictionary = {
        "Milk" : 73, "Almond milk" : 30, "Yougurt" : 77, "Sour cream" : 16, "Egg" : 75, "Egg whites" : 16, "Watermelon" : 11, "Banana" : 33, "Orange" : 21, "Avocados" : 48
    }
    print(food_dictionary)
    food = input("Type the name of two foods from above(separate them with commas): ").split("/")
    calories(food)

def calories(food):
    a = food[0]
    b = food[1]

main()