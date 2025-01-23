import random
import string

def generate_password(length):
    """Generate a random password of the specified length."""
    if length < 1:
        return "Password length must be at least 1."

    # Combine all possible characters (lowercase, uppercase, digits, and symbols)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        # Prompt the user to specify the desired password length
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password length must be at least 1.")
            return

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()