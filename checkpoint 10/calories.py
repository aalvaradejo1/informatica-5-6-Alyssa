def main():
    food_dictionary = {
        "milk" : 73, "almond milk" : 30, "yougurt" : 77, "sour cream" : 16, "egg" : 75, "egg whites" : 16, "watermelon" : 11, "banana" : 33, "orange" : 21, "avocados" : 48
    }
    print(food_dictionary)
    two_foods = input("Type the name of two foods from above(separate them with commas): ").split(",")
    calories(two_foods, food_dictionary)
    

def calories(food, food_dictionary):
    
    a = food[0]
    b = food[1]
    total_calories = 0
    while True:
        try:
            if a in food_dictionary and b in food_dictionary:
                total_calories += food_dictionary[a]
                total_calories += food_dictionary[b]
                print(f"Calories: {total_calories}")
                break
            elif (a == food_dictionary[0] or food_dictionary[6]) and b == food_dictionary[0] or food_dictionary[6]:
                raise ValueError("You CANNOT mix watermelon and milk")
        except (ValueError, IndexError, ZeroDivisionError):
            print("Invalid, try again")
        
        print(total_calories)





main()