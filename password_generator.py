#RANDOM PASSWORD GENERATOR USING STRING MODULE

import string
from random import choice

#You dont need to convert to a list, it will still work
def generate_password(number):
    num = list(string.digits)
    char = list(string.ascii_lowercase)
    special_char = list(string.punctuation)


    charac = num + char + special_char
    pwd = []

    for num in range(number):
        chars = choice(charac)
        pwd.append(chars)
    password = ''.join(pwd)
    return password

pwd = generate_password(15)
print(pwd)