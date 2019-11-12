from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

altToken = 'item's image alt token'
size = 'item size (ex. s, m, 9.5, etc.)'
cardNumber = 'your card number'
ccMonth = 'your ccMonth'
ccYear = 'your ccYear'
ccv = 'your ccv'
currentHour = datetime.now().hour
currentMin = datetime.now().minute
itemLocator = 0

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:\supremeChrome\chromedriver.exe"
browser = webdriver.Chrome(chrome_driver, options=chrome_options)
browser.get('https://www.supremenewyork.com/shop/new')


while currentHour < 10 or currentMin < 59:
    time.sleep(30)
    currentHour = datetime.now().hour
    currentMin = datetime.now().minute

while itemLocator == 0:
    browser.get('https://www.supremenewyork.com/shop/new')
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'nav-categories')))
    try:
        itemLocator = str(browser.find_element_by_xpath("//img[@alt='" + altToken + "']"))
    except:
        print("refreshing")

start = time.time()

browser.get('https://www.supremenewyork.com/shop/new')
browser.find_element_by_xpath("//img[@alt='" + altToken + "']").click()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, 'commit')))
try:
    browser.find_element_by_id('s').send_keys(size)
except:
    print('no size')
browser.find_element_by_name('commit').click()
browser.find_element_by_xpath("//*[contains(text(), 'checkout now')]").click()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'cnb'))).send_keys(cardNumber)
browser.find_element_by_id('credit_card_month').send_keys(ccMonth)
browser.find_element_by_id('credit_card_year').send_keys(ccYear)
browser.find_element_by_name('credit_card[vvv]').send_keys(ccv)
browser.find_element_by_xpath("//*[contains(text(), 'I have read and agree to the ')]").click()
browser.find_element_by_name('commit').click()

end = time.time()
print('checkout time:', end - start, 'seconds')
