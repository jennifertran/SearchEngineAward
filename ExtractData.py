# Grabs html code from given url
# This solution does work but it is slow
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from Award import Award

counter = 0

def passResult(faculty,type,keyword):
    driver = webdriver.PhantomJS()
    result = []
    #facultyList = ["View all faculties", "Faculty of Agricultural & Food Sciences", "School of Agriculture", "Faculty of Architecture", "School of Art", "Faculty of Arts", "I.H. Asper School of Business", "School of Dental Hygiene", "College of Dentistry", "Faculty of Education", "Faculty of Engineering", "Faculty of Environment, Earth, & Resources", "Extended Education", "Faculty of Graduate Studies", "Faculty of Human Ecology", "Faculty of Kinesiology & Recreation Management", "Faculty of Law", "Max Rady College of Medicine", "Desautels Faculty of Music", "College of Nursing", "College of Pharmacy", "College of Rehabilitation Sciences", "Faculty of Science", "Faculty of Social Work", "University 1", "English Language Centre", "Post-Graduate Medical Education", "Not specific to faculties/colleges/schools", "International College of Manitoba", "Brandon University", "College universitaire de Saint-Boniface", "St. Andrew's College", "St. John's College", "St. Paul's College", "University of Winnipeg", "Western College of Veterinary Medicine"]
    typeList = ["Athletic Award", "Bursary", "Combined Medal and Prize", "Fellowship", "Medal", "Prize", "Scholarship", "Undergraduate Research Award"]

    # Get the original page


    for currFaculty in faculty:
        for currType in type:
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

                if currType == "Entrance Bursary":
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

                if currType == "Entrance Scholarship":
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

            if (currType != "Entrance Bursary") and (currType != "Entrance Scholarship") and (currType != "View all types"):
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

            if currType == "Entrance Bursary":
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

            if currType == "Entrance Scholarship":
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

    return result

def extractAwards(currPage,keyword):
    soup = BeautifulSoup(currPage.page_source, "html5lib")

    awards = []
    result = []  # Contains keyword related result
    keywords = [] # Collection of keyword


    type = soup.find(id="award").text.split( )

    for award in soup.find_all("div", {"id": "awardInfo"}):
        url = "https://wwwapps.cc.umanitoba.ca:8443"+award.find('a').get('href')
        name = award.find('a').text
        spanList = award.find_all(id="rightTag")
        global counter
        counter += 1
        award = Award(url, spanList[0].text, name, type[3], spanList[1].text, spanList[2].text, None, None, None,award.find(id="awardDesc").text.strip()[:-1][1:], counter)
        awards.append(award)



    if keyword:
        # try to split string based on logical conjunction
        # if find logical conjunction AND
        if keyword.find("AND")!=-1:
            keywords = keyword.split("AND")
            for award in awards:
                isFound = True
                awardInfo = str(award.displayAward())
                for currKeyword in keywords:
                    if awardInfo.find(currKeyword.strip())==-1:
                        isFound = False
                if(isFound == True):
                    result.append(award)
            return result
        #if find logical conjunction OR
        elif keyword.find("OR")!=-1:
            keywords = keyword.split("OR")
            for award in awards:
                awardInfo = str(award.displayAward())
                for currKeyword in keywords:
                    if awardInfo.find(currKeyword.strip())!=-1:
                        result.append(award)
            return result
        # no logic conjunction is found, only single keyword
        else:
            for award in awards:
                awardInfo = str(award.displayAward())
                if awardInfo.find(keyword) != -1:
                    result.append(award)
            return result
    else:
        return awards

#passResult("Faculty of Science", "Scholarship", "D")