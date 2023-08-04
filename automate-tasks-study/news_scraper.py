import requests #http request
from bs4 import BeautifulSoup as bs # webscraping
import html5lib
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
souping = ''
def extract_news(url):
    print('extracting News Stories')
    cnt = '' #place holder for assigning content
    cnt += ('<b>Top Stories in thời sự:</b>\n'+'<hr>') #first line
    response = requests.get(url) #get content from the url and stored in the response object
    content = response.content #get the content of the http response object
    soup = bs(content,'html5lib')
    for i,tag in enumerate(soup.find_all('h3',class_ = 'title-news')):
        # after extract all the data with its index we pass the output to cnt
        if i == 10:
            break

        cnt += ((str(i+1)+'::'+tag.text.strip() + '\n' + '<br>' ))
    return(cnt)

cnt = extract_news('https://vnexpress.net/thoi-su')
content += cnt
content += ('<br>-------<br>\n')

content +=('End of Message')

print(content)