def main():  # define the main function
    
    message = input("Write a message: ").lower()    # we ask the user for a message

    encode_message(message)    # we execute the function

def encode_message(text):       #definind the function that will encode the message
    alphabet = "abcdefghijklmnopqrstuvwxyz"   # created a variable to store all the letters from a to z
    cipher = "zyxwvutsrqponmlkjihgfedcba"   # created a variable to store all the letters from z to a
    new_message = ""   # that is the variable which will be printed at the end
    i = 0         # this is our counter

    while i < len(text): # inicialized the loop with our counter that will update every time the loop starts again until the condition is false
        char = text[i]  # we created a variable that stores the position 0( but will update every time) of the message the user put
        
        if char in alphabet:   # we created a condition which states that if the character that is in the position 0  is in the alphabet it will do the following
            cipher_index = alphabet.find(char) # in this variable will be stored the position that the letter of the massage takes in the alphabet
            new_message += cipher[cipher_index] # # here we updated the new message that will be printed to heve the character that is in the same position as in the alphabet but for the cipher variable so that it is encoded
        else: new_message += char              # here we stated that if any character that doesn't cualifies for the previous condition it will just be printed or added to the variable that will be printed at the end
        i += 1      # here we updated our counter so that it can do the same but for the rest of the letters of the message
    print(new_message)  # print the new message after every letter is encoded and added together

main() # we "closed" the main funtion, finished our code

