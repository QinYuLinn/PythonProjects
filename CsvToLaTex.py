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
tail_content="\hline"#表格每行最后添加的字符串，当为\hline时表示完全表格
space_fill_string="null"#表格中有空的数据项时用此字符填充
text="\hline"+'\n'#三线表固定格式
index_viarable=0
colum_number=0
for eachline in file_pointer_data_read.readlines():#获取csv文件每行中最多项数目
    eachlinelist=eachline.split(seperator)
    colum_number=len(eachlinelist)
    break
file_pointer_data_read.seek(0)
if (flag):
    for eachline in file_pointer_data_read.readlines():
        eachline2=eachline.strip('\n')
        eachlinelist=eachline2.split(seperator)
        colum_number_current=len(eachlinelist)
        if (colum_number_current>0):
            text=text+eachlinelist[0]
            for index_viarable in range(1,colum_number):
                if (index_viarable<colum_number_current):
                    text=text+'&'+eachlinelist[index_viarable]
                else:
                    text=text+('&'+space_fill_string)*(colum_number-colum_number_current-1)+'&'
                    break
            text=text+"\\"+"\\"+tail_content+'\n'
        else:
            pass
    text=text+"\hline"
    file_pointer_data_write.write(text)
    print("transfer to tex table format successfully!"+"\n"+"the datas are stored in"+'\t'+file_output_data+'\n')
file_pointer_data_read.close()
file_pointer_data_write.close
exit
