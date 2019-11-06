import unittest
from selenium import webdriver


# class TestSelenium(unittest.TestCase):

#     #test google title
#     def test_title(self):
#         driver = webdriver.Firefox()
#         driver.get("https://google.com")
#         title = driver.title 
#         driver.close()
#         self.assertEqual(title , "Google")
        
#     #test faceboook h2 element text
#     def test_h2_element(self):
#         driver = webdriver.Firefox()
#         driver.get("https://facebook.com")
#         elem = driver.find_element_by_tag_name("h2").text
#         driver.close()
#         self.assertFalse(elem)



class TestSelenium(unittest.TestCase):

    #this will run at the start of each test
    def setUp(self):
        self.driver  = webdriver.Firefox()
        self.get = self.driver.get("https://google.com")

    #test title of google
    def test_title(self):
        homepage_text = self.driver.title
        self.assertEqual(homepage_text , "Google")


    #this will end the process
    def tearDown(self):
        return driver.close()

