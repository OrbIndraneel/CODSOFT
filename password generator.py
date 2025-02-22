#password generator
import random as r
import string as st

def password_generator(length):
    characters = st.ascii_letters + st.digits + st.punctuation
    password = ''.join(r.choice(characters) for i in range(length))
    return password

a=int(input("Enter the length of your password: "))
print(f"your password is {password_generator(a)}.")
