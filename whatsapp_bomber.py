from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\aravi\\AppData\\Local\\Google\\Chrome\\User Data")

driver = webdriver.Chrome(options=options)

driver.get("https://web.whatsapp.com")

inp_xpath_search = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]"
contact = input("Enter contact name \n")
text = input("Enter message \n")
n = input("Enter no. of times \n")
input_box_search = WebDriverWait(driver,100).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(1)
input_box_search.send_keys(contact +  Keys.ENTER)
time.sleep(2)
inp_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
for i in range(n):
    input_box.send_keys(text + Keys.ENTER)

time.sleep(2)
driver.quit()