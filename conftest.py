import pytest
import requests
from urls import *
from helpers import *


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = WebdriverFactory.get_webdriver(request.param)
    driver.get(main_page_url)
    yield driver
    driver.quit()

@pytest.fixture
def create_user():
    payload = new_user_credentials()
    response = requests.post(f'{main_page_url}api/auth/register', json=payload)
    return {
        "response" : response,
        "email": payload["email"],
        "password": payload["password"]
    }

@pytest.fixture
def delete_user():
    
    def _delete(access_token):
        headers = {"Authorization": access_token}
        response = requests.delete(f'{main_page_url}api/auth/user', headers=headers)
        return response
    return _delete
