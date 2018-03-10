# import socket
# sk=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     sk.connect(('192.168.0.1', 21))
#     print('Server port 21 OK!')
# except Exception:
#     print('Server port 21 not connect!')
# sk.close()

import paramiko
import telnetlib,os
def checkhostport(host , port):
    try:
        tn=telnetlib.Telnet(host,port,timeout=3)
    except:
        print('端口不可用')
    else:
        print('端口可用')
def checkhost(host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect('192.168.19.222', 22, 'root', 'Pass2010')
    stdin,stout,stderr=ssh.exec_command('/bin/ping '+host+' -c 3 -W 1')
    print(stout.read().decode('utf-8'))
    ssh.close()
checkhostport('192.168.19.222',999)
checkhost('140.205.174.76')

