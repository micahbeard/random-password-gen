"""
Password generator: Create a script that will create a random password of a user specified length
"""
import secrets
import string
#import random

print("Welcome to my Password Generator!")
length = input('Enter the length of password: ')



lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
alphabet = lower + upper + num + symbols
pwd = ''

if length.isdigit():
    for i in range(int(length)):
        pwd += ''.join(secrets.choice(alphabet))
    print(pwd)

else:
    print("----Error----")

