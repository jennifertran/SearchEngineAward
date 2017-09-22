# Grabs html code from given url
# This solution does work but it is slow
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

#driver = webdriver.Chrome()
def passResult():
    driver = webdriver.PhantomJS()

    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")

    Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text("Faculty of Science")
    Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text("Scholarship")

    driver.find_element_by_xpath("//*[@id='Search']").click()

    result = BeautifulSoup(driver.page_source)

    return result