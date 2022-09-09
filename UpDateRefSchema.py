import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")
import mysql.connector
from mysql.connector import Error
file_input_argv=sys.argv[1]
database_class=sys.argv[2]
try:
        file_pointer_data_read=open(file_input_argv,'r')
except Exception:
        print("file "+file_input_argv+" does not exist!")
        exit#打开程序参数文件
text=file_pointer_data_read.read()#读取整个bib文件
items_list=text.split('@')#根据@字符对bib文件进行分解为多个小的文章条目

#四个循环指标
iindex=0
jindex=0
kindex=0
lindex=0
#三个临时变量
temp_str=[]
temp=[]
temp1=[]
temp2=[]

print("fetching all the items in jabref........")
citekeys_jabref=[]#所有条目的citekey
for iindex in range(1,len(items_list)-1):#循环遍历每个文章条目
    temp1=items_list[iindex].split(',')
    temp2=temp1[0].split('{')
    citekeys_jabref.append(temp2[1])

print("fetching all the corresponding items in database........")
citekeys_database=[]
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='RefSchema',
                                         user='root',
                                         password='QYLQYL20142017',autocommit=True,auth_plugin='mysql_native_password')
    if connection.is_connected():
        sql_query="select citationkey from reference where class='"+database_class+"';"
        cursor = connection.cursor()
        cursor.execute(sql_query)
        record = cursor.fetchall()
        for rows in record:
            citekeys_database.append(rows[0])
            
        citekeys=[]#需要向数据库添加的条目的citekey
        for temp in citekeys_jabref:
            if (temp not in citekeys_database):
                citekeys.append(temp)
        print("there are "+str(len(citekeys))+" new items need to be add:\n")
        for temp in citekeys:
            print(temp)
        print('\n')
        if(len(citekeys)>0):
            print("constructing the sql to add these new items.......")
            informations=["author","title","journal","year"]#需要提取的信息索引
            informations_taken=[]#提取的信息储存的字符串
            #输出的字符串
            text_output=""
            #数据库插入操作语句
            text_output=text_output+'INSERT INTO reference VALUES'
            #从bib文件中提取信息
            for iindex in range(0,len(items_list)):#循环遍历每个文章条目
                for jindex in range(0,len(citekeys)):#循环遍历每个citekey
                    if(citekeys[jindex] in items_list[iindex]):#如果citekey与文章条目匹配，首先输出citekey
                        text_output=text_output+'("'+citekeys[jindex]+'"'
                        temp_str=items_list[iindex].split(',\n')
                        for kindex in range(0,len(informations)):#然后在从文章条目里面提取特定的信息
                            for lindex in range(0,len(temp_str)):#循环遍历单个文章条目的每行
                                if(informations[kindex] in temp_str[lindex]):#如果匹配上需要提取的信息就保存
                                    temp2=temp_str[lindex].split('{')
                                    temp=temp2[1].split('}')
                                    text_output=text_output+',"'+temp[0]+'"'
                        text_output=text_output+',"Reference","'+database_class+'"),'
            text_output=text_output[:-1]
            text_output=text_output+";"
            print(text_output)
            print("executing the sql sentence to insert these new items......")
            cursor.execute(text_output)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed!\n Done!")
file_pointer_data_read.close
exit
