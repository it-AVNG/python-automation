from bs4 import BeautifulSoup as bs

## after we download an html, 
# we open the file and read it
#working with file
with open('D:\Onedrive\Desktop\MarkdownReference.htm', 'r') as html_file:
    content = html_file.read()

    soup = bs(content, 'html5lib')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] 

        print(f'{course_name} cost {course_price}')