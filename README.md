# README #

### What is this repository for? ###

All items to do with building and parameterising a model that will enable us to be able to determine the value of the insured cars

### What is here so far: ###

* Web-scraper built to scrape data from the SA car search engine "cars.brick7.co.za" 
* Relatively clean dataset as output from the scraper in the file "clean_cars.csv" - this is to be used to parameterise the depreciation model. 

### About the web-scraper ###

* The web-scraper is built in python on the "scrapy" library.
* It is currently set up pipe the data into a postgressql database called scrape. 
* There are two spiders, one for national data and another for city specific data - have to but run one at a time.
* The code is based on the tutorial: "http://newcoder.io/scrape"

### If you want to run the scraper on your PC ###

* Have a look at the tutorial: "http://newcoder.io/scrape" - it will help with the initial setup - highly recommended!
* Set up a virtual environment and install the python libraries found in the requirements.txt file
* create a postgressql database called scrape
* set up a postgresql username and password and put these details in the "settings.py" file
* cd to "car_scraper/scraper_app"
* start the postgressql server "sudo service postgressql start"
* run the spiders one at a time (national and city) simply by commenting out the spider that you don't want to run.
* inspect the output in postgressql - the table name can be found in the model.py file.


### Next steps: ###

* Decide what value we want to pay out e.g retail value, trade-in value, replacement value, book value, etc.
* Build model in Excel - parameterise based on the data in "clean_cars.csv" (possibly keep back some data for a test and validation set)
* Test the model either on a test and validation subset of the data, or on another online website like cars.co.za
* Build final model in python and deploy it to the python server.

### Who do I talk to? ###

* Geoffrey Clark