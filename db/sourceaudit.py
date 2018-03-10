import sqlite3
conn=sqlite3.connect(r'./userpd.db')
cursor=conn.cursor()

sql='''create table sourceaudit(
sourcename text,
sourceip text,
sourceport text,
types text,
username text,
datetimes text,
status text,
id int)
'''
cursor.execute(sql)
conn.commit()
cursor.close()