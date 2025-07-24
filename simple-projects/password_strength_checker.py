import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digit = string.digits
symbols = string.punctuation

password = input('Enter the password:')
print("Tip: Use at least 8 characters, including uppercase, lowercase, numbers, and symbols.")

score = 0

if len(password) >= 8:
    score += 1

if any(char in lowercase for char in password):
    score += 1
if any(char in uppercase for char in password):
    score += 1
if any(char in digit for char in password):
    score += 1
if any(char in symbols for char in password):
    score += 1

if score == 5:
    print("Password Strength: Strong")
elif 3 <= score < 5:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")

