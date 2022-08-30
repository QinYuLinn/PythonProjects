import sys
file_input_argv=sys.argv[1]#从输入参数获取程序参数文件
try:
        file_pointer_data_read_argv=open(file_input_argv,'r')
except Exception:
        print("file "+file_input_argv+" does not exist!")
        exit#打开程序参数文件
file_source_data=[]
citekeys=[]#需要提取的文章的citekey
pickup_flag=1#程序参数文件第一行为程序读取的bib文件，后面几行时citekey
for eachline in file_pointer_data_read_argv.readlines():#获取csv文件每行中最多项数目
    if(pickup_flag==1):
        file_source_data=eachline.strip('\n')
        pickup_flag=2
    else:
        citekeys.append(eachline.strip('\n'))
#打开待处理的bib文件
try:
        file_pointer_data_read=open(file_source_data,'r')
except Exception:
        print("file "+file_source_data+" does not exist!")
        exit
text=file_pointer_data_read.read()#读取整个bib文件
items_list=text.split('@')#根据@字符对bib文件进行分解为多个小的文章条目
informations=["author","title","journal","year"]#需要提取的信息索引
informations_taken=[]#提取的信息储存的字符串
#三个临时变量
temp_str=[]
temp2=[]
temp=[]
#输出的字符串
text_output=""
#三个循环指标
iindex=0
jindex=0
kindex=0
lindex=0
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
            text_output=text_output+',"Reference","凝聚态物理"),'
text_output=text_output[:-1]
print(text_output)
file_pointer_data_read.close()
exit
