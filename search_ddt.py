import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\lrchi\Desktop\Platzi\selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://demo.onestepcheckout.com/")

    @data(('dress', 4), ('music', 5))
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f"Found {len(products)} products")

        for product in products:
            print(product.text)
        
        self.assertEqual(expected_count, len(products))


  
    def tearDown(self):
        self.driver.implicitly_wait(4)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)