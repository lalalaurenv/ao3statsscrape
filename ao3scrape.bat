@echo on
call C:\PATHOFANACONDA\Anaconda3\Scripts\activate.bat C:\PATHOFANACONDA\Anaconda3\
d:
cd C:\THEFULLPATHOFYOURPROJECT
python -m scrapy crawl profilescraper -o output.csv
