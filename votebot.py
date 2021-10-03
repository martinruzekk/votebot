from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

driverPath = "/home/martin/dev/python/chromedriver"

driver = webdriver.Chrome(driverPath)

driver.get("https://martinruzek.eu")
fiala = driver.find_element_by_link_text("Petr Fiala")
fiala.click()

btn = driver.find_element_by_id("btn")
btn.click()
