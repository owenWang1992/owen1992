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
        # options.add_argument("--window-size=1920x1080")
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        # self.driver.maximize_window()
        testUrl = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products-1.html?pc=dir_exp_0"
        self.driver.implicitly_wait(10)
        self.driver.get(testUrl)
        tlinks = self.driver.find_elements(By.CSS_SELECTOR, "a.btn")
        self.links = [link for link in tlinks if link.is_displayed()]
        self.urls = [x.get_attribute("href") for x in self.links]
        self.htmls = [x.get_attribute("innerText") for x in self.links]
        self.placements = []
        for url in self.urls:
            a = url.split('?')
            placement = dict(parse.parse_qsl(a[1]))
            placement["url"] = url
            self.placements.append(placement)
        for placement in self.placements:
            print(placement["url"])

    def testUrl(self):
        urlTable_A = [
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-XXXXXXX-XX-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-MQE-XXXXXXX-XX-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-MQE-XXXXXXX-XX-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-TBL-XXXXXXX-XX-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-TBL-XXXXXXX-XX-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-TBL-XXXXXXX-XX-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-XXXXXXX-XX-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-XXXXXXX-XX-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX"
        ]

        urlTable_B = [
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-MQE-RNSCOMP-B0-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-MQE-RNSCOMP-B0-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-TBL-RNSCOMP-B0-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-TBL-RNSCOMP-B0-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-TBL-RNSCOMP-B0-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-B0-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-B0-EXP-VMAC-DIR-XXXXXX-XXXXXX-XXXXX"
        ]
        is_Test_B = "-B0-" in self.placements[0]["url"]
        urlTable = urlTable_A
        if(is_Test_B):
            urlTable = urlTable_B
            print("B Test")
        else:
            print("A Test")
        for idx, placement in enumerate(self.placements):
            self.assertEqual(placement["url"], urlTable[idx])
            
    def tearDown(self):
        self.driver.close()
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
