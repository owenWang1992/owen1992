import unittest
from urllib import parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
'''
Grab all op links and print out.

Assert offer and op match each other based on a opTable dictionary.
Assert no unrecognized offer and op pair
Assert Campain field is not "XXXX"
Test passed if all assert pass, otherwise failed.

if new offer and op pairs are found, print out so that they can be copied and added to opTable

'''

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
        self.mobile = False
        self.opTable = {
            'at_fcras100': 'FRCR-PRD-PCO-100', 
            'at_eiwpd102': 'W3DC-PRD-PCO-102', 
            'at_eiwa104': 'WPAC-PRD-PCO-104', 
            'at_eiwb105': 'WPMC-PRD-PCO-105', 
            'at_eiwpa106': 'W3AC-PRD-PCO-106', 
            'at_1b1s109': '1B1S-PRD-PCO-109', 
            'at_3b3s110': '3B3S-PRD-PCO-110'
            }
        
    def getPlacementsFromPage(self):
        time.sleep(5)
        links = self.driver.find_elements(By.CSS_SELECTOR, "#main a.btn")
        placements = []
        for link in links:
            url = link.get_attribute("href")
            a = url.split('?')
            placement = dict(parse.parse_qsl(a[1]))
            placement["url"] = url
            placement["title"] = link.get_attribute("innerText")
            placement["hidden"] = False if link.is_displayed() else True
            if placement["op"]:
                opComponents = placement["op"].split("-")
                placement["op_offer"] = "-".join(opComponents[0:4])
                placement["op_postion"] = "-".join(opComponents[4:5])
                placement["op_campaing"] = "-".join(opComponents[5:6])
                placement["op_AB"] = "-".join(opComponents[6:7])
                placement["op_source"] = "-".join(opComponents[7:8])
                placement["op_platform"] = "-".join(opComponents[8:9])      
            placements.append(placement)
        return placements


    def checkNewOffer(self, placements):
        newOffer = {}
        for placement in placements:
            if placement["offer"] not in self.opTable:
                newOffer[placement["offer"]] = placement["op_offer"]
        if newOffer:
            print("***find new offers, please add them to opTable in the code.")
            print(newOffer)

    def checkPage(self):
        placements = self.getPlacementsFromPage()
        for placement in placements:
            print("{:20s} {} {}".format(placement["title"], placement["url"], "\tH" if placement["hidden"] else ""))
        print("")
        self.checkNewOffer(placements)  
        for placement in placements:
            self.assertEqual(self.opTable[placement["offer"]], placement["op_offer"])
            self.assertNotEqual(placement["op_campaing"], "XXXX")        

    
    def doTest(self):        
        startUrl = "https://www.experian.com"
        testUrl_A = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products-1.html?pc=dir_exp_0"
        testUrl_B = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products-cl.html?pc=dir_exp_0"
        testUrl = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products.html"
        #self.driver.get(startUrl)
        self.driver.get(testUrl)
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
        self.driver.set_window_size(375, 812)
        self.doTest()
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
