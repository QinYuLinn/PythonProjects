import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='BookStoreSchema',
                                         user='root',
                                         password='QYLQYL20142017')
    if connection.is_connected():
        sql_query="select name,author,press from Books where class='物理学'"
        cursor = connection.cursor()
        cursor.execute(sql_query)
        record = cursor.fetchall()
        print("书名\t作者\t出版社\n")
        for rows in record:
            print(rows[0]+'\t'+rows[1]+'\t'+rows[2]+'\n')
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
