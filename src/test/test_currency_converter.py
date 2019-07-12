import unittest
from ddt import ddt, data
from src.main.common.chromedriver_obj import Driver
from src.main.page_objects.insert_values_page import InsertValuesPage
from src.main.page_objects.results_page import ResultsPage

chromedriver_path = '/home/luis/Programs/chromedriver/chromedriver'


@ddt
class TestCurrencyConverter(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver(chromedriver_path)

    def setUp(self):
        self.driver.navigate("https://www.xe.com/currencyconverter/")
        self.insert_data_page = InsertValuesPage(self.driver)

    @data(11111, 1, 2, 333, 234, 543, 9, 12345, 2345, 9876)
    def test_convert_euro_2_pounds(self, amount):
        self.insert_data_page.insert_amount(amount)
        self.insert_data_page.select_currencies('EUR', 'GBP')
        self.insert_data_page.perform_convertion()
        ResultsPage(self.driver).perform_validate('EUR', amount)

    def test_convert_euro_cents_2_pounds(self):
        amount = 0.1
        self.insert_data_page.insert_amount(amount)
        self.insert_data_page.select_currencies('EUR', 'GBP')
        self.insert_data_page.perform_convertion()
        ResultsPage(self.driver).perform_validate('EUR', amount)

    def test_convert_euro_cents_2_pounds(self):
        amount = 0.2
        self.insert_data_page.insert_amount(amount)
        self.insert_data_page.select_currencies('EUR', 'GBP')
        self.insert_data_page.perform_convertion()
        ResultsPage(self.driver).perform_validate('EUR', amount)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.instance.quit()

if __name__ == "__main__":
    unittest.main()
