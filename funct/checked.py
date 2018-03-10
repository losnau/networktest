import paramiko
import requests
from sys import path
from os.path import abspath
path.append(abspath('..')+'\db')

from sqlhelp import SqlHelp
sqlhelper = SqlHelp()
requests.packages.urllib3.disable_warnings()
class Session():
    def __init__(self):
        self.a=1
    '''
    session是一个字段，类似于
    session={'username':'lizuofang','password':'lizuofang'}
    '''
    def login(self,sessions,session):
        session=sessions['userid']
        return session
class Request():
    def __init__(self):
        self.a=1
    def userlogin(self,request):
        vadictions={}
        vadictions['username']=request('username')
        vadictions['password'] = request('password')
        return vadictions

def sessions_login(session):
    print(session['userid'])
    print(session)
def requsets_login(argvs):
    print(argvs('password'))
    print(argvs('username'))
def savesourceaudit(conditions=None,status=None):
    conditions['id']=sqlhelper.lastid('sourceaudit')
    conditions['status']=status
    sqlhelper.datasave('sourceaudit',conditions)
def checkhost(sourceip,temethod,host,port,username,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(sourceip, 22, username, password)
    title=content=retype=''
    stdin=stout=stderr=''
    print(temethod)
    if temethod == 'ping':
        title='Ping测试结果'
        stdin,stout,stderr=ssh.exec_command('/bin/ping '+host+' -c 3 -W 1')
        content = stout.read().decode('utf-8')
        status=stout.channel.recv_exit_status()
        if status == 0:
            retype = 'success'
        else:
            retype = "error"
    elif temethod == 'telnet' or temethod=='nc':
        if temethod=='nc':
            title='NC测试结果'
        elif temethod=='telnet':
            title = 'Telnet测试结果'

        stdin, stout, stderr = ssh.exec_command('/usr/bin/nc -z -w 2  -v '+host +' '+port)
        status = stout.channel.recv_exit_status()
        if status==0:
            content = stout.read().decode('utf-8')
            retype='success'
        else:
            content = stderr.read().decode('utf-8')
            retype = "error"
    elif temethod == 'request':
        title = 'requests测试结果'
        try:
            response = requests.get('https://103.243.255.241:9443/queryData/', verify=False,timeout=2)
            content = '状态码:' + response.status_code + '\n返回内容：' + response.content.decode('utf-8')
            if response.status_code == 200:
                retype = 'success'
            else:
                retype = 'error'
        except:
            retype = 'error'
            content = '网络不通'
    data = {
        'title': title,
        'content': content,
        'type': retype
    }
    ssh.close()
    return data
if __name__ == '__main__':
    a={'a':'a'}
    savesourceaudit(a, 2)