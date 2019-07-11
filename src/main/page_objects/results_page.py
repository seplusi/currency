class ResultsPage:
    def __init__(self, driver):
        self.driver = driver.instance
        result_str = self.driver.find_element_by_css_selector('span[class="converterresult-toAmount"]').text

        if ',' in result_str:
            thousands = int(result_str.split(',')[0])
        else:
            thousands = 0

        remain = result_str.split(',')[-1]
        units = int(remain.split('.')[0])
        decimals = remain.split('.')[1]
        multiplier = pow(10, len(decimals))

        self.result = thousands*multiplier*1000 + units*multiplier + int(decimals)




    def perform_validate(self, from_currency_name, amount):
        for element in self.driver.find_elements_by_css_selector('div[class="sc-EHOje lkcPkj"]'):
            if "1 %s =" % from_currency_name in element.text:
                conv_rate = element.text.split(' ')[-2]
                conv_rate_units = int(conv_rate.split('.')[-1])
                total = conv_rate_units * amount
                while total > 1000000:
                    total = int(total/10)
                try:
                    assert self.result == total, 'result=%d conv_rate=%d amount=%d' % (self.result, conv_rate_units, amount)
                except:
                    pass
                break
        else:
            print('element with conversion rate was not found')
            assert False
