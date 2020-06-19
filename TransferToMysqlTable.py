file_source_data="/Users/qinyulin/Desktop/11.csv"
file_output_data="/Users/qinyulin/MySQL/Databases/MysqlTableFormat.txt"
try:
        file_pointer_data_read=open(file_source_data,'r')
        file_pointer_data_write=open(file_output_data,'w')
except Exception:
        print("file "+file_source_data+" does not exist!")
        exit
index_set={0,1,2,3,5}
flag=1
text=""
for eachline in file_pointer_data_read.readlines():
    eachlinelist=eachline.split(',')
    colum_number=len(eachlinelist)
    break
file_pointer_data_read.seek(0)
for eachline in file_pointer_data_read.readlines():
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
