import unittest
from google_page import GooglePage
from selenium import webdriver


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'C:\Users\lrchi\Desktop\Platzi\selenium\chromedriver.exe')
        

    def test_search(self):
        google = GooglePage(self.driver)
        # Realiza todas las acciones
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)
    


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)