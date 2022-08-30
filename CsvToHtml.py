import sys
file_source_data=sys.argv[1]
file_output_data=sys.argv[2]
try:
        file_pointer_data_read=open(file_source_data,'r')
        file_pointer_data_write=open(file_output_data,'w')
except Exception:
        print("file "+file_source_data+" does not exist!")
        exit
flag=1#测试脚本时的一个控制变量
seperator=","#csv文件的分隔符
front_content="<!DOCTYPE HTML>\n"+"<html>\n"+"<head>\n"+'<meta charset="UTF-8">\n'+' <link rel="stylesheet" href="http://www.xuantianlinyu.com.cn/css/index.css">\n'+'<link href="http://www.xuantianlinyu.com.cn/css/styles-global.css" type="text/css" rel="stylesheet" />\n'+'<link href="http://www.xuantianlinyu.com.cn/css/table-concerned.css" type="text/css" rel="stylesheet" />\n'+'</head>\n'+'<body>\n'+'<div class="container_12 clearfix">\n'+'<div class="main grid_12">\n'+'<table class="styled-table">\n'
tail_content='</tbody>\n'+'</table>\n'+'</div>\n</div>\n'+'</tbody>\n'+'</html>\n'#表格每行最后添加的字符串，当为\hline时表示完全表格
text=front_content
index_viarable=0
colum_number=0
eachline=file_pointer_data_read.readline()#获取csv文件每行中最多项数目
eachline2=eachline.strip('\n')
eachlinelist=eachline2.split(seperator)
colum_number_current=len(eachlinelist)
colum_number=colum_number_current
text=text+"<thead><tr>"
if (colum_number_current>0):
    for index_viarable in range(0,colum_number):
        text=text+"<th>"+eachlinelist[index_viarable]+"</th>"+"\n"
else:
    pass
    text=text+"</thead>"+'\n'
text=text+"<tbody>"
if (flag):
    for eachline in file_pointer_data_read.readlines():
        eachline2=eachline.strip('\n')
        eachlinelist=eachline2.split(seperator)
        colum_number_current=len(eachlinelist)
        text=text+"<tr>"
        if (colum_number_current>0):
            for index_viarable in range(0,colum_number):
                    text=text+"<td>"+eachlinelist[index_viarable]+"</td>"+"\n"
            text=text+"</tr>"+'\n'
        else:
            pass
    text=text+tail_content
    file_pointer_data_write.write(text)
    print("transfer to tex table format successfully!"+"\n"+"the datas are stored in"+'\t'+file_output_data+'\n')
file_pointer_data_read.close()
file_pointer_data_write.close
exit
