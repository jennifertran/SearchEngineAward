# Grabs html code from given url

import urllib

link = "https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/searchForm/awardSearch"
f = urllib.urlopen(link)
myfile = f.read()
print myfile