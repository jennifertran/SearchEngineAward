# Grabs html code from given url
# This solution does work but it is slow
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from Award import Award

counter = 0

def passResult(faculty, type, keyword):
    driver = webdriver.PhantomJS()
    result = []
    typeList = ["Athletic Award", "Bursary", "Combined Medal and Prize", "Fellowship", "Medal", "Prize", "Scholarship",
                "Undergraduate Research Award"]

    # Get the original page

    for currFaculty in faculty:
        for currType in type:
            # Max Rady College of Medicine is an exception, it has sub-branches
            if currFaculty == "Max Rady College of Medicine":
                if currType == "View all types":
                    # Athletic Award
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=ATHL+AWARD&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=ATHL+AWARD&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=BURS&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=BURS&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=COMB&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=COMB&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=FELLOW&disabled=&faculty=05&awardsPerPage=10&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=FELLOW&disabled=&faculty=05&awardsPerPage=10&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=MEDAL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=MEDAL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=PRIZE&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=PRIZE&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=SCHOL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=SCHOL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=RESEARCH&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=RESEARCH&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == "Entrance Bursary":
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=ENTRANCE&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=BURS&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=ENTRANCE&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=BURS&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == "Entrance Scholarship":

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=ENTRANCE&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=SCHOL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=ENTRANCE&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=SCHOL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == typeList[0]:
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=ATHL+AWARD&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=ATHL+AWARD&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == typeList[1]:
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=BURS&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=BURS&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == typeList[2]:
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=COMB&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=COMB&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == typeList[3]:
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=FELLOW&disabled=&faculty=05&awardsPerPage=10&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=FELLOW&disabled=&faculty=05&awardsPerPage=10&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == typeList[4]:
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=MEDAL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=MEDAL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == typeList[5]:
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=PRIZE&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=PRIZE&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == typeList[6]:
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=SCHOL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=SCHOL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == typeList[7]:
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=RESEARCH&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=RESEARCH&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

            else:
                if currType == "View all types":
                    for y in typeList:
                        driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")
                        Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(currFaculty)
                        Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text(y)
                        Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")
                        driver.find_element_by_xpath("//*[@id='Search']").click()
                        result += extractAwards(driver, keyword)  # result on the first page
                        try:
                            while driver.find_element_by_link_text("Next"):
                                driver.find_element_by_link_text("Next").click()
                                result += extractAwards(driver, keyword)
                        except NoSuchElementException:
                            pass

                    # Add "Entrance Bursary"
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")
                    Select(driver.find_element_by_xpath("//*[@id='level']")).select_by_visible_text("Entrance")
                    Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(currFaculty)
                    Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text("Bursary")
                    Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")
                    driver.find_element_by_xpath("//*[@id='Search']").click()
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                    # Add "Entrance Scholarship"
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")
                    Select(driver.find_element_by_xpath("//*[@id='level']")).select_by_visible_text("Entrance")
                    Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(currFaculty)
                    Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text("Scholarship")
                    Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")
                    driver.find_element_by_xpath("//*[@id='Search']").click()
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        return result

                elif currType == "Entrance Bursary":
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")
                    Select(driver.find_element_by_xpath("//*[@id='level']")).select_by_visible_text("Entrance")
                    Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(currFaculty)
                    Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text("Bursary")
                    Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")
                    driver.find_element_by_xpath("//*[@id='Search']").click()
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                elif currType == "Entrance Scholarship":
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")
                    Select(driver.find_element_by_xpath("//*[@id='level']")).select_by_visible_text("Entrance")
                    Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(currFaculty)
                    Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text("Scholarship")
                    Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")
                    driver.find_element_by_xpath("//*[@id='Search']").click()
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

                else:
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")
                    Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(currFaculty)
                    Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text(currType)
                    Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")
                    driver.find_element_by_xpath("//*[@id='Search']").click()
                    result += extractAwards(driver, keyword)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword)
                    except NoSuchElementException:
                        pass

    return result


def extractAwards(currPage, keyword):
    soup = BeautifulSoup(currPage.page_source, "html5lib")

    awards = []
    result = []  # Contains keyword related result
    keywords = []  # Collection of keyword
    global counter
    global isCleared

    type = soup.find(id="award").text.split()

    for award in soup.find_all("div", {"id": "awardInfo"}):
        url = "https://wwwapps.cc.umanitoba.ca:8443" + award.find('a').get('href')
        name = award.find('a').text
        spanList = award.find_all(id="rightTag")
        if keyword == "":
            counter += 1
        award = Award(url, spanList[0].text, name, type[3], spanList[1].text, spanList[2].text, None, None, None,
                      award.find(id="awardDesc").text.strip()[:-1][1:], counter)
        awards.append(award)


    if keyword:
        # try to split string based on logical conjunction
        # if find logical conjunction AND

        if keyword.find("AND") != -1:
            keywords = keyword.split("AND")
            for award in awards:
                isFound = True
                awardInfo = str(award.displayAward())
                for currKeyword in keywords:
                    if awardInfo.find(currKeyword.strip()) == -1:
                        isFound = False
                if (isFound == True):
                    counter += 1
                    award.sequence = counter
                    result.append(award)
            return result
        # if find logical conjunction OR
        elif keyword.find("OR") != -1:
            keywords = keyword.split("OR")
            for award in awards:
                awardInfo = str(award.displayAward())
                for currKeyword in keywords:
                    if awardInfo.find(currKeyword.strip()) != -1:
                        counter += 1
                        award.sequence = counter
                        result.append(award)
                        break
            return result
        # no logic conjunction is found, only single keyword
        else:
            for award in awards:
                awardInfo = str(award.displayAward())
                if awardInfo.find(keyword) != -1:
                    counter += 1
                    award.sequence = counter
                    result.append(award)
            return result
    else:
        return awards

def getTotal():
    global counter
    temp = counter # Pass counter value to temp
    counter = 0 # Clear counter after each query
    return temp