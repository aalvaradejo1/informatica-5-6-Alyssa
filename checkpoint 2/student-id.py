def main():
	print('')
	print('Please enter the following information to create your ID Card.')
	input('Press enter to continue.')
	


	name = input("Enter your first name: ")
	lastname = input("Enter your last name: ")
	email = input("Enter your email adress: ")
	phone = input("Enter your phone number: ")
	id = input("Enter student id: ")
	fpt = input("Enter your formacion para el trabajo class:")
	graduation = input("Enter your expected graduation year:")
	extra = ("Enter yes or no if you are in an extracurricular: ")
	
	

	print("Your ID card is:")
	print("-" * 45)
	print(f"{lastname.upper()}, {name.capitalize()}")
	print(f"ID: {id}")
	print(" ")
	print(f"{email}")
	print(f"{phone}") luego le sigo

main()