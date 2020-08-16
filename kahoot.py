from urllib import *
import selenium
from selenium import webdriver
import time
from time import sleep
import string
import random
from selenium.webdriver.common.keys import Keys
y = 0
def kbot(kahootkey, name, count):
    while(y < count):
        driver = webdriver.Chrome("C:/Users/nsous/Downloads/chromedriver_win32 (1)/chromedriver.exe")
        driver.get('https://kahoot.it/')

        sleep(1)
        pass_box = driver.find_element_by_name('gameId')
        enter = driver.find_element_by_css_selector("button[class = 'enter-button__EnterButton-sc-1o9b9va-0 kxpxeu']")

        i = 0


        h = 0
        i += 1
        pass_box.send_keys(kahootkey)
        enter.click()
        sleep(0.7)
        name = driver.find_element_by_name('nickname')
        enter2 = driver.find_element_by_css_selector("button[class = 'enter-button__EnterButton-sc-1o9b9va-0 kxpxeu']")
        x = str(y)
        name.send_keys(name, x)
        enter2.click()
        y += 1
    
kbot()