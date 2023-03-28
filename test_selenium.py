import time

import pytest
from main import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests



#______________________________Sanity Test 100%_________________________________________________________________________
class Tests_Selenium:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    def test_sanity(self,driver):
        expected = 'https://www.saucedemo.com/'
        actual = open_site(driver,expected)
        assert expected == actual
#______________________________Login Test 100%__________________________________________________________________________
#
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
#________________________________Login_N Test 100%______________________________________________________________________
    @pytest.fixture()
    def url(self):
        return 'https://www.saucedemo.com/'

    def test_login_N(self,driver,url):
        open_site(driver , url)
        actual = login_N(driver, 'diaa', '123')
        expected = False
        assert expected == False
        print(driver.current_url)
#___________________________________Images Test 100%___________________________________________________________________
    def test_images(self,driver,url):
        expected = True
        open_site(driver,url)
        login(driver,'standard_user','secret_sauce')
        actual = Imagescheck(driver)
        assert expected == actual
#______________________________________Prices Test 100%_________________________________________________________________
    def test_Prices(self,driver,url):
        expected = True
        open_site(driver,url)
        # assert  True
        login(driver,'standard_user' , 'secret_sauce')
        actual = PriceSortTest(driver)
        assert actual == expected




#_______________________________________________________________________________________________________________________

#_____________________________Api (Sanity_tests) Tests 100%_____________________________________________________________________________

class Tests_Api:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    def test_sanity_API1(self,driver):
        res = requests.get('https://reqres.in/api/users')
        open_site(driver,'https://reqres.in/api/users')
        assert res.status_code <400 and res.status_code >= 200
        print(f' The Status Code you received {res.status_code}')


    def test_sanity_API2(self,driver):
        res = requests.get('https://reqres.in/api/users/3')
        open_site(driver,'https://reqres.in/api/users/3')
        assert res.status_code <400 and res.status_code >= 200
        print(f'The Status Code you received {res.status_code}' )
