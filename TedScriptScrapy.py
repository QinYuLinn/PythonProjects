import sys
import requests
from bs4 import BeautifulSoup #导入程序运行所依赖的python包
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")
ted_author=sys.argv[1]
ted_title=sys.argv[2]
url_tedscript=sys.argv[3]
file_output=sys.argv[4]
try:
    file_output_pointer=open(file_output,'w+')
except Exception:
    print("file "+file_output+" acquire some error!")
    exit
file_output_pointer.write('<!DOCTYPE html><html><head><title></title><link href="http://www.xuantianlinyu.com.cn/css/article.css" rel="stylesheet" type="text/css" /></head><body onclick="closeshowBos()"><meta charset="UTF-8"><div class="main3"><div class="left"><div style=" width:1px; height:1px; overflow:hidden;"></div><div class="sons" id="sonsyuanwen"><div class="cont">')
file_output_pointer.write('<h1 style="font-size:20px; line-height:22px; height:22px; margin-bottom:10px; text-align:center">'+str(ted_title)+'</h1>')
file_output_pointer.write('<p class="source" style="text-align:center"><a href="">'+ted_author+'</a></p>')
file_output_pointer.write('<div class="contson" id="contsonc7e28ca4629f">')
tedscript_request=requests.get(url_tedscript,timeout=30)
tedscript_soup=BeautifulSoup(tedscript_request.text,'html.parser')
for news in tedscript_soup.find_all('div',class_='flx-s:1'):
    if len(news)>0:
        file_output_pointer.write(str(news))
file_output_pointer.write('<div class="sons"><div class="contyishang"><div style="height:30px; font-weight:bold; font-size:16px; margin-bottom:10px; clear:both;"><h2><span style="float:left;"></span></h2><span id="shangxiPlay27057" style=" display:none;width:1px; height:1px; float:left;"></span></div><p></p></div></div></div></div></div></div></div></body></html>')
#由于不同网站html代码有差异，因此爬虫不同网站的代码需要单独编写
