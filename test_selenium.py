from main import *
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSanity:
    def test_sanity(self):
        driver = webdriver.Chrome()
        expected = 'https://www.saucedemo.com/'
        actual = open_site(driver,expected)
        assert expected == actual

    def test_login(self):
        driver = webdriver.Chrome()
        expected = 'https://www.saucedemo.com/inventory.html'
        open_site(driver,'https://www.saucedemo.com/')
        actual = login(driver,'standard_user','secret_sauce')
        assert actual == expected
        print(driver.current_url)

    def test_login_N(self):
        driver = webdriver.Chrome()
        expected = 'https://www.saucedemo.com/inventory.html'
        open_site(driver,'https://www.saucedemo.com/')
        actual = login(driver,'diaa','123')
        assert actual == expected
        print(driver.current_url)

    def test_checkout(self):
        driver = webdriver.Chrome()
        open_site(driver, 'https://www.saucedemo.com/')
        expected = 'https://www.saucedemo.com/checkout-complete.html'
        actual = 'https://www.saucedemo.com/cart.html'
        assert expected == actual