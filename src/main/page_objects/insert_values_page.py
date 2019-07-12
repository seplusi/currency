from selenium.common.exceptions import NoSuchElementException
import time


class InsertValuesPage:
    """
        Class that represents the web page where currency data is inserted before clicking in the conversion button
    """
    def __init__(self, driver):
        self.driver = driver.instance

        # Sometimes the web page has cookies.
        self.verify_cookies_and_accept()

        # Verify heading
        self.verify_heading()

    def verify_heading(self):
        """
            Verify heading so we're sure the page was fully loaded and we haven't picked up some other selector

        :return: None
        """
        for _ in range(10):
            if self.driver.find_element_by_css_selector('div > h1[id="main-heading"]').text == 'XE Currency Converter':
                break
            time.sleep(0.1)
        else:
            print('Main page heading was not loaded')
            assert False

    def verify_cookies_and_accept(self):
        """
            Accepts cookies if they exist
        :return: None
        """
        try:
            self.driver.implicitly_wait(5)
            verify_cookie = self.driver.find_element_by_css_selector('div[class="privacy-basic-body"]')
            verify_cookie.find_element_by_css_selector('div[class="privacy-button-container"] > button').click()
        except NoSuchElementException:
            print('No cookie. No need to accept')
        finally:
            self.driver.implicitly_wait(5)

    def insert_amount(self, amount):
        """
            Inserts the numeric values in the amount text box
        :param amount: Integer with amount to convert
        :return: None
        """
        element = self.driver.find_element_by_css_selector('input[class^="Input-lwa9ow-0"]')
        element.send_keys(amount)

    def select_currencies(self, from_currency_name, to_currency_name):
        """
            Inserts from currency and to currency
        :param from_currency_name: String with from currency name
        :param to_currency_name: String with to cirrency name
        :return: None
        """
        self.driver.find_element_by_xpath("//*[@id=\"from\"]").send_keys("%s\n" % from_currency_name)
        self.driver.find_element_by_xpath("//*[@id=\"to\"]").send_keys("%s\n" % to_currency_name)

    def perform_convertion(self):
        """
            Clicks in the convert icon
        :return: None
        """
        self.driver.find_element_by_css_selector('button[class^="Button-sc-1ikk70s-0 submitButton"]').click()
