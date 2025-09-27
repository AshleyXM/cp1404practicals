MINIMUM_PASSWORD_LENGTH = 4

password = input("Enter a password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
	print("Invalid password")
	password = input("Enter a password: ")

print(len(password) * '*')