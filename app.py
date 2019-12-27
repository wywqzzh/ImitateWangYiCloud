from flask import Flask, render_template, url_for, request, redirect,session,make_response,Response
from service.song import Logic_Song
from tools.tools import getJsonByPath
from sqlalchemy import BIGINT
import os
import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
from controller.songController import songController
from controller.usersController import usersController
from controller.leaderboardController import leaderboardController

app.config['SECRET_KEY'] = os.urandom(24)


# 主页
@app.route('/hello_world/')
def hello_world():
    username = session.get('username')
    controller = leaderboardController()
    args = controller.Leaderboard()
    if username != None:
        return render_template('home.html', username=username, args=args)
    else:
        return render_template('home.html', username='', args=args)


# 音乐播放
@app.route('/playerDeal/<int:id>/<Type>/')
def playerDeal(id, Type):
    index = request.args.get('index');
    if (Type == 'SONG'):
        controller = songController()
        if id == 1:
            id = request.args.get('ID')
        args = controller.getWordsSnamesVnamesBySid([id])
        args.update({"index": index})
        args.update({"SIDS": [id]})
        return render_template("player.html", args=args);
    elif (Type == 'ALBUM' or Type == 'LIST'):
        controller = songController()
        args = controller.getWordsSnamesVnamesByAid(id, Type)
        args.update({"index": index})
        return render_template("player.html", args=args);


# 歌单专辑显示
@app.route('/AlbumAndList/<int:id>/<type>/')
def AlbumAndList(id, type):
    controller = songController()
    ID = request.args.get('id');
    if id == 0:
        id = ID
    isUser = request.cookies.get('isUser')
    args = controller.getAlbumAndListMessageByAid(id, type)
    username=session.get('username')
    return render_template("AlbumAndList.html",id=id, type=type, args=args)




@app.route("/login/")
def login():
    return render_template('login.html', error='')


# 登录事件处理
@app.route("/loginInterpretation/", methods=['POST', 'GET'])
def loginInterpretation():
    ID = request.form.get('username')
    PASSWORD = request.form.get('password')
    controller = usersController()
    flag, username, UTYPE, Prohibit = controller.loginSuccess(ID, PASSWORD)
    if ID == None or not flag:
        error = '用户名或密码错误'
        return render_template("login.html", error=error)
    if Prohibit == 1:
        error = '很抱歉你的账户违反了相关规定,已被冻结'
        return render_template("login.html", error=error)
    session['uid'] = ID
    session['username']=username
    outdate = datetime.datetime.today() + datetime.timedelta(days=30)

    if UTYPE == 0:
        resp = make_response(redirect(url_for('hello_world')))
        resp.set_cookie('username', username, expires=outdate)
        return resp
    else:
        resp = make_response(redirect(url_for('manageUser')))
        resp.set_cookie('username', username, expires=outdate)
        return resp


# 注册
@app.route('/register/', methods=['post', 'get'])
def register():
    return render_template('register.html');


# 注册事件处理
@app.route('/registerInterpretation/', methods=['POST', 'GET'])
def registerInterpretation():
    userID = request.form.get('username')
    nickname = request.form.get('nickname')
    password = request.form.get('password')
    problem = request.form.get('problem')
    answer = request.form.get('answer')
    controller = usersController()
    if userID == None:
        return render_template('register.html')
    if controller.isExist(userID):
        return render_template('register.html', error='该手机号已注册')
    if controller.usernameIsExist(nickname):
        return render_template('register.html', error='用户名已存在')
    else:
        controller.addUser(userID, nickname, password, problem, answer)
    return redirect(url_for('login'))


# 搜索测试
@app.route('/search/')
def search():
    controller = songController()
    args = controller.fuzzyQuerySongs('张杰')
    key = "张杰"
    return render_template('search.html', key=key, args=args)


# 搜索事件处理
@app.route('/searchInterpretation/', methods=['GET', 'POST'])
def searchInterpretation():
    s = request.form.get('search')
    controller = songController()
    args = controller.fuzzyQuerySongs(s)
    username = session.get('username')
    return render_template('search.html', type='SONG', key=s, args=args)


