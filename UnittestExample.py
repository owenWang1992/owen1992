import unittest
from urllib import parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

class LandingPageTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("- incognito")
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        testUrl = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products-1.html?pc=dir_exp_0"
        self.driver.implicitly_wait(10)
        self.driver.get(testUrl)
        tlinks = self.driver.find_elements(By.CSS_SELECTOR, "a.btn")
        self.links= [link for link in tlinks if link.is_displayed()]
        self.urls = [x.get_attribute("href") for x in self.links]
        self.htmls = [x.get_attribute("innerText") for x in self.links]
        
        print("\n". join (self.htmls))
        for url in self.urls:
            a = url.split('?')
            parameters = a[1].split("&")
            print(parameters)

    def testUrl(self):
        self.assertEqual(self.htmls[0], "Get your free report")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()                 