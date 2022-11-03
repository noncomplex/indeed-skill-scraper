# indeed-skill-scraper
scrapes relevant words form Indeed job listings and returns the top 10 counts.
Set ChromeDriver path variable for the Scraper object in the main call at the end of main.py (ex. main(r"path to ChromeDriver.exe")), run main.py and simply follow the prompts.<br />
![2022-11-01 16_44_16-Cmder](https://user-images.githubusercontent.com/71818162/199337942-b9ae15b9-caf9-4553-a040-db613e9d1d0d.png)


## Requirements
working with
* Python 3.9.6
* Selenium 4.5.0
* prettytable 3.4.1
* ChromeDriver 106 (any suitable ChromeDriver with the appropriate chrome version should work)

## Note
* Site must be loaded and in active view
* Occasionally will bug out and need to be ran again (data attribute not found, new tabs being opened)
* Indeed's anti-scraping mechanisms may kick in
* Takes a few minutes to scrape a few pages
* For reasons above only recommend scraping 2-3 pages
* The non-included word-list is non-exhaustive and words can be added
