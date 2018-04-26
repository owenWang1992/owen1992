import unittest
from urllib import parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
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
        self.mobile = False

    def getPlacementsFromPage(self):
        time.sleep(5)
        tlinks = self.driver.find_elements(By.CSS_SELECTOR, "#main a.btn")
        links = [link for link in tlinks if link.is_displayed()]
        placements = []
        for link in links:
            url = link.get_attribute("href")
            a = url.split('?')
            placement = dict(parse.parse_qsl(a[1]))
            placement["url"] = url
            placement["title"] = link.get_attribute("innerText")
            placements.append(placement)
        return placements

    def check(self, placements, version):
        url_table = self.mapping_table(version)
        if self.mobile:
            url_table = [x.replace("VWIN", "TWIN") for x in url_table]
        
        for idx, placement in enumerate(placements):
            self.assertEqual(placement["url"], url_table[idx])

    def mapping_table(self, version):
        urlTable ={"A" : [
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-MQE-RNSCOMP-A0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-A0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-A0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-A0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX"
        ], "B" : [
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX"
        ], "B_Annual" : [
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwa104&br=exp&op=WPAC-PRD-PCO-104-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpa106&br=exp&op=W3AC-PRD-PCO-106-MQE-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwa104&br=exp&op=WPAC-PRD-PCO-104-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpa106&br=exp&op=W3AC-PRD-PCO-106-TBL-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-B0-EXP-VWIN-DIR-XXXXXX-XXXXXX-XXXXX"
        ]}

        urlTable_mobile ={"A" : [
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-MQE-RNSCOMP-A0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-A0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-A0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-A0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX"
        ], "B" : [
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-MQE-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-MQE-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-TBL-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwb105&br=exp&op=WPMC-PRD-PCO-105-TBL-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpd102&br=exp&op=W3DC-PRD-PCO-102-TBL-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX"
        ], "B_Annual" : [
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-MQE-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwa104&br=exp&op=WPAC-PRD-PCO-104-MQE-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpa106&br=exp&op=W3AC-PRD-PCO-106-MQE-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_fcras100&br=exp&op=FRCR-PRD-PCO-100-TBL-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwa104&br=exp&op=WPAC-PRD-PCO-104-TBL-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_eiwpa106&br=exp&op=W3AC-PRD-PCO-106-TBL-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_1b1s109&br=exp&op=1B1S-PRD-PCO-109-SEC-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX",
            "https://usa.experian.com/#/registration?offer=at_3b3s110&br=exp&op=3B3S-PRD-PCO-110-SEC-RNSCOMP-B0-EXP-TWIN-DIR-XXXXXX-XXXXXX-XXXXX"
        ]}

        return urlTable_mobile[version] if self.mobile else urlTable[version]

    def checkAB(self):
        placements = self.getPlacementsFromPage()
        for placement in placements:
            print(placement["title"], placement["url"])
        print("")
        if "-B0-" in placements[0]["url"]:
            self.check(placements, "B")
        else:
            self.check(placements, "A")

        planButtons = self.driver.find_elements(
            By.CSS_SELECTOR, "span.plan-btn")
        if planButtons:
            planButtons[1].click()
            time.sleep(3)
            placements = self.getPlacementsFromPage()
            self.check(placements, "B_Annual")

    def testDesktop(self):        
        testUrl = "http://www.experian.com"
        self.driver.get(testUrl)
        reportScoreElement = self.driver.find_element(By.CSS_SELECTOR,"ul.left-main-nav.main-nav.flex-nav > li:nth-child(1) > a")
        hover = ActionChains(self.driver).move_to_element(reportScoreElement)
        hover.perform()
        compareAllProductsElement = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-shadow > li:nth-child(6) > a")
        compareAllProductsElement.click()
        self.mobile = False
        self.checkAB()

    def testMobile(self):
        self.driver.set_window_size(375, 812)
        testUrl = "http://www.experian.com"
        self.driver.get(testUrl)
        barElement =self.driver.find_element(By.CSS_SELECTOR,".nav-toggle")
        barElement.click()
        reportScoreElement = self.driver.find_element(By.CSS_SELECTOR,"ul.left-main-nav.main-nav.flex-nav > li:nth-child(1) > span")
        reportScoreElement.click()
        compareAllProductsElement = self.driver.find_element(By.CSS_SELECTOR, "ul.left-main-nav.main-nav.flex-nav > li:nth-child(1) > ul > div > li:nth-child(6) > a")
        self.driver.get(compareAllProductsElement.get_attribute("href"))
        #compareAllProductsElement.click()
        self.mobile = True
        self.checkAB()
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
