'''
from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://bpm.alqueria.com.co")#bpm.alqueria.com.co
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.set_capability("acceptInsecureCerts", True)
#options.add_argument('--allow-running-insecure-content')
#options.add_argument('--ignore-certificate-errors')
desired_capabilities = DesiredCapabilities.CHROME.copy()
desired_capabilities['acceptInsecureCerts'] = True

chrome_driver_path = './chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, desired_capabilities=desired_capabilities)
url = "https://www.google.com"
driver.get(url)
print(driver.title)
#article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a" )
#print (article_count.text)
driver.close()