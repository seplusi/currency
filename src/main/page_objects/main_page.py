from selenium.common.exceptions import NoSuchElementException


class MainPage:
    def __init__(self, driver):
        self.driver = driver.instance

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

    def perform_convertion_and_validate(self, from_currency_name, amount):
        self.driver.find_element_by_css_selector('button[class^="Button-sc-1ikk70s-0 submitButton"]').click()

        result = float(self.driver.find_element_by_css_selector('span[class="converterresult-toAmount"]').text)

        for element in self.driver.find_elements_by_css_selector('div[class="sc-EHOje lkcPkj"]'):
            if "1 %s =" % from_currency_name in element.text:
                conv_rate = float(element.text.split(' ')[-2])
                assert result == conv_rate * amount, 'result=%s conv_rate=%s amount=%s' % (str(result), str(conv_rate), amount)
                break
        else:
            print('element with conversion rate was not found')
            assert False



