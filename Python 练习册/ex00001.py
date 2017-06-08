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


print(gen_code(8,100))




