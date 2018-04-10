from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
option = webdriver.ChromeOptions()
option.add_argument("- incognito")
browser = webdriver.Chrome()
browser.get("https://github.com/TheDancerCodes")
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")
titles = [x.text for x in titles_element]
print('titles: ')
print(titles, '\n')
language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
languages = [x.text for x in language_element]
print("languages:")
print(languages, '\n')
for title, language in zip (titles, languages):
    print("RepoName : Language")
    print(title + ":" + language, '\n')