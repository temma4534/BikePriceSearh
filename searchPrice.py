from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
#import chromedriver_binary


class SearchPri:
    def __init__(self, getName):
        self.getName = getName

    def high_search(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)

        driver.get('https://www.goobike.com/index.html')

        driver.implicitly_wait(10)

        search_name = driver.find_element_by_id('phrase_input')
        search_button = driver.find_element_by_id('searchAreaBtn')

        search_name.send_keys(self.getName)
        search_button.click()

        search_dropdown = driver.find_element_by_name('sortlist')
        search_select = Select(search_dropdown)
        search_select.select_by_visible_text('支払総額(高)')

        cur_url = driver.current_url

        return cur_url

        driver.close()
        driver.quit()


    def low_search(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)

        driver.get('https://www.goobike.com/index.html')

        driver.implicitly_wait(10)

        search_name = driver.find_element_by_id('phrase_input')
        search_button = driver.find_element_by_id('searchAreaBtn')

        search_name.send_keys(self.getName)
        search_button.click()

        search_dropdown = driver.find_element_by_name('sortlist')
        search_select = Select(search_dropdown)
        search_select.select_by_visible_text('支払総額(安)')

        cur_url = driver.current_url

        return cur_url

        driver.close()
        driver.quit()


    def all_search(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)

        driver.get('https://www.goobike.com/index.html')

        driver.implicitly_wait(10)

        search_name = driver.find_element_by_id('phrase_input')
        search_button = driver.find_element_by_id('searchAreaBtn')

        search_name.send_keys(self.getName)
        search_button.click()

        cur_url = driver.current_url

        return cur_url

        driver.close()
        driver.quit()
