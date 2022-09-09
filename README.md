In this reposity, there are some python projects which make my personal life easier.

CsvToMysql.py script just as its name shows, it transfer csv file to mysql insert format so that we can easily tranfer a table into a mysql table.Besides, TxtToMysql.py is similar to this script.调用格式为:
    python3 CsvToMysql.py input.csv output.sql

CsvToLaTex.py transfer csv file to latex souce code of inserting a table which make sure that one can easily migrate a table to latex table easily.
    python3 CsvToLatex.py input.csv output.tex

CsvToHtml.py  transfer csv file to html souce code of inserting a table which make sure that one can easily migrate a table to html table easily,besides, the table format in html is precontroled by the css file in my website www.xuantianlinyu.com.cn
    python3 CsvToHtml.py input.csv output.html

TxtToHtml.py transfer txt file to html souce code of showing an article which make sure that one can easily migrate a plain tex to a readable html page easily.
    python3 TxtToHtml.py 题目 作者 input.txt output.tml

TedScriptScrapy.py scrapy the subscript in ted official website www.ted.com,which one can easily get the manuscript for such ted speeches and learn these speeches more deeply.
    python3 TedScriptScrapy.py 题目 作者 script_url output.html

ExtraxtFromBib.py extract specific information in bib file and transfer these information to mysql sql expression so that one can insert  these infortion in the database which can be used in my website. Moreover ,ExtraFromBibInputArgv.txt is the inputing angvs for this script.
    python3 ExtraxtFromBib.py ExtraFromBibInputArgv.txt

TestPythonMysql.py is a test script for the mysql
    python3 TestPythonMysql.py

DeleteRowNumbers.py delete the row number of a file(for example the file created using vim editor which contain the row number).
    python3 DeleteRowNumbers.py input_file output_file

GaussLagueree.py is a mathmatica script for using the guass integratin in python,it's output is the coefficienct of guass-lagueree integration
    python3 GaussLagueree.py

BasicQuantity.py is a physical script to get some basic quantity in physics, such as the Boltizaman constant,etc.
    python3 BasicQuantity.py

ListFilms.py scrapy the iqiyi website for new films and its play url,the IqiyiFilmsContent.txt file is a recored file for the history scrapy.
    python3 ListFilms.py

BillardsAngle.py is a script for calculate the potting angle for different postion shot in snooker.

UpDateRefSchema.py is a script to add the ref in my jabref to the database RefSchema
    python3 UpDateRefSchema.py input.bib 插入数据库的文章分类名称


