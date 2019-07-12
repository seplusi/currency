from src.main.common import utils

class ResultsPage:
    """
        Page object that represents the page with the conversion result
    """
    def __init__(self, driver):
        self.driver = driver.instance
        result_str = self.driver.find_element_by_css_selector('span[class="converterresult-toAmount"]').text

        # Get rid of floats as they can have a precision problem. Work with integers instead
        self.result = utils.convert_string_float_into_integer(result_str)

    def perform_validate(self, from_currency_name, amount):
        """
            Reads the used conversion from the web page and calculates to result. Then compares it with the result in
            the web page

        :param from_currency_name: String with the original currency
        :param amount: Integer with theconverted amount
        :return: None
        """
        # Get the conversion rate from web page
        for element in self.driver.find_elements_by_css_selector('div[class="sc-EHOje lkcPkj"]'):
            if "1 %s =" % from_currency_name in element.text:

                # Make conversion rate integer and multiply with amount
                conv_rate = element.text.split(' ')[-2]
                conv_rate_units = int(conv_rate.split('.')[-1])
                total = conv_rate_units * amount
                while total > 1000000:
                    total = round(total/10)

                # Make sure conversion is OK
                assert self.result == total, 'result=%d conv_rate=%d amount=%d total=%d' % (self.result, conv_rate_units, amount, total)
                break
        else:
            print('element with conversion rate was not found')
            assert False
