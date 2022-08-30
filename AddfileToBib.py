import sys
file_input_argv=sys.argv[1]
file_output_argv=sys.argv[2]
try:
        file_pointer_data_read_argv=open(file_input_argv,'r')
except Exception:
        print("file "+file_input_argv+" does not exist!")
        exit
Add_To_String='\n file      = {:/Library/WebServer/Documents/Jabref/RefPdf/'
try:
        file_pointer_data_write_argv=open(file_output_argv,'w')
except Exception:
        print("file "+file_output_argv+" does not exist!")
        exit


seperator="@"#csv文件的分隔符
text=file_pointer_data_read_argv.read()
text_each_item_list=text.split(seperator)

temp_string=[]
joint_string=','
modified_eachitem=[]
modified_text="@"
for eachitem in text_each_item_list:
    eachitem_list=eachitem.split(',')
    temp_string=eachitem_list[0][8:]
    temp_string=Add_To_String+temp_string+'.pdf:PDF}'
    eachitem_list.insert(1,temp_string)
    modified_eachitem=joint_string.join(eachitem_list)
    print(modified_eachitem)
    modified_text=modified_text+modified_eachitem+'@'
file_pointer_data_write_argv.write(modified_text)

