from scraper import Scraper
from prettytable import PrettyTable
import os
import string
import collections
            
what = input('job? (ex. software engineer): ')
where = input('where? (ex. remote): ')
pages = int(input('how many search pages?: '))

try:
    with Scraper() as scraper:
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
        with open('1000-words.txt') as f:
            com_words = f.read().split()
            com_words = list(map(lambda word: word.capitalize(), com_words))
            final_words = filter(lambda word: word not in com_words, no_days)

        ## other common words not in file
        words = ['Google', 'Minimum', 'San Francisco', 'America', 'Florida', 'Click',
                 'Software', 'Required', 'Ability', 'LLC', 'EEO', 'COVID19', 'Qualification',
                 'Qualifications', 'Engineer', 'Intermediate', 'Youll', 'Engineering', 'Dev',
                 'Maintain', 'Business', 'Collaborate', 'Ethical', 'Effective', 'Health', 'Description',
                 'Scope', 'Fortune', 'Expert', 'Proven', 'Implement',  'Certification', 'Systems',
                 'Security', 'Freedom', 'Web', 'Responsibility', 'Global', 'Manager', 'Staff',
                 'Prior', 'Develops', 'Delivery', 'Takes', 'Learns', 'Plans', 'Aligns', 'Creates',
                 'Works', 'Collaborates', 'Relates', 'Helps', 'Notes', 'Reports', 'Established',
                 'Quickly', 'Excellent', 'Customer', 'San', 'Francisco', 'Colorado', 'Palm', 'Beach',
                 'Miami', 'Digital', 'Engineers', 'Demonstrated', 'Senior', 'Computer', 'Knowledge',
                 'Developer', 'Services', 'Skills', 'Code', 'Collective', 'Whats', 'Title', 'CEO',
                 'Deliver', 'Responsibilities', 'Candidates', 'Benefits', 'Dental', 'Location', 'Status',
                 'United', 'States', 'Duties', 'Fluent', 'Opportunity', 'Corporate', 'Rising',
                 'Commitment', 'Innovation', 'Follows', 'Exposure', 'Executes', 'Builds', 'Purpose',
                 'Role', 'Requirements', 'Benefits', 'App', 'Vision', 'Salary', 'Integrated', 'Solutions',
                 "We're", 'Results', 'Specific', 'Focused', 'Applicants', 'Development', 'Maryland',
                 'Pinterest', 'Depot', 'Toast', 'Johns', 'Hopkins', 'Philadelphia', 'ACT', 'SAT',
                 'Forbes', 'Inclusion', 'Curation', 'USA', 'Employee', 'Contract', 'Wellness', 'Functions',
                 'English', 'Tech', 'Delivers', 'Provides', 'Exhibits', 'Years', 'Growth', 'University',
                 'Building', 'Relational', 'Interact', 'Wizard', 'Winner', 'Funding', 'Familiarity',
                 'Preferred', 'Remote', 'Schedule', 'Manages', 'Perspective', 'Located', 'Environment',
                 'However', 'Leader', 'Asset', 'Assets', 'Culture', 'Medical', 'Entry', 'Associate',
                 'US', 'Union', 'TherapyNotes', 'MasteryPrep', 'Principal', 'I', 'II', 'Position',
                 'Positions', 'UnitedHealth', 'Inc', 'Jack', 'SWE', 'Education', 'Liberty', 'Mutual',
                 'Flexible', 'Fulltime', 'Paid', 'Ezoic', 'Insurance', 'Proficiency', 'Amazon',
                 'Americas', 'York', 'New', 'Employers', 'APIs', 'Professional', 'Professionals',
                 'Extensive', 'OpenGov', 'Henry']
    
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
