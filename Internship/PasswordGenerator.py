import string
import secrets

symbols = ['*', '%', '£'] # Can add more

password = ""
for _ in range(9):
    password += secrets.choice(string.ascii_lowercase)
password += secrets.choice(string.ascii_uppercase)
password += secrets.choice(string.digits)
password += secrets.choice(symbols)
print(password)