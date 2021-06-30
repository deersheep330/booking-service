from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class VirtualParser():

    def __init__(self):

        self.wait_timeout = 10
        self.click_retry_timeout = 3

        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_setting_values.notifications': 2}
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('window-size=1920,1200')
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

        self.url = ''
        self.elements = {}

    def _is_exist(self, target):
        try:
            self.driver.find_element_by_xpath(self.elements[target])
        except NoSuchElementException:
            return False
        return True

    def _wait_for(self, target):
        try:
            WebDriverWait(self.driver, self.wait_timeout).until(
                expected_conditions.presence_of_element_located((By.XPATH, self.elements[target]))
            )
            return True
        except Exception as e:
            print(f'wait for {target} error: {e}')
            return False

    def _click(self, target):
        self.driver.find_element_by_xpath(self.elements[target]).click()

    def _click_and_wait(self, target, expected):
        success = False
        retry = 0
        max_retry = 10
        while success is not True and retry < max_retry:
            try:
                _target = self.driver.find_element_by_xpath(self.elements[target])
                _target.click()
                WebDriverWait(self.driver, self.click_retry_timeout).until(
                    expected_conditions.presence_of_element_located((By.XPATH, self.elements[expected]))
                )
                success = True
            except ElementClickInterceptedException as e:
                raise e
            except Exception as e:
                print(f'[retry {retry}] try to click {target} and wait for {expected} failed ... {repr(e)} {e}')
            retry += 1

    def _send_keys(self, target, keys):
        _target = self.driver.find_element_by_xpath(self.elements[target])
        _target.send_keys(keys)

    def is_full(self):
        if self.url == '':
            raise RuntimeError('url should be provided!')
        print(f'==> parse page: {self.url}')
