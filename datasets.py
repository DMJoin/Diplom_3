import string
import random


def generate_random_credentials(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
   

def new_user_credentials():
    username = generate_random_credentials(10)
    return {
        "email": f"{username}@yandex.ru",
        "password": generate_random_credentials(10),
        "name": username
    }