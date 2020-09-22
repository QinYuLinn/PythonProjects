file_source_data="/Users/qinyulin/MySQL/books.csv"
file_output_data="/Users/qinyulin/MySQL/books2.csv"
try:
        file_pointer_data_read=open(file_source_data,'r')
        file_pointer_data_write=open(file_output_data,'w')
except Exception:
        print("file "+file_source_data+" does not exist!")
        exit
cut_off_rate=0.4
flag=1
text=""
for eachline in file_pointer_data_read.readlines():
    eachlinelist=eachline.split(',')
    colum_number=len(eachlinelist)
    break
file_pointer_data_read.seek(0)
if (flag):
    for eachline in file_pointer_data_read.readlines():
        eachline2=eachline.strip('\n')
        eachlinelist=eachline2.split(',')
        new_price=round(float(eachlinelist[colum_number-1])*cut_off_rate)
        text=text+eachline2+','+str(new_price)+'\n'
    file_pointer_data_write.write(text)
    print("transfer to mysql table format successfully!"+"\n"+"the datas are stored in"+'\t'+file_output_data+'\n')
file_pointer_data_read.close()
file_pointer_data_write.close
exit
