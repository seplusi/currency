from selenium.common.exceptions import NoSuchElementException
import time


class InsertValuesPage:
    def __init__(self, driver):
        self.driver = driver.instance

        self.verify_cookies_and_accept()
        self.verify_heading()

    def verify_heading(self):
        for _ in range(10):
            if self.driver.find_element_by_css_selector('div > h1[id="main-heading"]').text == 'XE Currency Converter':
                break
            time.sleep(0.1)
        else:
            print('Main page heading was not loaded')
            assert False

    def verify_cookies_and_accept(self):
        try:
            self.driver.implicitly_wait(5)
            verify_cookie = self.driver.find_element_by_css_selector('div[class="privacy-basic-body"]')
            verify_cookie.find_element_by_css_selector('div[class="privacy-button-container"] > button').click()
        except NoSuchElementException:
            print('No cookie. No need to accept')
        finally:
            self.driver.implicitly_wait(5)

    def insert_amount(self, amount):
        element = self.driver.find_element_by_css_selector('input[class^="Input-lwa9ow-0"]')
        element.send_keys(amount)

    def select_currencies(self, from_currency_name, to_currency_name):

        self.driver.find_element_by_xpath("//*[@id=\"from\"]").send_keys("%s\n" % from_currency_name)
        self.driver.find_element_by_xpath("//*[@id=\"to\"]").send_keys("%s\n" % to_currency_name)

    def perform_convertion(self):
        self.driver.find_element_by_css_selector('button[class^="Button-sc-1ikk70s-0 submitButton"]').click()
