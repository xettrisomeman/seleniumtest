import unittest
from selenium import webdriver


class TestSelenium(unittest.TestCase):

    def test_one(self):
        driver = webdriver.Firefox()
        driver.get("https://google.com")
        title = driver.title 
        driver.close()
        self.assertEqual(title , "Google")
        

