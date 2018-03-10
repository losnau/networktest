from db.sqlhelp import SqlHelp
sqlhelper = SqlHelp()
result=sqlhelper.checked('lizuofang', '12345', 'check')
print(result)
# if result:
#     print('yes')
# else:
#     print('NO')
# from checked.checked import checkhost
#
# result=checkhost('192.168.19.222', 'ping', '8.8.8.8', '', 'root', 'Pass2010')
# print(result)
# from selfconfig import *
# print(c60a_remote_machine['user'])
# print(no_ping_sourceip)
a={'a':'a'}
b={'b':'b'}
print(dict(a,**b))