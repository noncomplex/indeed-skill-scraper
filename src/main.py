from scraper import Scraper
from prettytable import PrettyTable
import os
import string
import collections

def main(driver_path):
    what = input('job? (ex. software engineer): ')
    where = input('where? (ex. remote): ')
    pages = int(input('how many search pages?: '))

    try:
        with Scraper(driver_path = driver_path) as scraper:
            scraper.search_job(what, where)
            job_descs = scraper.get_job_descriptions(pages)

            # filters    
            ## remove non-capitalized words
            caps_only = filter(lambda word: word[0].isupper(), job_descs)

            ## remove days of the week
            no_days = filter(lambda word:
                             word != 'Monday' and
                             word != 'Tuesday' and
                             word != 'Wednesday' and
                             word != 'Thursday' and
                             word != 'Friday', caps_only)

            ## not in common words
            with open('../resources/1000_words.txt', 'rt') as f:
                com_words = f.read().split()
                com_words = list(map(lambda word: word.capitalize(), com_words))
                final_words = filter(lambda word: word not in com_words, no_days)

            ## other common words that pop in job listings
            with open('../resources/select_filters.txt', 'rt') as f:
                words = f.read().split()

            final_words = filter(lambda word: word not in words, final_words)
        
            counter = collections.Counter(final_words).most_common()[:10]
            skill_rows = []
            for pair in counter:
                skill_rows.append([pair[0], pair[1]])
            
            table = PrettyTable(
                field_names=["Skill", "Count"]
            )
            table.add_rows(skill_rows)
            print(table)

    except Exception as e:
        if 'in PATH' in str(e):
            print('set driver_path to your Selenium drivers folder when creating Scraper()')


if __name__ == '__main__':
    main(r'A:\SeleniumDrivers')
        