# 歌曲播放量处理
@app.route('/BehindMethod/', methods=['GET', 'POST'])
def BehindMethod():
    id = request.args.get('id')
    controller = leaderboardController()
    controller.setPlayMessage(id)
    data = {
        's': 1
    }
    return data


# 我的音乐
@app.route('/mymusic/')
def mymusic():
    username = session.get('username')
    uid=session.get('uid')
    if username == ''or username==None:
        return redirect('/login/')
    controller = usersController()
    args = controller.giveUserListMessage(uid)
    return render_template('mymusic.html', args=args)


# 热门推荐
@app.route('/playlist/', methods=['post', 'get'])
def playlist():
    username=session.get('username')
    controller = songController()
    style = request.form.get('style')
    if style == '' or style == None:
        style = '全部'
    print(style)
    args = controller.recommendListAndList(style)
    return render_template('playlist.html', args=args)


@app.route('/selectList/', methods=['post', 'get'])
def selectList():
    if request.method == 'GET':
        pass
    id = request.args.get('id')
    return render_template('selectList.html', id=id)


@app.route('/getMylist/', methods=['post', 'get'])
def getMylist():
    username=session.get('username')
    uid=session.get('uid')
    if username == None or username == '' or len(username) == 0:
        data = {
            'suc': 0
        }
        return data
    else:
        userscontroller = usersController()
        data = userscontroller.giveUserListMessage(uid)
        data.update({'suc': 1})
        return data


@app.route('/addMusic/', methods=['post', 'get'])
def addMusic():
    sid = request.args.get('sid')
    lid = request.args.get('lid')
    userscontroller = usersController()
    flag = userscontroller.addSongToUserList(sid, lid)
    if flag:
        data = {
            'flag': 1
        }
    else:
        data = {
            'flag': 0
        }
    return data


@app.route('/deleteMusic/', methods=['post', 'get'])
def deleteMusic():
    sid = request.args.get('sid')
    lid = request.args.get('lid')
    userscontroller = usersController()
    userscontroller.deleteSongList(sid, lid)
    data = {
        'flag': 1
    }
    return data


@app.route('/manageUser/')
def manageUser():
    controller = usersController()
    username = session.get('username');
    args = controller.getAllUserMessage(username)
    return render_template('Manage.html', args=args)


@app.route('/setAdminOrUser/', methods=['post', 'get'])
def setAdminOrUser():
    data = request.values
    username = data['username']
    Utype = data['Utype']
    controller = usersController()
    controller.ChangeAdminOrUser(username, int(Utype))
    data = {
        'flag': 1
    }
    return data


@app.route('/setProhibit/', methods=['post', 'get'])
def setProhibit():
    data = request.values
    username = data['username']
    Prohibit = data['Prohibit']
    controller = usersController()
    controller.ChangeProhibit(username, int(Prohibit))
    data = {
        'flag': 1
    }
    return data


@app.route('/deleteUser/', methods=['post', 'get'])
def deleteUser():
    data = request.values
    username = data['username']
    controller = usersController()
    controller.deleteUser(username)
    data = {
        'flag': 1
    }
    return data


@app.route('/')
def logLout():
    if session.get('uid')!=None:
        session.pop('uid')
    if session.get('username')!=None:
        session.pop('username')
    resp=make_response(redirect(url_for('hello_world')))
    resp.set_cookie('username','')
    return resp


@app.route('/deleteList/',methods=['post','get'])
def deleteList():
    data = request.values
    lid = data['lid']
    username = session.get('username')
    controller = usersController()
    controller.deleteList(username, lid)

    return {'suc':1}

@app.route('/addList/',methods=['post','get'])
def addList():
    data = request.values
    listName = data['listname']
    uid=session['uid']
    controller = usersController()
    controller.addList(listName, uid)
    return {'suc':1}
if __name__ == '__main__':
    app.run()
