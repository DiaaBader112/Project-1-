
#
#
# driver = webdriver.Chrome()
# driver.get('http://google.com')
# time.sleep(3)
# search_box = driver.find_element(By.NAME , 'q')
# search_box.send_keys('pizza')
# time.sleep(3)
# search_button = driver.find_element(By.NAME, 'btnK')
# search_button.click()
# time.sleep(3)
# link = driver.find_element(By.XPATH , '//*[@id="rso"]/div[2]/div[2]/div/div[1]/div/a')
# link.click()
# time.sleep(3)
# driver = webdriver.Chrome()
# driver.get('http://google.com')
# time.sleep(3)
# driver.fullscreen_window()
# driver.get('https://linkedin.com')
# driver.back()
# driver.forward()
# driver.refresh()
# time.sleep(1)
#
# title = driver.title
# url = driver.current_url
# print(title)
# print(url)
#
#


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time


# driver = webdriver.Chrome()
# driver.get('http://google.com')
# time.sleep(3)
# search_box = driver.find_element(By.NAME , 'q')
# search_box.send_keys('pizza')
# time.sleep(3)
# search_button = driver.find_element(By.NAME, 'btnK')
# search_button.click()
# time.sleep(3)
# link = driver.find_element(By.CSS_SELECTOR, '//*[@id="rso"]/div[2]/div[2]/div/div[1]/div/a')
# link.click()
# time.sleep(3)



# from selenium import webdriver # chromedriver
# from selenium.webdriver.common.by import By # using method
# from selenium.webdriver.common.keys import Keys # import keys --
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome();
# driver.get('https://www.ebay.com/')
# driver.fullscreen_window()
# time.sleep(3)
# search = driver.find_element(By.CSS_SELECTOR , '#gh-ac')
# userinput = input('Enter what you search ? ')
# search.send_keys(userinput)
# searchbutton = driver.find_element(By.CSS_SELECTOR , '#gh-btn')
# searchbutton.click()
# time.sleep(3)
# price = driver.find_element(By.CSS_SELECTOR , '#srp-river-results > ul > li:nth-child(6) > div > div.s-item__info.clearfix > div.s-item__details.clearfix > div:nth-child(1) > span')
# print(price.text)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome()
# driver.get('https://demo.applitools.com/')
# time.sleep(3)
# inputname = driver.find_element(By.CSS_SELECTOR , '#username')
# inputname.send_keys('hoid123')
# time.sleep(3)
# inputpass = driver.find_element(By.CSS_SELECTOR , '#password')
# inputpass.send_keys('1234')
# time.sleep(3)
# signin = driver.find_element(By.CSS_SELECTOR , '#log-in')
# signin.click()
# time.sleep(5)
# price = driver.find_element(By.CSS_SELECTOR , 'body > div > div.layout-w > div.content-w > div > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(1) > td.text-right.bolder.nowrap > span')
# print(price.text)
# price2 = driver.find_element(By.CSS_SELECTOR , 'body > div > div.layout-w > div.content-w > div > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(2) > td.text-right.bolder.nowrap > span')
# print(price2.text)
# price3 = driver.find_element(By.CSS_SELECTOR , 'body > div > div.layout-w > div.content-w > div > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(1) > td.text-right.bolder.nowrap > span , body > div > div.layout-w > div.content-w > div > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(2) > td.text-right.bolder.nowrap > span')
# print(price2.text , price3.text , 'The prices')
# print(min( price2.text , price3.text) , 'The bigger price')
#

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common import keys
# import time
#

# driver = webdriver.Chrome(r'C:\Users\lenovo\Desktop\Diaa Files/chromedriver.exe')
# driver.get('https://demo.applitools.com/')
# admin =
# driver.close()

# driver = webdriver.Chrome()
# driver.get('https://demo.applitools.com/')
# time.sleep(3)
# inputname = driver.find_element(By.CSS_SELECTOR , '#username')
# inputname.send_keys('hoid123')
# time.sleep(3)
# inputpass = driver.find_element(By.CSS_SELECTOR , '#password')
# inputpass.send_keys('1234')
# time.sleep(3)
# signin = driver.find_element(By.CSS_SELECTOR , '#log-in')
# signin.click()
# time.sleep(3)
# balance = driver.find_element(By.CSS_SELECTOR , 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)')
# newbalance = driver.find_element(By.CSS_SELECTOR, 'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(2) > div.balance-value')
# time.sleep(2)
# balance = float(balance[1:])
# newbalance = float(newbalance[1:].replace (',',''))
# print(balance+newbalance)
#
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(r'C:\Users\lenovo\Desktop\Diaa Files\chromedriver.exe')
# url = ('http://www.fb.com')
# driver.get(url)
# time.sleep(3)
#
# if str(driver.current_url) == 'https://www.facebook.com/':
#     print('True page')
# else:
#     print('Wrong page')
#     time.sleep(2)
#
# print('True page')
# print("The current url is:" + str(driver.current_url))
# try:
#    signup = driver.find_element(By.CSS_SELECTOR, 'a._51sy')
#    signup.click()
# except :
#     print("Element does not exist")
#
# driver.close()
# signup = driver.find_element(By.CSS_SELECTOR , '#u_0_0_\+v')
# signup.click()

