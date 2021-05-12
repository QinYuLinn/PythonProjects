file_source_data="/Users/qinyulin/JabRef/Ref.bib"
try:
        file_pointer_data_read=open(file_source_data,'r')
        file_pointer_data_write=open(file_output_data,'w')
except Exception:
        print("file "+file_source_data+" does not exist!")
        exit
text=file_pointer_data_read.read()
items_list=text.split('@')
citekeys=["Dudek1984p61p91"]
informations=["author","title","journal","year"]
informations_taken=[]
temp_str=[]
temp2=[]
temp=[]
text_output=""
iindex=0
jindex=0
kindex=0
lindex=0
for iindex in range(0,len(items_list)):
    for jindex in range(0,len(citekeys)):
        if(citekeys[jindex] in items_list[iindex]):
            text_output=text_output+'("'+citekeys[jindex]+'"'
            temp_str=items_list[iindex].split(',\n')
            for kindex in range(0,len(informations)):
                for lindex in range(0,len(temp_str)):
                    if(informations[kindex] in temp_str[lindex]):
                        temp2=temp_str[lindex].split('{')
                        temp=temp2[1].split('}')
                        text_output=text_output+',"'+temp[0]+'"'
            text_output=text_output+',"Ref"),'
text_output=text_output[:-1]
print(text_output)
file_pointer_data_read.close()
exit
