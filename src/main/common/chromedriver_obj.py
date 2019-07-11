from selenium import webdriver


class Driver:

    def __init__(self, chromedriver_path):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-popup-blocking");
        options.add_experimental_option('w3c', False)
        options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})

        self.instance = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.instance.implicitly_wait(30)

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")
