import unittest
from src.main.common.chromedriver_obj import Driver
from src.main.page_objects.main_page import MainPage


chromedriver_path = '/home/luis/Programs/chromedriver/chromedriver'

class TestCurrencyConverter(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver(chromedriver_path)

    def setUp(self):
        self.driver.navigate("https://www.xe.com/currencyconverter/")
        self.main_page = MainPage(self.driver)
        self.main_page.verify_cookies_and_accept()

    def test_convert_euro_2_pounds(self):
        self.main_page.insert_amount(10)
        self.main_page.select_currencies('EUR', 'GBP')
        self.main_page.perform_convertion_and_validate('EUR', 10)
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()

if __name__ == "__main__":
    unittest.main()
