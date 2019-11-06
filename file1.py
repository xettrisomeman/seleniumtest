
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time 
import os



driver = webdriver.Firefox()
driver.get("https://facebook.com")
driver.maximize_window() #maximize the window
driver.implicitly_wait(5) #wait for 5 seconds and try again
driver.save_screenshot("Facebook.png") #save screenshot
driver.close() #close the window




