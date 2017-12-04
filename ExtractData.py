# Grabs html code from given url
# This solution does work but it is slow
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from Award import Award

counter = 0

def passResult(faculty, type, keyword, amount, indig, inter, disabil, appli, renew):
    driver = webdriver.PhantomJS()
    result = []
    typeList = ["Athletic Award", "Bursary", "Combined Medal and Prize", "Fellowship", "Medal", "Prize", "Scholarship",
                "Undergraduate Research Award"]
    typeSyn = ["ATHL+AWARD", "BURS", "COMB", "FELLOW", "MEDAL", "PRIZE", "SCHOL", "RESEARCH"]

    # Get the original page

    for currFaculty in faculty:
        for currType in type:
            # Max Rady College of Medicine is an exception, it has sub-branches
            if currFaculty == "Max Rady College of Medicine":
                if currType == "View all types":
                    for type in typeSyn:
                        driver.get(
                            "https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type="+type+"&disabled=&major=-1&awardsPerPage=10&faculty=05")
                        result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                        try:
                            while driver.find_element_by_link_text("Next"):
                                driver.find_element_by_link_text("Next").click()
                                result += extractAwards(driver, keyword, amount, renew)
                        except NoSuchElementException:
                            pass

                        driver.get(
                            "https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type="+type+"&disabled=&major=-1&awardsPerPage=10&faculty=05")
                        result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                        try:
                            while driver.find_element_by_link_text("Next"):
                                driver.find_element_by_link_text("Next").click()
                                result += extractAwards(driver, keyword, amount, renew)
                        except NoSuchElementException:
                            pass

                elif currType == "Entrance Bursary":
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=ENTRANCE&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=BURS&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword, amount, renew)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=ENTRANCE&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=BURS&awardsPerPage=10&disabled=&faculty=05&major=-1")
                    result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword, amount, renew)
                    except NoSuchElementException:
                        pass

                elif currType == "Entrance Scholarship":

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=ENTRANCE&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=SCHOL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword, amount, renew)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=ENTRANCE&_requireApp=&program=-1&aboriginal=&international=&awardName=&type=SCHOL&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword, amount, renew)
                    except NoSuchElementException:
                        pass

                else:
                    index = typeList.index(currType)
                    currentType = typeSyn[index]
                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-FSS%2C-FSS2?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type="+currentType+"&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword, amount, renew)
                    except NoSuchElementException:
                        pass

                    driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/showSubFacAwards/-00%2C-S?Search=Search&level=-1&_requireApp=&program=-1&aboriginal=&international=&awardName=&type="+currentType+"&disabled=&major=-1&awardsPerPage=10&faculty=05")
                    result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                    try:
                        while driver.find_element_by_link_text("Next"):
                            driver.find_element_by_link_text("Next").click()
                            result += extractAwards(driver, keyword, amount, renew)
                    except NoSuchElementException:
                        pass

            else:
                driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")
                if indig and indig!="-1":
                    Select(driver.find_element_by_xpath("//*[@id='aboriginal']")).select_by_visible_text(indig)

                if inter and inter!="-1":
                    Select(driver.find_element_by_xpath("//*[@id='international']")).select_by_visible_text(inter)

                if disabil and disabil!="-1":
                    Select(driver.find_element_by_xpath("//*[@id='disabled']")).select_by_visible_text(disabil)

                if appli and appli=="on":
                    driver.find_element_by_xpath("//*[@id='requireApp']").click()

                if currType == "View all types":
                    for y in typeList:
                        Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(currFaculty)
                        Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text(y)
                        Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")
                        driver.find_element_by_xpath("//*[@id='Search']").click()
                        result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                        try:
                            while driver.find_element_by_link_text("Next"):
                                driver.find_element_by_link_text("Next").click()
                                result += extractAwards(driver, keyword, amount, renew)
                        except NoSuchElementException:
                            pass

                else:
                    Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text(currFaculty)
                    Select(driver.find_element_by_xpath("//*[@id='awardsPerPage']")).select_by_visible_text("30")

                    if currType == "Entrance Bursary":
                        Select(driver.find_element_by_xpath("//*[@id='level']")).select_by_visible_text("Entrance")
                        Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text("Bursary")
                        driver.find_element_by_xpath("//*[@id='Search']").click()
                        result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                        try:
                            while driver.find_element_by_link_text("Next"):
                                driver.find_element_by_link_text("Next").click()
                                result += extractAwards(driver, keyword, amount, renew)
                        except NoSuchElementException:
                            pass

                    elif currType == "Entrance Scholarship":
                        Select(driver.find_element_by_xpath("//*[@id='level']")).select_by_visible_text("Entrance")
                        Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text("Scholarship")
                        driver.find_element_by_xpath("//*[@id='Search']").click()
                        result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                        try:
                            while driver.find_element_by_link_text("Next"):
                                driver.find_element_by_link_text("Next").click()
                                result += extractAwards(driver, keyword, amount, renew)
                        except NoSuchElementException:
                            pass

                    else:
                        Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text(currType)
                        driver.find_element_by_xpath("//*[@id='Search']").click()
                        result += extractAwards(driver, keyword, amount, renew)  # result on the first page
                        try:
                            while driver.find_element_by_link_text("Next"):
                                driver.find_element_by_link_text("Next").click()
                                result += extractAwards(driver, keyword, amount, renew)
                        except NoSuchElementException:
                            pass

    return result


