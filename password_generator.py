import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
    # Define character sets based on complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ""
    special_chars = string.punctuation if include_special_chars else ""

    # Combine character sets based on complexity
    characters = lowercase_letters + uppercase_letters + digits + special_chars

    if len(characters) == 0:
        return "Complexity is too low. Please include at least one character set."

    # Generate the password
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the password length: "))
            include_digits = input("Include digits? (y/n): ").strip().lower() == "y"
            include_special_chars = input("Include special characters? (y/n): ").strip().lower() == "y"

            password = generate_password(length, include_digits, include_special_chars)
            print(f"Generated Password: {password}")
        except ValueError:
            print("Invalid input. Please enter a valid password length (a positive integer).")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
