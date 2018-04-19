#http://elementalselenium.com/tips/47-waiting
import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
class PythonTest(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        option.add_argument("- incognito")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    def test_wenxuecity(self):
        self.driver.get("http://www.wenxuecity.com")
        self.assertIn("文学城", self.driver.title)
        assert "No results found." not in self.driver.page_source
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()