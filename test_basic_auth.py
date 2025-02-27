"Test for https://the-internet.herokuapp.com/basic_auth"
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



CRED = dict(admin='admin', wrong42= '422')


class TestBasicAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_basic_auth_corect_credentials(self):
        "visit URL, get screenshot"
        user = "admin"
        password = CRED["admin"]
        self.url = f"https://{user}:{password}@the-internet.herokuapp.com/basic_auth"
        driver = self.driver
        res = driver.get(self.url)
        print(dir(res))
        self.assertIn('The Internet', driver.title)      
        bauth = driver.find_element(By.CSS_SELECTOR, "#content > div > h3")
        content = driver.find_element(By.ID, "content")
        driver.save_screenshot("test.png")
        self.assertIn('Basic Auth', content.text)
        self.assertIn('Basic Auth', bauth.text)
       
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
