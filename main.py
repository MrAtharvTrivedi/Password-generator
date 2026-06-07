import random
import string

while True:
    try:
        length = int(input("Enter the length of password: "))
        if length > 0:
            break
        print("Length must be greater than 0")
    except ValueError:
        print("Please enter a number")

num_c = input("Do you want to include numbers ? (y/n): ").lower()
capital_letters_c = input("Do you want to include capital letters ? (y/n): ").lower()
small_letters_c = input("Do you want to include small letters ? (y/n): ").lower()
special_char_c = input("Do you want to include special characters ? (y/n): ").lower()

characters = ""

if num_c == "y":
    characters += string.digits

if capital_letters_c == "y":
    characters += string.ascii_uppercase

if small_letters_c == "y":
    characters += string.ascii_lowercase

if special_char_c == "y":
    characters += string.punctuation

# Check if User Selected Nothing
if not characters:
    print("Please select at least one character type.")
    exit()

password = ""

for _ in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)
