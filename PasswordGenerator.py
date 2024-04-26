import random
import string

class PasswordGenerator:
    """Class for generating strong and random passwords."""

    def __init__(self):
        pass

    def generate_password(self, length=12, complexity="medium"):
        """Generate a random password of specified length and complexity."""
        if complexity == "low":
            characters = string.ascii_letters + string.digits
        elif complexity == "medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "high":
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
        else:
            raise ValueError("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def main():
    """Main function to interact with the Password Generator."""
    print("Welcome to the Password Generator!")
    password_generator = PasswordGenerator()
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid length.")

    while True:
        complexity = input("Choose complexity level ('low', 'medium', or 'high'): ").lower()
        if complexity not in ['low', 'medium', 'high']:
            print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
        else:
            break

    password = password_generator.generate_password(length, complexity)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
