import string
import random

def generate_password(length):
    charectors = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    password = "".join(random.choice(charectors) for _ in range(length))
    return password

length = int(input('Enter the length of the password:'))
password = generate_password(length)
print(f'Password:{password}')