#http://www.heibanke.com/lesson/crawler_ex00/
#python黑板客爬虫闯关
import requests
from bs4 import BeautifulSoup
import re

stat_url = "http://www.heibanke.com/lesson/crawler_ex00/"
start_html = requests.get(stat_url)
soup = BeautifulSoup(start_html.text, 'lxml')
next_number = soup.find('h3')
next_number = re.findall("\d+", str(next_number.get_text()))
while next_number:
    url = "http://www.heibanke.com/lesson/crawler_ex00/" + next_number[0]
    print(url)
    html = requests.get(url)
    tmp = BeautifulSoup(html.text, 'lxml')
    nextnumber = tmp.find('h3')
    next_number = re.findall("\d+", str(nextnumber.get_text()))

print(nextnumber)


