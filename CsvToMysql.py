import sys
file_source_data=sys.argv[1]#获取第一个输入参数作为输入文件
file_output_data=sys.argv[2]#获取第二个参数作为输出文件名称
#print(file_source_data)
#print(file_output_data)
#file_source_data="/Users/qinyulin/Desktop/Sheet.csv"
#file_output_data="/Users/qinyulin/Desktop/MysqlTableFormat.txt"
try:
        file_pointer_data_read=open(file_source_data,'r')
        file_pointer_data_write=open(file_output_data,'w')
except Exception:
        print("file "+file_source_data+" does not exist!")
        exit
index_set={0,1,2}
flag=1
text=""
for eachline in file_pointer_data_read.readlines():
    eachlinelist=eachline.split(',')
    colum_number=len(eachlinelist)
    break
file_pointer_data_read.seek(0)
for eachline in file_pointer_data_read.readlines():
    eachline=eachline.strip('\n')
    eachlinelist=eachline.split(',')
    if (flag==1):
        text=text+'('
    else:
        text=text+',('
    for index in range(0,colum_number):
        if (index in index_set):
            eachlinelist[index]='"'+eachlinelist[index]+'"'
        else:
            pass
        if index==0:
            text=text+eachlinelist[index]
        else:
            text=text+','+eachlinelist[index]
    text=text+')'
    flag=2
text=text+';'
file_pointer_data_write.write(text)
file_pointer_data_read.close()
file_pointer_data_write.close
print("transfer to mysql table format successfully!"+"\n"+"the datas are stored in"+'\t'+file_output_data+'\n')
exit
