# datasource='''203.81.244.199,8511.8711,中胜数据源
# 59.151.33.214,80,天创数据源
# 59.151.33.215,80,天创备用数据源
# 43.243.130.44,9000,QY数据源
# 123.56.222.172,8443,掌通无极数据源
# 172.16.254.17,80,CMBCC据源
# 113.106.54.66,18080,电信数据源
# 140.205.174.76,80,高德数据源 旧
# 114.113.231.233,80,集奥数据源
# 219.143.253.204,80,国政通数据源
# 114.55.187.168,80,企查查数据源
# 111.198.162.10,8080,深圳联通数据源
# 172.16.254.9,7031,移动数据源
# 218.205.68.67,8000,浙江移动
# 58.213.97.45,443,天翼征信数据源
# 106.11.93.17,80,高德新IP地址
# 106.11.12.1,80,高德新IP地址
# 106.11.208.1,80,高德新IP地址
# 106.11.132.13,80,高德新IP地址
# 106.11.208.26,80,高德新IP地址
# 172.16.254.9,7031,移动集团
# 172.16.254.10,21,移动集团
# 172.16.254.17,,招行数据源
# 172.16.254.23,80,集奥聚合
# 172.16.254.25,82,招联数据'''
#
# import sqlite3
# conn=sqlite3.connect(r'./userpd.db')
# cursor=conn.cursor()
# sql='''create table datasource(
# sourcename text,
# sourceip text,
# sourceport text,
# id int)
# '''
# cursor.execute(sql)
# conn.commit()
# temp=0
# for i in datasource.split('\n'):
#     sourceip=i.split(',')[0]
#     sourceport=i.split(',')[1]
#     sourcename = i.split(',')[2]
#     sql=''' insert into datasource(sourcename,sourceip,sourceport,id)
#  VALUES (:st_sourcename,:st_sourceip,:st_sourceport,:st_id)
#     '''
#     cursor.execute(sql,{'st_sourcename':sourcename,'st_sourceip':sourceip,'st_sourceport':sourceport,'st_id':temp})
#     temp=temp+1
# # sql='drop table datasource'
# # cursor.execute(sql)
# conn.commit()
# cursor.close()