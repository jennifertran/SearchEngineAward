# Grabs html code from given url
# This solution does work but it is slow
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

#driver = webdriver.Chrome()
def passResult(faculty,type):
    driver = webdriver.PhantomJS()

    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")

    Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(faculty)
    Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text(type)

    driver.find_element_by_xpath("//*[@id='Search']").click()

    soup = BeautifulSoup(driver.page_source,"html5lib")

    result = ""

    for award in soup.find_all("div", {"id":"awardInfo"}):
        result = result + str(award) + '\n'

    return result

    #return result.find("form", {"name":"mailMessage"})





