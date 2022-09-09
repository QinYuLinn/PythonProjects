import sys
file_source_data=sys.argv[1]
file_output_data=sys.argv[2]
try:
        file_pointer_data_read=open(file_source_data,'r')
        file_pointer_data_write=open(file_output_data,'w')
except Exception:
        print("file "+file_source_data+" does not exist!")
        exit
flag=1
text=""
str=" "
file_pointer_data_read.seek(0)
if (flag):
    for eachline in file_pointer_data_read.readlines():
        eachlinelist=eachline.split(' ')
        eachlinelist.pop(0)
        eachline=str.join(eachlinelist)
        text=text+eachline
    file_pointer_data_write.write(text)
    print("transfer to mysql table format successfully!"+"\n"+"the datas are stored in"+'\t'+file_output_data+'\n')
file_pointer_data_read.close()
file_pointer_data_write.close()
exit
