import requests #http request
from bs4 import BeautifulSoup as bs # webscraping

#send email
import smtplib

#emailbody
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#system Date time manipulation

import datetime
#extract current datetime
#create email subject line to make sure that the email is send everyday
now = datetime.datetime.now()

# email content place
content = ''

def extract_news(url):
    print('extracting News Stories')
    cnt = '' #place holder for assigning content
    cnt += ('<b>Top Stories:</b>\n'+'<hr>') #first line
    response = requests.get(url) #get content from the url and stored in the response object
    content = response.content #get the content of the http response object
    soup = bs(content,'html.parser')
    for i,tag in enumerate(soup.find_all('h3',attrs={'class': 'title-news'})):
        # after extract all the data with its index we pass the output to cnt
        if i == 30:
            break
        cnt += ((str(i+1) + ' :: '+tag.text + "\n" + '<br>' ) if tag.text!= 'More' else '')
    return(cnt)

cnt = extract_news('https://vnexpress.net/goc-nhin')
content += cnt
content += ('<br>')

content +=('End of Message')

print(content)