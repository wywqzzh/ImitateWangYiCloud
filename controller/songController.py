from service.song import Logic_Song
from tools.tools import getJsonByPath
from flask import url_for


class songController():
    def __init__(self, s=1):
        self.s = s
        self.logic_song = Logic_Song()

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

    def getWordsSnamesVnamesByAid(self, ID, type):
        logic_song = Logic_Song()
        if type == 'ALBUM':
            A_S = logic_song.getSongAlbumByAID(ID)
        else:
            A_S = logic_song.getSongListByLID(ID)
        songList = []
        for i in A_S:
            songList.append(i.SID)
        songs = logic_song.getSongsByIdList(songList)
        IRCS = []
        URLS = []
        SNAMES = []
        VANMES = []
        for song in songs:
            path = '../网易云音乐2/static' + song.SWORDSURL
            IRCS.append(getJsonByPath(path))
            URLS.append(url_for('static', filename=song.SAUDIOURL[1:]))
            SNAMES.append(song.SNAME)
            VANMES.append(song.VNAME)
        args = {
            "IRCS": IRCS,
            "URLS": URLS,
            "SNAMES": SNAMES,
            "VNAMES": VANMES,
            "SIDS":songList,
        }
        return args

    def getAlbumAndListMessageByAid(self, ID, type):
        logic_song = Logic_Song()
        args = {}
        if type == 'SONG':
            AOL = logic_song.getSongsByIdList([ID])[0]
            SNAMES = [AOL.SNAME]
            SAURLS = [AOL.SAUDIOURL]
            SVOCALISTS = [AOL.VNAME]
            SIDS = [AOL.ID]
            args = {
                "id": AOL.ID,
                "name": AOL.SNAME,
                "imgurl": AOL.SIMAGEURL[1:],
                "snames": SNAMES,
                "saurls": SAURLS,
                "svocalists": SVOCALISTS,
                "sids": SIDS
            }
            args.update({"type": "SONG"})
            return args
        if type == 'ALBUM':
            AOL = logic_song.getAlbumById(ID)
            args.update({"type": "ALBUM"})
            R_S = logic_song.getSongAlbumByAID(ID)

        elif type == 'LIST':
            AOL = logic_song.getListById(ID)
            args.update({"type": "LIST"})
            R_S = logic_song.getSongListByLID(ID)
        idList = []
        for i in R_S:
            idList.append(i.SID)
        songs = logic_song.getSongsByIdList(idList)

        SNAMES = []
        SAURLS = []
        SVOCALISTS = []
        SIDS = []
        for i, song in enumerate(songs):
            SNAMES.append(song.SNAME)
            SAURLS.append(song.SAUDIOURL)
            SVOCALISTS.append(song.VNAME)
            SIDS.append(song.ID)
        args.update({
            "id": ID,
            "snames": SNAMES,
            "saurls": SAURLS,
            "svocalists": SVOCALISTS,
            "sids": SIDS
        })
        args.update({
            "name": AOL.NAME,
            "imgurl": AOL.URL[1:],
        })
        return args

    # 模糊查询
    def fuzzyQuerySongs(self, s):
        song1 = self.logic_song.fuzzyQuerySongsBySname(s)
        song2 = self.logic_song.fuzzyQuerySongsByVname(s)
        songs = song1 + song2
        SNAMES = []
        SAURLS = []
        SVOCALISTS = []
        SIDS = []
        for i, song in enumerate(songs):
            SNAMES.append(song.SNAME)
            SAURLS.append(song.SAUDIOURL)
            SVOCALISTS.append(song.VNAME)
            SIDS.append(song.ID)
        args={
            "snames": SNAMES,
            "saurls": SAURLS,
            "svocalists": SVOCALISTS,
            "sids": SIDS
        }
        return args
    #推荐内容信息
    def recommendListAndList(self):
        listsIds=self.logic_song.getAllLists()
        albumsIds=self.logic_song.getAllAlbums()
        args={"name":'全部'}
        Lists=[]
        for i, listId in enumerate(listsIds):
            arg = {}
            List = self.logic_song.getListById(listId)
            LNAME = List.NAME
            arg.update({'name': LNAME, 'id': listId,'type':'LIST'})
            Lists.append(arg)
        for i, albumId in enumerate(albumsIds):
            arg = {}
            Album = self.logic_song.getAlbumById(albumId)
            LNAME = Album.NAME
            arg.update({'name': LNAME, 'id': albumId,'type':'ALBUM'})
            Lists.append(arg)
        args.update({"lists":Lists})
        return args
# c = songController()
# c.fuzzyQuerySongs('张杰')
