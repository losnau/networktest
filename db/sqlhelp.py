from sqlite3 import dbapi2 as sqlite3
from datetime import datetime
import logging
import os
class SqlHelp():
    def __init__(self):
        self.conn=sqlite3.connect(r'E:\py36\flaskr\networktest\networktest\db\userpd.db',check_same_thread=False)
        self.cursor=self.conn.cursor()
    '''
    查询表，并且返回所有数据
    '''
    def select(self,tablename):
        sql = "select * from '{}'".format(tablename)
        result = self.cursor.execute(sql).fetchall()
        return result
    '''
    查询表，并且返回表中的最后一个id
    '''
    def all_counts(self,tablename):
        sql = "select count(*) from '{}' ".format(tablename)
        data=self.cursor.execute(sql).fetchall()
        count = data[0][0]
        return count
    '''
    查询表，返回表中id最后一个
    '''
    def lastid(self,tablename):
        sql = "select id from  '{}' ORDER BY id desc limit 1;".format(tablename)
        result = self.cursor.execute(sql).fetchone()
        id = int(result[0]) + 1
        return id
    '''
    用户检查和修改函数
    '''
    def checked(self,username, password, method):
        if method == 'check':
            sql = "select * from userpd where username='{}' and password='{}'".format(username, password)
            # print(sql)
            result = self.cursor.execute(sql).fetchone()
            return result
        elif method == 'changepd':
            sql = "update userpd set password='{}' WHERE username='{}'".format(password, username)
            # print(sql)
            result = self.cursor.execute(sql)
            self.conn.commit()
            return result
    '''
    数据源测试保存
    '''
    def savesourceaudit(self,username,sourcename, host, port, types, status):
        dt = datetime.now()
        datetimes = dt.strftime('%Y/%m/%d %H:%M:%S')
        sql = 'select count(*) from sourceaudit '
        ids = self.cursor.execute(sql).fetchall()
        sql = "insert into sourceaudit(sourcename,sourceip,sourceport,types,username,datetimes,status,id) VALUES ('{}','{}','{}','{}','{}','{}','{}',{})".format(
            sourcename, host, port, types, username, datetimes, status, ids[0][0])
        self.cursor.execute(sql)
        self.conn.commit()
    '''
    数据新增
    conditions的格式是个字典。类似self.params
    :param count:
    :param conditions:
    :return:
    '''
    def datasave(self,tablename,conditions=None):
        dt = datetime.now()
        datetimes = dt.strftime('%Y/%m/%d %H:%M:%S')
        if tablename=='datasource':
            sql = "insert into datasource(sourcename,sourceip,sourceport,id) VALUES ('{}','{}','{}',{})".format(conditions['sourcename'],conditions['sourceip'],
                                                                                                                conditions['sourceport'],conditions['id'])

        elif tablename == 'userpd':
            sql = "insert into userpd(username,password,is_superuser,is_disabled,nickname,createtime,updatetime,lastlogin,id) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                conditions['username'],conditions['password'],conditions['is_superuser'],conditions['nickname'],conditions['is_disabled'],conditions['nowtime'],conditions['nowtime'],conditions['nowtime'],conditions['id']
            )
        elif tablename == 'sourceaudit':
            sql = "insert into sourceaudit(sourcename,sourceip,sourceport,types,username,datetimes,status,id) VALUES ('{}','{}','{}','{}','{}','{}','{}',{})".format(
                conditions['sourcename'], conditions['host'], conditions['port'], conditions['types'], conditions['username'], datetimes, conditions['status'], conditions['id'])

        self.cursor.execute(sql)
        self.conn.commit()
        return True
    '''
    数据更新
    conditions的格式是个字典。类似self.params
    :param count:
    :param conditions:
    :return:
    '''
    def dataupdate(self,tablename,conditions=None):
        if tablename=='datasource':
            sql = "update  datasource  set sourcename='{}',sourceip='{}',sourceport='{}' where id={}".format(conditions['sourcename'], conditions['sourceip'],
                                                                                                           conditions['sourceport'], conditions['id'])
        elif tablename == 'userdb':
            sql = "update  userpd  set nickname='{}',username='{}',is_superuser='{}',is_disabled ='{}' where id ={}".format(
                conditions['nickname'], conditions['username'], conditions['is_superuser'], conditions['is_disabled'], conditions['id'])
        self.cursor.execute(sql)
        self.conn.commit()
        return True
    '''
    删除记录
    :id:每条记录的唯一识别
    :return:
    '''
    def datadelete(self,tablename,id=None):
        if tablename=='datasource':
            sql = "delete from datasource where id ={}".format(id)
        elif tablename == 'userdb':
            sql = "delete from  where id ={}".format(id)
        self.conn.commit()
        return True
    def resetpd(self,id,password):
        '''
        重置用户密码
        :id:每条记录的唯一识别
        :return:
        '''
        sql = "update userpd set password='{}' where id ={}".format(password, id)
        self.cursor.execute(sql)
        self.conn.commit()