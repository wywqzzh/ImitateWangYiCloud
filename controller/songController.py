from service.song import Logic_Song
from tools.tools import getJsonByPath
from flask import url_for


class songController():
    def __init__(self,s=1):
        self.s=s
    def getWordsSnamesVnamesBySid(self, List):
        logic_song = Logic_Song()
        song = logic_song.getSongsByIdList(List)[0];
        path = '../网易云音乐2/static' + song.SWORDSURL
        irc = getJsonByPath(path)
        args = {
            "IRCS": [irc],
            "URLS": [url_for('static', filename=song.SAUDIOURL[1:])],
            "SNAMES": [song.SNAME],
            "VNAMES": [song.VNAME],
        }
        return args
    def getWordsSnamesVnamesByAid(self,ID,type):
        logic_song = Logic_Song()
        print(ID)
        if type=='ALBUM':
            A_S=logic_song.getSongAlbumByAID(ID)
        else:
            A_S=logic_song.getSongListByLID(ID)
        songList=[]
        for i in A_S:
            songList.append(i.SID)
            print(i.SID)
        songs=logic_song.getSongsByIdList(songList)
        IRCS=[]
        URLS=[]
        SNAMES=[]
        VANMES=[]
        for song in songs:
            path = '../网易云音乐2/static' + song.SWORDSURL
            IRCS.append(getJsonByPath(path))
            URLS.append(url_for('static',filename=song.SAUDIOURL[1:]))
            SNAMES.append(song.SNAME)
            VANMES.append(song.VNAME)
        args = {
            "IRCS": IRCS,
            "URLS": URLS,
            "SNAMES":SNAMES,
            "VNAMES": VANMES,
        }
        return args

    def getAlbumAndListMessageByAid(self, ID, type):
        logic_song = Logic_Song()
        print(ID)
        args={}
        if type == 'ALBUM':
            AOL=logic_song.getAlbumById(ID)
            A_S = logic_song.getSongAlbumByAID(ID)

        else:
            AOL = logic_song.getListById(ID)
            A_S = logic_song.getSongListByLID(ID)

        args={
            "name":AOL.NAME,
            "imgurl":AOL.URL[1:],
        }
        if type=='ALBUM':
            args.update({"type": "ALBUM"})
        else:
            args.update({"type": "LIST"})
        return args
        # songList = []
        # for i in A_S:
        #     songList.append(i.SID)
        #     print(i.SID)
        # songs = logic_song.getSongsByIdList(songList)
        # IRCS = []
        # URLS = []
        # SNAMES = []
        # VANMES = []
        # for song in songs:
        #     path = '../网易云音乐2/static' + song.SWORDSURL
        #     IRCS.append(getJsonByPath(path))
        #     URLS.append(url_for('static', filename=song.SAUDIOURL[1:]))
        #     SNAMES.append(song.SNAME)
        #     VANMES.append(song.VNAME)
        # args = {
        #     "IRCS": IRCS,
        #     "URLS": URLS,
        #     "SNAMES": SNAMES,
        #     "VNAMES": VANMES,
        # }


