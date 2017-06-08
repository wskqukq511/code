from urllib import request
import time
import os
import codecs
import csv

filename = time.strftime("%Y%m%d")+".js"
url="http://www.sse.com.cn/js/common/stocks/new/600086.js"

if os.path.exists(filename):
    print("今天的公告已下载")
else:
    request.urlretrieve(url, time.strftime("%Y%m%d") + ".js")

all_the = open(filename,encoding='utf-8')
#print(all_the)

#返回公告连接和标题
def getdata():
    list_date = []
    for line in all_the:
        data = line[line.find('bulletin_date:"'):line.find('",bulletin_year')][15:]
        title = line[line.find('bulletin_title:"'):line.find('",bulletin_file_url')][16:]
        gonggao_url = 'http://static.sse.com.cn/' + line[line.find('bulletin_file_url:"'):line.find('",bulletin_time')][
                                                    19:]
        new_url = '<embed src="'+gonggao_url + '" width="800" height="600" />'
        if data :
            list_date.append([data, title, gonggao_url,new_url])


        #print(list_date[0:3])
    return list_date



#print(getdata())
#写入csv文件
with open(time.strftime("%Y%m%d")+'.csv','wb') as f:
    for item in getdata():
        line = ','.join(item)+'\n'
        f.write(line.encode('gb18030'))







