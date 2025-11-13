import random
import string
from selenium import webdriver


class WebdriverFactory: 
    @staticmethod 
    def get_webdriver(browser_name): 

        if browser_name == "firefox": 
            return webdriver.Firefox() 
        elif browser_name == "chrome": 
            return webdriver.Chrome()
        else:
            raise ValueError
        
        
def generate_random_credentials(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
   

def new_user_credentials():
    username = generate_random_credentials(10)
    return {
        "email": f"{username}@yandex.ru",
        "password": generate_random_credentials(10),
        "name": username
    }

