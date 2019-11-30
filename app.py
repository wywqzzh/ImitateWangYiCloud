from flask import Flask, render_template, url_for
from service.song import Logic_Song
from tools.tools import getJsonByPath

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
from controller.songController import songController


def getJson():
    f = open("C:/Users/76774/Desktop/歌词/一念之间.txt", encoding='UTF-8')  # 设置文件对象
    line = f.readline()
    line = line[:-1]
    x = ''
    c = {}
    while line:
        c.update({line[:11]: line[11:]})
        line = f.readline()
        line = line[:-1]
    return c


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/player/')
def player():
    y = getJson();
    return render_template("player.html", irc=y);

@app.route('/playerDeal/<int:id>/<Type>/')
def playerDeal(id, Type):
    if (Type == 'SONG'):
        controller=songController()
        args = controller.getWordsSnamesVnamesBySid([id])
        print(args)
        return render_template("player.html", args=args);
    elif(Type=='ALBUM' or Type=='LIST'):
        controller = songController()
        print(id)
        print(Type)
        args=controller.getWordsSnamesVnamesByAid(id,Type)
        # print("ID",id)
        # print(args)
        return render_template("player.html", args=args);
@app.route('/AlbumAndList/<int:id>/<type>/')
def AlbumAndList(id,type):
    controller = songController()
    args=controller.getAlbumAndListMessageByAid(id,type)
    print(type)
    return render_template("AlbumAndList.html",id=id,type=type,args=args);
if __name__ == '__main__':
    app.run()
