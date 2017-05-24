import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import  re


data = {'username':'herui'}
url = "http://www.heibanke.com/lesson/crawler_ex01/"

for num in range(1,31):
    data['password']=num
    post_data = urllib.parse.urlencode(data).encode(encoding='utf-8')
    next_number = urllib.request.urlopen(url,post_data)
    html =  next_number.read().decode('utf-8')
    print(post_data)
    result = re.findall("密码错误",html)
    if not result:
        print(html)
        break



