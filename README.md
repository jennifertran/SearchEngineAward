# Search Engine Award

The main goal of the project was to improve the existing University of Manitoba’s Award form by implementing a search engine to it as the one used by the University was not effective enough.

<img src="https://raw.githubusercontent.com/jennifertran/SearchEngineAward/master/static/screenshot.png" width="700px" height="400px">

**Previous version:** https://wwwapps.cc.umanitoba.ca:8443/searchableAwards/ <br>
**New proposed version of the application live:** https://searchengineaward.herokuapp.com/

**Created by [Zhikan Xu](https://github.com/Jason-xu96), and [Jennifer Tran](https://github.com/jennifertran)**

## Features
* Three new filter categories of awards:
  * All awards	
  * Entrance scholarships
  * Entrance bursaries 
  
* Filters by keyword(s) and logical conjunction(s)
  * eg) Quantum **AND** Chemistry, Electronics **OR** Engineering, Math **NOT** Physics
  
* Filters by amount
  * eg) Return only those worth more than $500
  
* Filters by due date

* Filters for Indigenous students

* Filters by whether the award is renewable

* Filters by whether an application form is required or not

* Filters for students with disabilities
* Filters for international students

## Challenges Faced
* Filtering by due date was an issue since only a small portion of awards contain a specific date (even some were outdated). 
  * As a result we left the form option on the app but disabled since the feature was never implemented on the backend.
* The speed of the application is slow since we had no API or access of the backend of the University’s awards database.
  * The only way we were able to bypass that is by web scraping all of the awards that was returned in the site’s form.
  * We did a test run of the app on heroku (https://searchengineaward.herokuapp.com/) but the issue is that when a request reaches more than 30 seconds the connection is cut since we have no control over the maximum timeout limit.
* Hosting the app to the University of Manitoba’s server was another issue as well since the tech stack that was used to built this application was not compatible with the University’s backend server. 
  * We spoke to IT about our project and he mentioned that the only way we are able to launch our app successfully is if they were to implement a virtual environment which requires permission from our supervisor first before proceeding. 
  * The only downfall is that it would have taken them weeks to get the virtual environment going which was not in our time schedule.

## The Future of the Project:
* Our supervisor mentioned that there is a possibility that the project may require maintenance that we can be compensated for in future terms.
* There were several features that we wanted to implement but were unable to including:
  * Making the site responsive (mobile friendly)
  * Improving the user interface of the application
  * Improve the speed of the search engine 
  * Hosting the application on the University’s server
  * Highlight the keywords of an award if given
  * Numbering how many awards were being scanned while user was waiting for a search result

## How to install & run the app locally

**Step 1:** Clone or download the repo 

**Step 2:** cd into the SearchEngineAward Directory

**Step 3:**  Install Python libraries using the following command (**must activate virtualenv first**) :

~~~
pip install -r requirements.txt
~~~

**Step 4:** Install the frontend libraries via bower (requires npm)

~~~
bower install
~~~

**Step 5:** Run the program using:

~~~
python main.py
~~~

## Copyright ©

Apache License 2.0, all rights reserved
