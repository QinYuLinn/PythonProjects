import sys
import requests
from bs4 import BeautifulSoup #导入程序运行所依赖的python包
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")
weeping_title=sys.argv[1]
weeping_author=sys.argv[2]
weeping_source_file=sys.argv[3]
file_output=sys.argv[4]
try:
    file_source_pointer=open(weeping_source_file,'r')
except Exception:
    print("file "+weeping_source_file+" does not exist!")
    exit
try:
    file_output_pointer=open(file_output,'w')
except Exception:
    print("file "+file_output+" acquire some error!")
    exit
file_output_pointer.write('<!DOCTYPE html>\n<head>\n<title>\n</title>\n<link href="http://www.xuantianlinyu.com.cn/css/article.css" rel="stylesheet" type="text/css" />\n</head>\n<body onclick="closeshowBos()">\n<meta charset="UTF-8">\n<div class="main3">\n<div class="left">\n<div style=" width:1px; height:1px; overflow:hidden;">\n</div>\n<div class="sons" id="sonsyuanwen"><div class="cont">\n')
file_output_pointer.write('<h1 style="font-size:20px; line-height:22px; height:22px; margin-bottom:10px; text-align:center">\n'+str(weeping_title)+'\n</h1>\n')
file_output_pointer.write('<p class="source" style="text-align:center">\n<a href="">\n'+weeping_author+'\n</a></p>\n')
file_output_pointer.write('<div class="contson" id="contsonc7e28ca4629f">\n')
tempstring=[]
jindex=0
for news in file_source_pointer.readlines():
    news=news.strip('\n')
    if len(news)>2:
        tempstring=''
        file_output_pointer.write('<p>')
        tempstring=tempstring+news[0]
        for jindex in range(1,len(news)-1):
            if((news[jindex]==' ' and news[jindex+1]==' ') or (news[jindex]==' ' and news[jindex-1]==' ')):
                 tempstring=tempstring+'&nbsp;'
            elif(news[jindex]=='\t'):
                tempstring=tempstring+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
            else:
                tempstring=tempstring+news[jindex]
        tempstring=tempstring+news[-1]
        file_output_pointer.write(tempstring)
        file_output_pointer.write('</p>\n')
    elif(len(news)>0 and len(news)<=2):
         tempstring=''
         tempstring=tempstring+news
         file_output_pointer.write(tempstring)
         file_output_pointer.write('</p>\n')
file_output_pointer.write('<div class="sons">\n<div class="contyishang">\n<div style="height:30px; font-weight:bold; font-size:16px; margin-bottom:10px; clear:both;">\n<h2>\n<span style="float:left;">\n创作背景\n</span>\n</h2>\n<span id="shangxiPlay27057" style=" display:none;width:1px; height:1px; float:left;">\n</span>\n</div>\n<p>写入创作背景部分</p>\n</div>\n</div>\n</div>\n</div>\n</div>\n</div>\n</div>\n</body>\n</html>\n')
