import unittest
from urllib import parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


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

    def getPlacementsFromPage(self):
        time.sleep(5)
        tlinks = self.driver.find_elements(By.CSS_SELECTOR, "#main a.btn")
        links = [link for link in tlinks if link.is_displayed()]
        urls = [x.get_attribute("href") for x in links]
        # htmls = [x.get_attribute("innerText") for x in links]
        placements = []
        for url in urls:
            a = url.split('?')
            placement = dict(parse.parse_qsl(a[1]))
            placement["url"] = url
            placements.append(placement)
        return placements

    def checkA(self, placements):
        urlTable = [
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-MQE-RNSCOMP-A0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-A0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-A0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-A0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX"
        ]

        for idx, placement in enumerate(placements):
            self.assertEqual(placement["url"], urlTable[idx])

    def checkB(self, placements):
        urlTable = [
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX"
        ]
        for idx, placement in enumerate(placements):
            self.assertEqual(placement["url"], urlTable[idx])

    def checkBAnnual(self, placements):
        urlTable = [
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwa104&br=exp&op=WPAC-PRD-PCO-104-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpa106&br=exp&op=W3AC-PRD-PCO-106-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwa104&br=exp&op=WPAC-PRD-PCO-104-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpa106&br=exp&op=W3AC-PRD-PCO-106-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX"
        ]
        for placement in placements:
            print(placement["url"])

        for idx, placement in enumerate(placements):
            self.assertEqual(placement["url"], urlTable[idx])

    def testAB(self):
        testUrl = "https://www.experian.com/consumer-products/compare-credit-report-and-score-products.html"
        self.driver.get(testUrl)
        placements = self.getPlacementsFromPage()
        planButtons = self.driver.find_elements(
            By.CSS_SELECTOR, "span.plan-btn")
        self.checkAB(placements)
        if planButtons:
            planButtons[1].click()
            time.sleep(3)
            placements = self.getPlacementsFromPage()
            self.checkBAnnual(placements)

    def checkAB(self, placements):
        for placement in placements:
            print(placement["url"])
        print("")
        if "-B0-" in placements[0]["url"]:
            self.checkB(placements)
        else:
            self.checkA(placements)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
