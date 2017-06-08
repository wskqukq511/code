import urllib.request
from bs4 import BeautifulSoup
import re

#伪装浏览器登陆，获取网页源代码
def getPage(href):
    headers={'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.1;en-US;rv:1.9.1.6)Gecko/20091201 Firefox/3.5.6'}
    req = urllib.request.Request(
        url = href,
        headers = headers
    )
    try:
        post=urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.reason)
    return post.read()

#初始化url双色球首页
url='http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html'

#==========================================================================

#获取url总页数
def getPageNum(url):
    num = 0
    page = getPage(url)
    soup = BeautifulSoup(page)
    strong = soup.find('td',colspan = '7')
    #print strong
    if strong:
        result = strong.get_text().split('')
        #print result
        list_num = re.findall("[0-9]{1}",result[1])
        #print list_num
        for i in range(len(list_num)):
            num = num * 10 + int(list_num[i])
        return num
    else:
        return 0

#获取每页双色球的信息
def getText(url):
    for list_num in range(1,getPageNum()):   #从每一页到第getPageNum(url)页
        print(list_num)  #打印下页码
        href = 'http://kaijiang.zhcw.com/zhcw/html/ssq/list_' + str(list_num) + 'html'   #调用新url链接
        #for listnum in len(list_num)
        page = BeautifulSoup(getPage())
        em_list = page.find_all('em')  #匹配em内容
        div_list = page.find_all('td',{'align':'center'}) #匹配<td align = center>这样的内容

        #初始化
        n = 0
        #将双色球数字信息写入num.txt文件
        fp = open('num.txt','w')
        for div in em_list:
            emnum1 = div.get_text()
            #print emnum1
            txt = div.get_text()
            text = text.encode('utf-8')
            #print title
            n = n + 1
            if n == 7:
                text = text + '\n'
                n = 0
            else:
                text = text + '.'
            fp.write(str(text))
        fp.close()

