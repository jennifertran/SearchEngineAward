# Grabs html code from given url
# This solution does work but it is slow
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from Award import Award

def passResult(faculty,type):
    driver = webdriver.PhantomJS()
    result = []

    # Get the original page
    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")

    # Inital Selection
    Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(faculty)
    Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text(type)
    Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")

    driver.find_element_by_xpath("//*[@id='Search']").click()

    result += extractAwards(driver)

    # If there is a next link, click on it
    try:
        while driver.find_element_by_link_text("Next"):
            driver.find_element_by_link_text("Next").click()
            result += extractAwards(driver)

    except NoSuchElementException:
        return result

def extractAwards(currPage):
    soup = BeautifulSoup(currPage.page_source, "html5lib")


    awards = []
    type = soup.find(id="award").text.split( )

    for award in soup.find_all("div", {"id": "awardInfo"}):
        url = "https://wwwapps.cc.umanitoba.ca:8443"+award.find('a').get('href')
        name = award.find('a').text
        spanList = award.find_all(id="rightTag")
        #for span in spanList: print span.text
        award = Award(url,spanList[0].text,name,type[3],spanList[1].text,spanList[2].text,None,None,None,award.find(id="awardDesc").text.strip())
        awards.append(award)

    return awards



# For Debugging purposes only

# def passResult():
#     driver = webdriver.PhantomJS()
#     result = ""
#
#     # Get the original page
#     driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")
#
#     # Inital Selection
#     Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text("Faculty of Science")
#     Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text("Scholarship")
#     Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")
#
#     driver.find_element_by_xpath("//*[@id='Search']").click()
#
#     result += extractAwards(driver)
#
#     # If there is a next link, click on it
#     try:
#         while driver.find_element_by_link_text("Next"):
#             driver.find_element_by_link_text("Next").click()
#             result += extractAwards(driver)
#
#     except NoSuchElementException:
#         print result
#
# def extractAwards(currPage):
#     soup = BeautifulSoup(currPage.page_source, "html5lib")
#
#     data = ""
#
#     for award in soup.find_all("div", {"id": "awardInfo"}):
#         data += award.text + "AND"
#
#     return data





