import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range (length))

print("Password Generator")
password_length = int(input("Enter password length: "))
include_digits = input("Include digits? (yes/no):  ").lower() == "yes"
include_special = input("Include special characters? (yes/no):  ").lower() == "yes"

password = generate_password(password_length, include_digits, include_special)

print(f"\nyour password is:  {password}")