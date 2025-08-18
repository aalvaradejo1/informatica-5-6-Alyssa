def main():
    faces = input("Write a message with an emoticon:")
    convert(faces)

def convert(message):
    message = message.replace(":(", "😞").replace(":)", "😊")
    print(message)

main()



