from urllib import request
import time
import os
import csv

filename = time.strftime("%Y%m%d")+".js"
url="http://www.sse.com.cn/js/common/stocks/new/600086.js"

if os.path.exists(filename):
    print("今天的公告已下载")
else:
    request.urlretrieve(url, time.strftime("%Y%m%d") + ".js")

all_the = open(filename,encoding='utf-8')
#print(all_the)
for line in all_the:
    data = line[line.find('bulletin_date:"'):line.find('",bulletin_year')][15:]
    title = line[line.find('bulletin_title:"'):line.find('",bulletin_file_url')][16:]
    gonggao_url = 'http://static.sse.com.cn/'+ line[line.find('bulletin_file_url:"'):line.find('",bulletin_time')][19:]
    #print(type(data),type(title) ,type(gonggao_url))
    csvfile = open(time.strftime("%Y%m%d")+'.csv','w')
    writer = csv.writer(csvfile)
    for key in data:
        writer.writerow([key,data + ',' + title + ',' + gonggao_url])



