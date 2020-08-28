import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # return super().setUp()
        cls.driver = webdriver.Chrome(executable_path = r'C:\Users\lrchi\Desktop\Platzi\selenium\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        self.driver.get('https://www.platzi.com')

    def test_vist_wikipedia(self):
        driver = cls.driver
        driver.get('https://www.wikipedia.org')
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # return super().tearDown()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world'))
