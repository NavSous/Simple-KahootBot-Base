from urllib import *
import time
from time import sleep
import string
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


def kbot(kahootkey, name, count):
    y = 0
    while(y < count):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://kahoot.it/')
        sleep(4)
        pass_box = driver.find_element_by_name('gameId')
        enter = driver.find_element_by_css_selector("button[class = 'enter-button__EnterButton-sc-1o9b9va-0 gSoXKU']")
        i = 0
        h = 0
        i += 1
        pass_box.send_keys(kahootkey)
        enter.click()
        sleep(6)
        name = driver.find_element_by_name('nickname')
        x = str(y)
        b = f"{name}{x}"
        enter2 = driver.find_element_by_css_selector("button[class = 'enter-button__EnterButton-sc-1o9b9va-0 gSoXKU']")
        name.send_keys(b)
        enter2.click()
        y += 1
   
