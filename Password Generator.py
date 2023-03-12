import random
import string

def generate_password(length=8, strength='weak'):
    # Define the character sets to use
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Choose the character set based on the requested strength
    if strength == 'weak':
        char_set = lowercase + uppercase
    elif strength == 'strong':
        char_set = lowercase + uppercase + digits + symbols

    # Generate the password
    password = ''.join(random.choice(char_set) for i in range(length))

    return password

# Get input from the user
length = int(input("Enter the password length: "))
strength = input("Enter the password strength (weak/strong): ")

# Generate the password
password = generate_password(length, strength)
print("Your password is:", password)