def extractAwards(currPage, keyword, amount, renew):
    soup = BeautifulSoup(currPage.page_source, "html.parser")

    driver2 = webdriver.PhantomJS()

    awards = []
    results = []  # Contains keyword related results
    keywords = []  # Collection of keyword
    global counter

    type = soup.find(id="award").text.split()

    for entry in soup.find_all("div", {"id": "awardInfo"}):
        url = "https://wwwapps.cc.umanitoba.ca:8443" + entry.find('a').get('href')
        name = entry.find('a').text
        spanList = entry.find_all(id="rightTag")
        if keyword == "" and amount == "":
            counter += 1
        award = Award(url, spanList[0].text, name, type[3], spanList[1].text, spanList[2].text, None, 0, None,
                      entry.find(id="awardDesc").text.strip()[:-1][1:], counter)

        # Both amount and renewable are presented
        if amount!="" and renew=="on":
            driver2.get(url)
            soup2 = BeautifulSoup(driver2.page_source, "html.parser")
            div = soup2.find_all('div', class_="rowDisp")
            price = div[3].text.strip()[14:][:12].strip()
            try: # Make sure get the numerical value not string
                renewable = div[2].text.strip()[38:].strip()
                if int(price) >= int(amount) and renewable=="Yes":
                    counter += 1
                    award.sequence = counter
                    awards.append(award)
            except:
                pass
        # Only amount is presented
        elif amount!="" and renew!="on":
            driver2.get(url)
            soup2 = BeautifulSoup(driver2.page_source, "html.parser")
            div = soup2.find_all('div', class_="rowDisp")
            price = div[3].text.strip()[14:][:12].strip()
            try:  # Make sure get the numerical value not string
                if int(price) >= int(amount):
                    counter += 1
                    award.sequence = counter
                    awards.append(award)
            except:
                pass
        # Only renewable is presented
        elif amount=="" and renew=="on":
            driver2.get(url)
            soup2 = BeautifulSoup(driver2.page_source, "html.parser")
            div = soup2.find_all('div', class_="rowDisp")
            try: # Make sure get the numerical value not string
                renewable = div[2].text.strip()
                if renewable=="Yes":
                    counter += 1
                    award.sequence = counter
                    awards.append(award)
            except:
                pass
        # Neither amount nor renewable are presented
        elif amount=="" and renew!="on":
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
                        break
                if (isFound == True):
                    counter += 1
                    award.sequence = counter
                    results.append(award)
        # if find logical conjunction OR
        elif keyword.find("OR") != -1:
            keywords = keyword.split("OR")
            for award in awards:
                awardInfo = str(award.displayAward())
                for currKeyword in keywords:
                    if awardInfo.find(currKeyword.strip()) != -1:
                        counter += 1
                        award.sequence = counter
                        results.append(award)
                        break
        # if find logical conjunction NOT
        elif keyword.find("NOT") != -1:
            keywords = keyword.split("NOT")
            for award in awards:
                isFound = True
                awardInfo = str(award.displayAward())
                firstKeyword = keywords[0]
                # There is a keyword before logical conjunction NOT
                if firstKeyword != "":
                    if awardInfo.find(firstKeyword.strip()) != -1:
                        for currKeyword in keywords[1:]:  # make sure the keyword after NOT is not included
                            if awardInfo.find(currKeyword.strip()) != -1:
                                isFound = False
                                break
                        if (isFound == True):
                            counter += 1
                            award.sequence = counter
                            results.append(award)
                else:
                    for currKeyword in keywords[1:]:  # make sure the keyword after NOT is not included
                        if awardInfo.find(currKeyword.strip()) != -1:
                            isFound = False
                            break
                    if (isFound == True):
                        counter += 1
                        award.sequence = counter
                        results.append(award)

        # no logic conjunction is found, only single keyword
        else:
            for award in awards:
                awardInfo = str(award.displayAward())
                if awardInfo.find(keyword) != -1:
                    counter += 1
                    award.sequence = counter
                    results.append(award)

        return results
    else:
        return awards

def getTotal():
    global counter
    temp = counter # Pass counter value to temp
    counter = 0 # Clear counter after each query
    return temp