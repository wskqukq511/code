from PIL import Image,ImageFont,ImageDraw    #导入PIL库中所需要的模块
import sys

#头像路径
headPath = r"./"
#输出路径
outputPath = r"./"

#字体路径
fontPath = r"./"
#头像文件
headFile = r"ex0000.jpg"
#输出文件
outFile = r"exoutput.jpg"

#打开图片建立画布
image = Image.open(headPath + headFile,'r')
draw = ImageDraw.Draw(image)
#print(min(image.size))
#由图片大小确定字体大小
fontsize = int(min(image.size)/4)

#增加文字
fontobj = ImageFont.truetype(font = fontPath + "st.otf",size = fontsize,index=0,encoding='')
draw.text((image.size[0]-fontsize,20),text="4",fill=(255,0,0),font=fontobj,anchor=None)
image.save(outputPath+outFile)  #保存图片