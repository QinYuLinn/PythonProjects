import sys
import requests
from bs4 import BeautifulSoup #导入程序运行所依赖的python包
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")
url_iqiyi="https://www.iqiyi.com/dianying/?vfrm=pcw_home&vfrmblk=C&vfrmrst=712211_channel_dianying"
url_tencent="https://v.qq.com/channel/movie"
filename="/Users/qinyulin/PythonProjects/Works/IqiyiFilmsContent.txt"
filepointer=open(filename,'r+')
film_exists_set=set()
for exists in filepointer.readlines():
    film_exists_set.add(exists)#将文件中保存的新的已经上线的电影信息储存在变量中
url_default_part="https://"
iqiyi_request=requests.get(url_iqiyi,timeout=30)
iqiyi_soup=BeautifulSoup(iqiyi_request.text,'html.parser')
for news in iqiyi_soup.find_all('a',class_='img-link'):
    if len(news)>0:
        title=str(news.get('data-indexfocus-currenttitleelem'))
        if (title+'\n') in film_exists_set:#如果电影已经爬虫保存过就忽略
            continue
        else:               #没有保存过的电影信息打印出来并将电影名称添加到文件中
            film_exists_set.add((title+'\n'))
            link=str(news.get('href'))
            intro=str(news.get('data-indexfocus-description'))
            if (url_default_part in link):
                link=link
            else:
                link=link.replace('//','https://')
            print('film name:'+title)
            print('film link:'+'\t'+link)
            print('film intro:'+'\t'+intro+'\n')
#由于不同网站html代码有差异，因此爬虫不同网站的代码需要单独编写
tencent_request = requests.get(url_tencent,timeout=30)#输入字节流，解决编码问题
tencent_soup = BeautifulSoup(tencent_request.content,'html.parser')
tencent_target_div=tencent_soup.find('div',id='movie_v3_new')
for news in tencent_target_div.find_all('a',class_='figure_title'):
    if len(news)>0:
        title=str(news.get('title'))
        if (title+'\n') in film_exists_set:
            continue
        else:
            film_exists_set.add((title+'\n'))
            link=str(news.get('href'))
            if (url_default_part in link):
                link=link
            else:
                link=link.replace('//','https://')
            print('film name:'+title)
            print('film link:'+'\t'+link+'\n')
filepointer.seek(0)#将文件指针重置到文件开头以将保存电影名称的变量输出到文件
for exists in film_exists_set:
    filepointer.write(exists)
filepointer.close()
