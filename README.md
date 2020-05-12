# ao3statsscrape
Scrape your AO3 (Archive of Our Own) profile to record the stats of your works over time
## Introduction
This is my first real Python try. There are undoubtedly better ways to do this but it seems to work? This was made and run in a Windows environment.

After successfully setting this up, can make a batch file to run it, then set it as a scheduled task. Your stats will be compiled into one file as you have scheduled.
## Acknowledgements
Based heavily off the tutorial at: https://librarycarpentry.org/lc-webscraping/04-scrapy/index.html
## Installation
### Get Anaconda
* https://docs.anaconda.com/anaconda/install/
### Ensure you have scrapy installed through Anaconda
* If not, install it via the Anaconda shell according to the instructions at their website https://docs.scrapy.org/en/latest/intro/install.html
## Use
### Make your project
* In Anaconda shell, navigate to the directory where you want to put your project
* Once in the right directory, enter: python -m scrapy ao3scrape
* Make a new spider with the following (replace YOURUSERNAME with your actual AO3 username): python -m scrapy genspider profilescraper archiveofourown.org/users/YOURUSERNAME/works
* Navigate down to the newly created spider and open it in a text editor
* Change the file to match profilescraper.py in this GitHub repository, but ensure you update the start_url to your own profile's URL
* Navigate to items.py in your project (it's the 2nd ao3scrape directory)
* Change the file to match items.py in this GitHub repository
### Run the project
* In the Anaconda shell, navigate to your main scrapy project directory (where scrapy.cfg is). Type: python -m scrapy crawl profilescraper -o output.csv
* Check to make sure the output.csv file contains what you want
* scrapy appends new content rather than overwriting so you'll get a running list of your stats
### Make a batch file
* Make a new .bat file and update it to match ao3scrape.bat in this GitHub repository
* Change all of the directories to the relevant ones on your computer
* Make sure cd C:\THEFULLPATHOFYOURPROJECT is pointing to the place where scrapy.cfg is on your computer
### Set up task scheduler
* The easiest part!
* Make a new task in your Windows Task Scheduler to action the batch file daily
* You can run the task right away to make sure it's working, then wait as it runs each day and collects all your stats for you
## Issues / For the future
* Trying to grab the title of the fic does not return anything?
* Is it possible/easier to just grab all the details directly from the profile page itself? Yes, but it's in a list and how do we deal with this in scrapy? How do we deal with list items that don't have certain elements like comments?
