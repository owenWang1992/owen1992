from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import os


def openGmail():
    options = webdriver.ChromeOptions()
    #options.add_argument("--incognito")
    #options.add_argument('--ignore-certificate-errors')
    #options.add_argument('--ignore-ssl-errors')
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://accounts.google.com/signin")
    emailElement = driver.find_element_by_xpath("//input[@id='identifierId']")
    emailElement.send_keys("sihaowang4test@gmail.com")
    driver.find_element_by_id("identifierNext").click()
    wait = WebDriverWait(driver, 20)
    passwordElement = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
    passwordElement.send_keys("sihaowang419")
    driver.find_element_by_id("passwordNext").click()
    time.sleep(5)
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(5)


    


if __name__ == '__main__':
    openGmail()
