import sqlite3
import os
class sqlitemanage():
    def __init__(self):
        self.dbconfig = {
            "filename" : "userpd.db",
            "filepath" : "../"
        }
        self.path = self.dbconfig['filepath']+self.dbconfig['filename']
        self.tables = ['datasource','sourceaudit','userpd']
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
    def dbselect(self,sql,nums):
        result=''
        if nums=='one':
            result = self.cursor.execute(sql).fetchone()
        elif nums == 'all':
            result = self.cursor.execute(sql).fetchall()
        return result
    def dbmg(self,sql):
        result = self.cursor.execute(sql)
        self.conn.commit()
        return result
    def closedb(self):
        self.conn.close()

