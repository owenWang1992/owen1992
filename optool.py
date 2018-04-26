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
Navigation to target page
Grab all op links in page and print out.
Assert offer and op match each other based on a op_table dictionary.
Assert no unrecognized offer and op pairs
Assert Campaign field is not "XXXX"
Test passed if all assert pass, otherwise failed.

if new offer and op pairs are found, print out so that they can be copied and added to op_table

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
        self.op_table = {
            'at_fcras100': 'FRCR-PRD-PCO-100',
            'at_eiwpd102': 'W3DC-PRD-PCO-102',
            'at_eiwa104': 'WPAC-PRD-PCO-104',
            'at_eiwb105': 'WPMC-PRD-PCO-105',
            'at_eiwpa106': 'W3AC-PRD-PCO-106',
            'at_1b1s109': '1B1S-PRD-PCO-109',
            'at_3b3s110': '3B3S-PRD-PCO-110'
        }

    def doTest(self):
        # test_url_A = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products-1.html?pc=dir_exp_0"
        # test_url_B = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products-cl.html?pc=dir_exp_0"
        test_url = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products.html"
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
        self.driver.set_window_size(375, 812)
        self.doTest()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def parseOpLink(self, link):
        url = link.get_attribute("href")
        op_data = {}
        if url and "?" in url:
            a = url.split('?')
            op_data = dict(parse.parse_qsl(a[1]))
            if ("offer" in op_data) and ("op" in op_data):
                op_data["url"] = url
                op_data["title"] = link.get_attribute("innerText")
                op_data["hidden"] = False if link.is_displayed() else True
                if op_data["op"]:
                    opComponents = op_data["op"].split("-")
                    op_data["op_offer"] = "-".join(opComponents[0:4])
                    op_data["op_postion"] = "-".join(opComponents[4:5])
                    op_data["op_campaign"] = "-".join(opComponents[5:6])
                    op_data["op_AB"] = "-".join(opComponents[6:7])
                    op_data["op_source"] = "-".join(opComponents[7:8])
                    op_data["op_platform"] = "-".join(opComponents[8:9])
                    return op_data
        return {}

    def getOpDataListFromPage(self):
        time.sleep(5)
        links = self.driver.find_elements(By.CSS_SELECTOR, "a")
        op_data_list = []
        for link in links:
            op_data = self.parseOpLink(link)
            if op_data:
                op_data_list.append(op_data)
        return op_data_list

    def checkNewOffer(self, op_data_list):
        new_offer = {}
        for op_data in op_data_list:
            if op_data["offer"] not in self.op_table:
                new_offer[op_data["offer"]] = op_data["op_offer"]
        if new_offer:
            print("***find new offers, please add them to op_table in the code.")
            print(new_offer)

    def checkPage(self):
        op_data_list = self.getOpDataListFromPage()
        for op_data in op_data_list:
            print("{:20s} {} {}".format(
                op_data["title"], op_data["url"], "\tH" if op_data["hidden"] else ""))
        print("")
        self.checkNewOffer(op_data_list)
        for op_data in op_data_list:
            self.assertEqual(
                self.op_table[op_data["offer"]], op_data["op_offer"])
            self.assertNotEqual(op_data["op_campaign"], "XXXX")


if __name__ == '__main__':
    unittest.main()
