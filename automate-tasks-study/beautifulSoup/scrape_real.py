#write a program to pull a job listing
from bs4 import BeautifulSoup as bs
import requests
import html5lib
url ='https://itviec.com/it-jobs/django/ho-chi-minh-hcm?job_selected=backend-developer-python-django-skylink-group-2649'
html_text= requests.get(url).content
soup = bs(html_text,'html5lib')
jobs = soup.find_all('div', class_='job-card')
for i,job in enumerate(jobs) :
    position_name = job.find('a', attrs={'data-search--job-selection-target': 'jobTitle'}).text
    company_name = job.find('a', attrs={'data-controller': 'utm-tracking', 'class':'text-rich-grey'}).text
    date_post_list = job.find('span', class_='small-text text-dark-grey').text.splitlines()
    date_post =''
    for item in date_post_list:
        date_post += item
        date_post += ' '
    
    print(f'''Position {str(i+1)}: {position_name}
    Company : {company_name}
    Date post: {date_post}
    ----------------------
    ''')
       