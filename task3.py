import random
import string

length = int(input("Enter password length: "))

print("Choose password complexity:")
print("1. Letters only")
print("2. Letters and numbers")
print("3. Letters, numbers, and symbols")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    chars = string.ascii_letters
elif choice == "2":
    chars = string.ascii_letters + string.digits
elif choice == "3":
    chars = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice")
    exit()

password = ''.join(random.choice(chars) for _ in range(length))
print("Generated Password:", password)
