import mysql.connector
import random

def gen_code(length = 8,num=10):
    "将0-9,a-z,A-Z保存到list中，用random.sample从list中取固定位数"
    code_list = []
    veri_code = []
    for i in range(10):
        code_list.append(str(i))
    for i in range(65,91):
        code_list.append(chr(i))
    for i in range(97,123):
        code_list.append(chr(i))

    i=0
    while True:
        myslice = random.sample(code_list, length)
        veri_code.append(''.join(myslice))
        i += 1
        if i>= num:
            break
    return veri_code

def save_to_db(veri_code):
    #打开数据库连接
    conn = mysql.connector.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='ex0002')
    #创建cursor对象
    try:
        cursor = conn.cursor()
        #使用execute()方法执行sql，如果存在则删除
        sql = "insert into veri_code(id, code) values(%s, %s)"
        for i in range(len(veri_code)):
            cursor.execute(sql,(i,veri_code[i]))
        conn.commit()
        cursor.close()
    finally:
        conn.close()

if __name__ == "__main__":
    save_to_db(gen_code(8,200))