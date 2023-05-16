import pandas as pd
#pip install pymysql
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='shop')
curs = conn.cursor(pymysql.cursors.DictCursor)

# excel file load
excel_sheet_1 = pd.read_excel('D:\모음\python\pythonwork\input\\nation.xlsx', sheet_name = 'nation')
excel_sheet_2 = pd.read_excel('D:\모음\python\pythonwork\input\\nation.xlsx', sheet_name = 'city')

# db truncate tables
sql_truncate_1 = 'truncate table shop.nation'
sql_truncate_2 = 'truncate table shop.city'

curs.execute(sql_truncate_1)
curs.execute(sql_truncate_2)
conn.commit()

# data insert to db
sql_insert_1 = 'insert into shop.nation values(%s, %s, %s)'
for idx in range(len(excel_sheet_1)):
    	curs.execute(sql_insert_1, tuple(excel_sheet_1.values[idx]))
conn.commit()

sql_insert_2 = 'insert into shop.city values(%s, %s, %s)'
for idx in range(len(excel_sheet_2)):
    	curs.execute(sql_insert_2, tuple(excel_sheet_2.values[idx]))
conn.commit()

