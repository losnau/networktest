#-*- coding:utf-8
from flask import Flask,request,render_template,session,flash,redirect,url_for,abort,jsonify
from datetime import datetime
from flask_cors import *

from sys import path
from os.path import abspath
path.append(abspath('.')+'\db')
from sqlhelp import SqlHelp
sqlhelper = SqlHelp()
from selfconfig import *
from funct.checked import checkhost,savesourceaudit,sessions_login,requsets_login
from funct.checked import  Request
requester=Request()

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.update(dict(
    #开启了调试模式
    DEBUG=True,
    #配置了秘钥（一般这种在代码里显示配置秘钥的方式被认为是不安全的，实际当中更常用的方式是将秘钥放进服务器的一个环境变量中）
    SECRET_KEY='development key',
))
@app.route('/',methods=['GET','POST'])
def root():
    if not session.get('logged_in'):
        flash('请先登录')
        return redirect(url_for('login'))
    is_superuser = session.get('is_superuser')
    return render_template('index.html',is_superuser=is_superuser)

@app.route('/index',methods=['GET','POST'])
def index():
    if not session.get('logged_in'):
        flash('请先登录')
        return redirect(url_for('login'))
    is_superuser = session.get('is_superuser')
    return render_template('index.html',is_superuser=is_superuser)

@app.route('/login',methods=['GET','POST'])
def login():
    if  session.get('logged_in'):
        is_superuser = session.get('is_superuser')
        return render_template('index.html',is_superuser=is_superuser)
    if request.method == 'GET':

        return render_template('login.html')
    else:
        # userinfo=requester(request.form.get)
        # result = sqlhelper.checked(userinfo['username'], userinfo['password'], 'check')
        username = request.form.get('username')  # post请求模式，安排对象接收数据
        password = request.form.get('password')
        result=sqlhelper.checked(username, password, 'check')

        if result:
            # sessions_login(session)
            # requsets_login(request.form.get)
            # print(request.form.get)
            session['logged_in'] = True
            #session['username'] = userinfo['username']  # 利用session添加传回来的值username
            session['username'] = username
            session['userid'] = result[8] # 利用session添加传回来的值userid
            session['is_superuser'] = result[2] # 利用session添加传回来的值userid
            session.permanent = True  # 设置session过期的时间
            flash('You were logged in')
            return render_template('index.html',is_superuser=session['is_superuser'])
        else:
            return render_template('login.html', error='用户名或者密码错误')
@app.route('/index_content',methods=['GET','POST'])
def index_content():
    return render_template('index_v1.html', error='用户名或者密码错误')

