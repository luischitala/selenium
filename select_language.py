import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\lrchi\Desktop\Platzi\selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("https://demo.onestepcheckout.com/sales/guest/form/")

    def test_select_order_by(self):
        exp_options = ['Email Address', 'ZIP Code']
        act_options = []

        select_order_by = Select(self.driver.find_element_by_name('oar_type'))
        self.assertEqual(2, len(select_order_by.options))

        for op in select_order_by.options:
            act_options.append(op.text)

        self.assertListEqual(exp_options, act_options)

        self.assertEqual('Email Address',
                          select_order_by.first_selected_option.text
                        )

        select_order_by.select_by_visible_text('ZIP Code')
        self.driver.implicitly_wait(10)

    # def test_select_language(self):
    #     exp_options = ['English', 'German', 'French']
    #     act_options = []

    #     select_language = Select(self.driver.find_element_vy_id('select-language'))

    #     self.assertEqual(3, len(select_language.options))

    #     for option in select_language.options:
    #         act_options.append(option.text)

    #     self.assertListEqual(exp_options, act_options)

    #     self.assertEqual('English', select_language.first_selected_option.text)

    #     select_language.select_by_visible_text('German')

    #     self.assertTrue('store=german' in self.driver.current_url)

    #     select_language = Select(self.driver.find_element_by_id('select-language'))

    #     select_language.select_by_index(0)


  

    def tearDown(self):
        self.driver.implicitly_wait(4)
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)