# driver = webdriver.Chrome(r'C:\Users\lenovo\Desktop\Diaa Files\chromedriver.exe')
# url = 'http://www.fb.com'
# driver.get(url)
# time.sleep(3)
# print(driver.current_url)
#
# if driver.current_url == url:
#     print('True')
# else:
#     print('Wrong')
# signup = driver.find_element(By.CSS_SELECTOR, ' a._51sy')
# signup.click()
# time.sleep(3)
# print(signup.text)
#
# firstname = driver.find_element(By.NAME , 'firstname')
# familyname = driver.find_element(By.NAME, 'lastname')
# email = driver.find_element(By.NAME , 'reg_email__')
# passw = driver.find_element(By.CSS_SELECTOR , '#password_step_input')
# reenteremail = driver.find_element(By.NAME , 'reg_email_confirmation__')
# date = driver.find_element(By.CSS_SELECTOR , '#day')
# birthdaymonth = driver.find_element(By.NAME , 'birthday_month')
# birthdayyer = driver.find_element(By.NAME , 'birthday_year')
# male = driver.find_element(By.NAME, 'sex')
# Signupp = driver.find_element(By.NAME , 'websubmit')
#
# time.sleep(2)
# firstname.send_keys('diaa1131')
# familyname.send_keys('baderbader')
# time.sleep(2)
# time.sleep(2)
# email.send_keys('diaabaderbader23@gmail.com')
# time.sleep(5)
# passw.send_keys('123456789d')
# time.sleep(4)
# reenteremail.send_keys('diaabaderbader23@gmail.com')
# time.sleep(4)
# date.click()
# time.sleep(4)
# date.send_keys(20)
# time.sleep(2)
# date.click()
# time.sleep(3)
# birthdaymonth.click()
# birthdaymonth.send_keys('April')
# time.sleep(2)
# birthdaymonth.click()
# time.sleep(2)
# birthdayyer.click()
# birthdayyer.send_keys('2001')
# time.sleep(2)
# male.click()
# time.sleep(4)
# Signupp.click()
# time.sleep(2)
# print(signup.text)
#
#
# driver.close()
#
#
#


# def withdraw(amount):
#     if amount % 100 != 0 and amount < 4000:
#         return True
#     else:
#         re

# def check_password(password):
#     if len(password) > 8 and password[0] == password[0].upper() and not password.isalpha() :
#         return True
#     else:
#         return False

#def check_password(password):
   # if len(password) > 8 and password[0] == password[0].upper() and not password.isalpha():
        #return True
    #else:
        #return False


# print(check_password('Hothaifagfhjnhbg')) #F
# print(check_password('Hothaifa12344')) # T
# print(check_password('othaifagf123123')) #F
# print(check_password('fagfasfasg')) #F
# print(check_password('H2134567854')) #T


#def withdraw(amount):
   # if amount % 100 == 0 and amount < 4000:
      #  return True
    #else:
      #  return False

# N  4000 4100 - P 3900
# N- 330   N - 5050

#def deposit(amount):
   # if 0 < amount <= 10000:
      #  return True
   # else:
    #    return False

#print(withdraw(1000))
#print(withdraw(150))

# from selenium import webdriver # chromedriver
# from selenium.webdriver.common.by import By # using method
# from selenium.webdriver.common.keys import Keys # import keys --
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# driver = webdriver.Chrome();
# driver.get('https://www.ebay.com/')
# driver.fullscreen_window()
# time.sleep(3)
# search = driver.find_element(By.CSS_SELECTOR , '#gh-ac')
# userinput = input('Enter what you search ? ')
# search.send_keys(userinput)
# searchbutton = driver.find_element(By.CSS_SELECTOR , '#gh-btn')
# searchbutton.click()
# time.sleep(3)
# price = driver.find_element(By.CSS_SELECTOR , '#srp-river-results > ul > li:nth-child(6) > div > div.s-item__info.clearfix > div.s-item__details.clearfix > div:nth-child(1) > span')
# print(price.text)
