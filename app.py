from flask import Flask, render_template, url_for, request, redirect
from service.song import Logic_Song
from tools.tools import getJsonByPath
from sqlalchemy import BIGINT

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
from controller.songController import songController
from controller.usersController import usersController
from controller.leaderboardController import leaderboardController

#主页
@app.route('/')
def hello_world():
    username = request.args.get('username')
    controller=leaderboardController()
    args=controller.Leaderboard()
    if username != None:
        return render_template('home.html', username=username,args=args)
    else:
        return render_template('home.html', username='',args=args)


# @app.route('/player/')
# def player():
#     y = getJson();
#     return render_template("player.html", irc=y);

#音乐播放
@app.route('/playerDeal/<int:id>/<Type>/')
def playerDeal(id, Type):
    index = request.args.get('index');
    if (Type == 'SONG'):
        controller = songController()
        if id == 1:
            id = request.args.get('ID')
        args = controller.getWordsSnamesVnamesBySid([id])
        args.update({"index": index})
        args.update({"SIDS":[id]})
        return render_template("player.html", args=args);
    elif (Type == 'ALBUM' or Type == 'LIST'):
        controller = songController()
        args = controller.getWordsSnamesVnamesByAid(id, Type)
        args.update({"index": index})
        return render_template("player.html", args=args);


#歌单专辑显示
@app.route('/AlbumAndList/<int:id>/<type>/')
def AlbumAndList(id, type):
    controller = songController()
    ID=request.args.get('id');
    if id==0:
        id=ID
    args = controller.getAlbumAndListMessageByAid(id, type)
    username = request.args.get('username')
    return render_template("AlbumAndList.html", username=username, id=id, type=type, args=args);


@app.route("/test/")
def test():
    return render_template("test.html")


@app.route("/login/")
def login():
    return render_template('login.html', error='1')

#登录事件处理
@app.route("/loginInterpretation/", methods=['POST', 'GET'])
def loginInterpretation():
    ID = request.form.get('username')
    PASSWORD = request.form.get('password')
    controller = usersController()
    flag, username = controller.loginSuccess(ID, PASSWORD)
    if ID == None or not flag:
        error = '用户名或密码错误'
        return render_template("login.html", error=error)
    print(username)
    URL = url_for('hello_world') + '?username=' + username
    return redirect(URL)

#注册
@app.route('/register/')
def register():
    return render_template('register.html');

#注册事件处理
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
        return render_template('register.html', error='用户名已存在')
    else:
        controller.addUser(userID, nickname, password, problem, answer)
    return redirect(url_for('login'))

#搜索测试
@app.route('/search/')
def search():
    controller = songController()
    args = controller.fuzzyQuerySongs('张杰')
    key = "张杰"
    return render_template('search.html', key=key, args=args)

#搜索事件处理
@app.route('/searchInterpretation/', methods=['GET', 'POST'])
def searchInterpretation():
    s = request.form.get('search')
    controller = songController()
    args = controller.fuzzyQuerySongs(s)
    username = request.args.get('username')
    return render_template('search.html', username=username, type='SONG', key=s, args=args)


#歌曲播放量处理
@app.route('/BehindMethod/',methods=['GET','POST'])
def BehindMethod():
    id=request.args.get('id')
    controller=leaderboardController()
    controller.setPlayMessage(id)
    data={
        's':1
    }
    return data


#我的音乐
@app.route('/mymusic/')
def mymusic():
    username=request.args.get('username')
    controller=usersController()
    args=controller.giveUserListMessage(username)
    args.update({"username":username})
    print(args)
    return render_template('mymusic.html',username=username,args=args)


#热门推荐
@app.route('/playlist/')
def mymusic():
    username=request.args.get('username')
    controller=songController()
    args=songController.recommendListAndList()
    args.update({"username":username})
    print(args)
    return render_template('mymusic.html',username=username,args=args)
if __name__ == '__main__':
    app.run()
