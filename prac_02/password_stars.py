MINIMUM_PASSWORD_LENGTH = 4

def main():
	password = get_password()
	print_asterisks(password)


def print_asterisks(password):
	print(len(password) * '*')


def get_password():
	password = input("Enter a password: ")
	while len(password) < MINIMUM_PASSWORD_LENGTH:
		print("Invalid password")
		password = input("Enter a password: ")
	return password


main()