import unittest
from selenium import webdriver


class TestSelenium(unittest.TestCase):

    #test google title
    def test_title(self):
        driver = webdriver.Firefox()
        driver.get("https://google.com")
        title = driver.title 
        driver.close()
        self.assertEqual(title , "Google")
        
    #test faceboook h2 element text
    def test_h2_element(self):
        driver = webdriver.Firefox()
        driver.get("https://facebook.com")
        elem = driver.find_element_by_tag_name("h2").text
        driver.close()
        self.assertFalse(elem)


