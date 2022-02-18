import unittest
import time
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class HelloWorldGoogle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_go_to_google(cls):
        driver = cls.driver
        driver.get('https://www.google.com')
        
    def test_write_HelloWorld(cls):
        driver = cls.driver
        input_google = driver.find_element_by_name('q')
        input_google.clear()
        time.sleep(3)
        input_google.send_keys('HelloWorld in Google with Selenium')
        time.sleep(3)
        driver.save_screenshot('./img/screenshot.png')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output = 'reports', report_name='ReportHelloWorld'))
