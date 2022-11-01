# indeed-skill-scraper
scrapes relevant words form Indeed job listings and returns the top 10 counts.
Set Selenium driver path variable for the Scraper object in main.py (ex. Scraper(driver_path="your path")), run main.py and simply follow the prompts.
![2022-11-01 16_44_16-Cmder](https://user-images.githubusercontent.com/71818162/199337942-b9ae15b9-caf9-4553-a040-db613e9d1d0d.png)


## Requirements
working with
* Python 3.9.6
* Selenium 4.5.0
* prettytable 3.4.1
* ChromeDriver 106

## Note
* Occasionally will bug out and need to be ran again
* Indeed's anti-scraping mechanisms may kick in
* Takes a few minutes to scrape a few pages
* For reasons above only recommend scraping 2-3 pages
* The non-included word-list is non-exhaustive and words can be added
