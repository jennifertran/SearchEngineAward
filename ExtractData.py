# Grabs html code from given url

# import urllib
#
# link = "https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch"
# f = urllib.urlopen(link)
# myfile = f.read()
# print myfile

# !/usr/bin/python
# import re
# from mechanize import Browser
# br = Browser()
#
# # Ignore robots.txt
# br.set_handle_robots(False)
# # Google demands a user-agent that isn't a robot
# br.addheaders = [('User-agent', 'Firefox')]
#
# # Retrieve the Google home page, saving the response
# br.open("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")
#
# br.select_form('award_searchTemplate')
# # br.select_form(nr=0)
#
# # br.select_form( 'award_searchTemplate' )
# if br.form["faculty"] == ["Choose a faculty/school"]:
#     br.form["faculty"].value = ["02"]
#
# if br.form["type"] == ["Choose an Award Type"]:
#     br.form["type"].value = ["SCHOL"]
#
# #br.form['faculty'].value = ["Faculty of Science"]
# # br.form['type'].value = ["Scholarship"]
#
# #
# # Get the search results
# # br.submit(name="Search")
#
# r = br.submit()
#
# print r.read()



# This solution does work but it is slow
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()

driver.get("https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch")

Select(driver.find_element_by_xpath("//*[@id='faculty']")).select_by_visible_text("Faculty of Science")
Select(driver.find_element_by_xpath("//*[@id='type']")).select_by_visible_text("Scholarship")

driver.find_element_by_xpath("//*[@id='Search']").click()

soup = BeautifulSoup(driver.page_source)

print soup