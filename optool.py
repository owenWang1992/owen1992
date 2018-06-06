import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import ctalib
import time
import sys
'''
https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-GMAC-DIR-XXXXXX-XXXXXX-PHAS2
cta["offer"] = "at_fcras100"
cta["op_product"] = "FRCR"
cta["op_offer_number"] = "100"
cta["op_campaign"] = "RNSCOMP"
cta["op_placement"] = "MQE"
cta["op_recipe"] = "B0"
cta
'''

__unittest = True
class LandingPageTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        # options.add_argument("--window-size=1920x1080")
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
     
    def doTest(self):
        # test_url_A = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products-1.html?pc=dir_exp_0"
        # test_url_B = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products-cl.html?pc=dir_exp_0"
        # test_url = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products.html"
        test_url = "file:///C:/owen1992/optooltest.html"
        self.driver.get(test_url)
        print(self.driver.current_url)
        self.checkPage()
        planButtons = self.driver.find_elements(
            By.CSS_SELECTOR, "span.plan-btn")
        if planButtons:
            planButtons[1].click()
            time.sleep(3)
            self.checkPage()

    def testDesktop(self):
        print("\nTest Desktop")
        self.doTest()

    def testMobile(self):
        print("\nTest Mobile")
        time.sleep(5)
        self.driver.set_window_size(375, 812)
        self.doTest()

    def testTablet(self):
        print("\nTest Tablet")
        time.sleep(5)
        self.driver.set_window_size(900, 1366)
        self.doTest()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def checkPage(self):
        links = self.driver.find_elements(By.CSS_SELECTOR, "a")
        cta_list = ctalib.getCTAListFromLinks(links)
        for cta in cta_list:
            print("{:20s} {} {}".format(
                cta["title"], cta["url"], "\tH" if cta["hidden"] else ""))
        print("")
        errors = []
        hasError = False
        for cta in cta_list:
            errors.clear()
            print("")
            self.checkError(ctalib.checkMissingOp(cta), errors)
            if "op" in cta:
                self.checkError(ctalib.checkOpOffer(cta), errors)
                self.checkError(ctalib.checkCampaign(cta), errors)
                self.checkError(ctalib.checkRecipe(cta), errors)
            if len(errors):
                hasError = True
                print(cta["url"])
                for error in errors:
                    print(error)
        self.assertEqual(hasError, False, "Errors found!")
    
       
    def checkError(self, error, errors):
        if(error):
            errors.append(error)


if __name__ == '__main__':
    unittest.main()