@app.route('/api/<types>/<methods>',methods=['GET','POST'])
def managers(types,methods):
    conditions=source_data={}
    data = ''
    if not session.get('logged_in'):
        flash('请先登录')
        return redirect(url_for('login'))
    if types == 'source':
        if methods == 'add' or methods == 'save':
            conditions['sourcename'] = request.form.get('sourcename')
            conditions['sourceport'] = request.form.get('sourceport')
            conditions['sourceip'] = request.form.get('sourceip')
        if methods=='manager':
            data_all=sqlhelper.select('datasource')
            return render_template('tables/sourcemanage.html', data_all=data_all)
            return 'manager'
        elif methods=='add':
            if request.method == 'GET':
                return render_template('form/add_source.html')
            elif request.method == 'POST':
                conditions['id'] = sqlhelper.lastid('datasource')
                #print(conditions)
                result= sqlhelper.datasave('datasource',conditions)
                return  render_template('form/add_source.html',success='新增数据源名称'+conditions['sourcename']+',数据源地址:'+conditions['sourceport']+',数据源端口：'+conditions['sourceip'])
        elif methods == 'save':
            conditions['id'] = request.form.get('sourceid')
            app.logger.warn('sourcename:'+conditions['sourcename'] +',sourceip:'+conditions['sourceport']+',sourceport:'+conditions['sourceip'] +',sourceid:'+conditions['id'])
            result = sqlhelper.dataupdate('datasource', conditions)
            return 'test'
        elif methods == 'delete':
            sourceid = request.form.get('sourceid')
            app.logger.warn(sourceid)
            result = sqlhelper.datadelete('datasource', sourceid)
            return 'test'
        elif methods=='ping_telnet':
            data_all = sqlhelper.select('datasource')
            return render_template('tables/telnet_ping.html', data_all=data_all, no_ping_sourceip=no_ping_sourceip)
        elif methods=='checkpt':
            conditions['sourcename'] = request.form.get('sourcenam')
            conditions['host'] = request.form.get('host')
            conditions['port'] = request.form.get('port')
            conditions['sourceip'] = request.form.get('sourceip')
            conditions['temethod'] = request.form.get('temethod')
            sourceip = request.form.get('sourceip')
            if sourceip == 'C60A':
                source_data=c60a_remote_machine
            elif sourceip == 'C60B':
                source_data = c60b_remote_machine
            if sourceip != '' and conditions['temethod'] != '':
                data = checkhost(source_data['sourceip'], conditions['temethod'] , conditions['host'], conditions['port'], source_data['username'], source_data['password'])
                #两个字典合并了
                savesourceaudit(conditions, data['type'])
            return jsonify(data)
    elif types == 'audit':
        if methods == 'source_see':
            data_all = sqlhelper.select('sourceaudit')
            return render_template('tables/sourceaudit.html', data_all=data_all)
    elif types == 'prd':
        if methods=='status':
            if request.method == 'GET':
                return render_template('pro_network.html')
            elif request.method == 'POST':
                temethod=request.form.get('method')
                data=checkhost(te_source_data['sourceip'], temethod, prd_api['ip'], prd_api['port'], te_source_data['username'], te_source_data['password'])
                return jsonify(data)

    elif types == 'user':
        if methods == 'add' or methods == 'save':
            conditions['username'] = request.form.get('username')
            conditions['nickname'] = request.form.get('nickname')
            conditions['is_superuser'] = request.form.get('is_superuser')
            conditions['is_disabled'] = request.form.get('is_disabled')
        if methods=='manager':
            data_all = sqlhelper.select('userpd')
            return render_template('tables/usermanage.html', data_all=data_all)
        elif  methods=='add':
            if request.method == 'GET':
                return render_template('form/add_user.html')
            elif request.method == 'POST':
                dt = datetime.now()
                conditions['nowtime'] = dt.strftime('%Y/%m/%d %H:%M:%S')
                conditions['password'] = request.form.get('password')
                app.logger.warn(
                    'nickname:' + conditions['nickname'] + ',username:' + conditions['username']+ ',is_superuser:' + conditions['is_superuser'] + ',os_disabled :' + conditions['is_disabled'] )
                conditions['id'] = sqlhelper.lastid('userpd')
                result = sqlhelper.datasave('userpd',conditions)
                return  render_template('form/add_user.html',success='新增用户：'+conditions['nickname']+',登录名:'+conditions['username']+'新增时间'+conditions['nowtime'])
        elif methods == 'save':
            conditions['id'] = request.form.get('userid')
            app.logger.warn('nickname:'+conditions['nickname']+',username:'+conditions['username']+',is_superuser:'+ conditions['is_superuser']+',os_disabled :'+conditions['is_disabled'] +',userid:'+conditions['id'])
            result = sqlhelper.dataupdate('userpd', conditions)
            return 'success'
        elif methods == 'delete':
            userid = request.form.get('userid')
            result = sqlhelper.datadelete('userpd', userid)
            return 'test'
        elif methods == 'resetuserpd':
            if request.method == 'GET':
                userid=request.args.get('userid')
                app.logger.warn('resetuserpd------userid:'+userid)
                return render_template('form/userresetpd.html',userid=userid)
            elif request.method == 'POST':
                app.logger.warn('password:'+request.form.get('password')+',userid:'+request.form.get('userid'))
                sqlhelper.resetpd(request.form.get('password'),request.form.get('userid'))
                flash('你已成功修改密码')
                return redirect('api/user/manager')
        elif methods == 'logout':
            session.pop('logged_in', None)
            session.pop('username', None)
            flash('You were logged out')
            return redirect(url_for('login'))
        elif methods=='changepd':
            if request.method == 'GET':
                return render_template('form/changepd.html')
            elif request.method == 'POST':
                password = request.form.get('password')
                username = session.get('username')
                #保存修改的用户密码
                sqlhelper.checked(username, password, 'changepd')
                session.pop('logged_in', None)
                session.pop('us  ername', None)
                flash('你已成功修改密码')
                return redirect(url_for('login'))
        elif methods=='logout':
            session.pop('logged_in', None)
            session.pop('username', None)
            flash('You were logged out')
            return redirect(url_for('login'))

@app.errorhandler(500)
def page_not_found(error):
    return render_template('error_page/500.html'), 500

if __name__ == '__main__':
    app.run('0.0.0.0',19221,debug=True)
