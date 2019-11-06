
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time 
import os



driver = webdriver.Firefox()
driver.get("https://facebook.com")
driver.maximize_window()
driver.implicitly_wait(5)
driver.save_screenshot("Facebook.png")
driver.close()




