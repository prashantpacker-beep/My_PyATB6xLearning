from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
try:
    driver=webdriver.Chrome()
    driver.get("http://example.com")
    driver.find_element("id","No Exit button")
except NoSuchElementException as nse:
    print("Element not found!",nse.msg)