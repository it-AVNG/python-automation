#write a program to pull a job listing
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import time

def find_itviec_django_job():
    url ='https://itviec.com/it-jobs/django/ho-chi-minh-hcm?job_selected=backend-developer-python-django-skylink-group-2649'
    html_text= requests.get(url).content
    soup = bs(html_text,'html5lib')
    jobs = soup.find_all('div', class_='job-card')
    for i,job in enumerate(jobs) :
     
        position_name = job.find('a', attrs={'data-search--job-selection-target': 'jobTitle'}).text
        link_job = 'https://itviec.com/'
        link_job += job.find('h3').a['href']
        company_name = job.find('a', attrs={'data-controller': 'utm-tracking', 'class':'text-rich-grey'}).text
        date_post_list = job.find('span', class_='small-text text-dark-grey').text.splitlines()
        date_post =''
        for item in date_post_list:
            date_post += item
            date_post += ' '
        with open(f'posts/itviec.txt', 'a') as f:
            f.write(f'Position {str(i+1)}: {position_name}\n Company : {company_name}\n Date post: {date_post}\n link: {link_job}\n ---------------------- \n')

if __name__ == '__main__':
    # while True:
        print(f'look up django job on itviec.com: ')
        now = datetime.now()
        with open(f'posts/itviec.txt', 'w') as f:
             f.write(f'Date post: {now} \n')
        find_itviec_django_job()
        time_wait= 240
        print(f'wrote output to file! please check the file')
        time.sleep(time_wait * 60)