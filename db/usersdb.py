import sqlite3
from datetime import datetime
dt = datetime.now()

#昵称、创建时间、更新时间
sql='''create table userpd(
username text,
password text,
is_superuser int,
is_disabled int,
nickname text,
createtime text,
updatetime text,
lastlogin text,
id int)
'''
conn = sqlite3.connect(r'./userpd.db')
cursor = conn.cursor()
cursor.execute(sql)
a=[['lingkangzhi','lingkangzhi',0,1,'凌康志'],['huzhao','huzhao',0,1,'胡钊'],['zhouxian','zhouxian',0,1,'周贤'],['fusheng','fusheng',0,1,'符昇'],['tanyutao','tanyutao',0,1,'谭宇涛'],
   ['chenpuchuang','chenpuchuang',1,1,'陈普创'],['chenhongyu','chenhongyu',1,1,'陈洪宇'],['liutao','liutao',1,1,'刘涛'],['huguanglong','huguanglong',1,1,'胡广龙'],['lizuofang','lizuofang',1,1,'李作芳']]
temp=0
for i in a:

    sql=''' insert into userpd(username,password,is_superuser,is_disabled,nickname,createtime,updatetime,lastlogin,id)
 VALUES (:st_username,:st_password,:st_supperuser,:st_disabled,:st_nickname,:st_createtime,:st_updatetime,:st_lastlogin,:st_id)
    '''
    now=dt.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(sql,{'st_username':i[0],'st_password':i[1],'st_supperuser':i[2],'st_disabled':i[3],'st_nickname':i[4],'st_createtime':now,'st_updatetime':now,'st_lastlogin':now,'st_id':temp})
    temp=temp+1
conn.commit()
# sql='''select * from  userpd'''
# results=cursor.execute(sql).fetchall()
# for i in results:
#     print(i)
# sql="select * from userpd where username="+username+" and password="+password
# sql="select * from userpd where username='{}' and password='{}'".format(username,password)
# print(sql)
# result=cursor.execute(sql).fetchall()
# print(result)
#

