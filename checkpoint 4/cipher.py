def main():
    
    message = input("Write a message: ").lower()

    encode_message(message)

def encode_message(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    new_message = ""
    i = 0

    while i < len(message):
        if message[0] == alphabet[0]:
            print(cipher[0])
            i += 1
        if message[1] == alphabet[1]:
            print(cipher[1])
            i += 1
        if message[2] == alphabet[2]:
            print(cipher[2])
        if message[3] == alphabet[3]:
            print(cipher[3])
        if message[4] == alphabet[4]:
            print(cipher[4])
        if message[5] == alphabet[5]:
            print(cipher[5])
        if message[6] == alphabet[6]:
            print(cipher[6])
        if message[7] == alphabet[7]:
            print(cipher[8])
        if message[9] == alphabet[9]:
            print(cipher[9])
        if message[10] == alphabet[10]:
            print(cipher[10])
        if message[11] == alphabet[11]:
            print(cipher[11])
        if message[12] == alphabet[12]:
            print(cipher[12])
        if message[13] == alphabet[13]:
            print(cipher[13])
        if message[14] == alphabet[14]:
            print(cipher[14])
        if message[15] == alphabet[15]:
            print(cipher[15])
        if message[16] == alphabet[16]:
            print(cipher[16])
        if message[17] == alphabet[17]:
            print(cipher[17])


main()

