import time

import pytest
from main import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests



#______________________________Sanity Test 100%__________________________________________________
class TestSanity_UI:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    def test_sanity(self,driver):
        expected = 'https://www.saucedemo.com/'
        actual = open_site(driver,expected)
        assert expected == actual
#______________________________Login Test 100%____________________________________________________
class TestLogin_UI:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver
    @pytest.fixture()
    def url(self):
        return 'https://www.saucedemo.com/'

    def test_login(self,driver,url):
        expected = 'https://www.saucedemo.com/inventory.html'
        open_site(driver , url)
        actual = login(driver,'standard_user','secret_sauce')
        assert expected == actual
#________________________________Login_N Test 100%_________________________________________________
    @pytest.fixture()
    def url(self):
        return 'https://www.saucedemo.com/'

    def test_login_N(self,driver,url):
        expected = 'https://www.saucedemo.com/inventory.html'
        open_site(driver , url)
        actual = login_N(driver,'diaa' , '123')
        assert expected == actual
        print(driver.current_url)
#____________________________________________________________________________________________________








class TestApi:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    def test_sanity_API(self,driver):
        res = requests.get('https://reqres.in/api/users')
        assert res.status_code <400 and res.status_code >= 200
        print(f' The Status Code you received {res.status_code}')
