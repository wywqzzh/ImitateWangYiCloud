from Model.Base import SONG, ALBUM, LIST
from Model.Relation import ALBUM_SONG, LIST_SONG
from implement.implement import implement_actions


class Logic_Song():
    def __init__(self):
        self.action = implement_actions()

    # 获取基本表SONG数据
    def getSongsByIdList(self, idLits):
        action = implement_actions()
        query_filter = SONG.ID.in_(idLits)
        result = action.query_all(SONG, query_filter)
        return result

    # 获取关系表ALBUM_SONG数据
    def getSongAlbumByAID(self, AID):
        query_filter = ALBUM_SONG.AID == AID
        result = self.action.query_all(ALBUM_SONG, query_filter)
        return result

    # 获取关系表LIST_SONG数据
    def getSongListByLID(self, LID):
        query_filter = LIST_SONG.LID == LID
        result = self.action.query_all(LIST_SONG, query_filter)
        return result

    # 获取基本表ALBUM数据
    def getAlbumById(self, ID):
        query_filter = ALBUM.ID == ID
        result = self.action.query_all(ALBUM, query_filter)[0]
        return result

    # 获取基本表LIST数据
    def getListById(self, ID):
        query_filter = LIST.ID == ID
        result = self.action.query_all(LIST, query_filter)
        if len(result)>=1:
            return result[0]
        else:
            return None
    def getListByNAME(self,NAME):
        query_filter=LIST.NAME==NAME
        result=self.action.query_all(LIST,query_filter)
        return result
    # 模糊查询根据歌名
    def fuzzyQuerySongsBySname(self, sname):
        sname='%'+sname+'%'
        query_filter=SONG.SNAME.ilike(sname)
        songs=self.action.query_all(SONG,query_filter)
        return songs

    # 模糊查询根据歌名
    def fuzzyQuerySongsByVname(self, vname):
        vname = '%' + vname + '%'
        query_filter = SONG.VNAME.ilike(vname)
        songs = self.action.query_all(SONG, query_filter)
        return songs

    #添加LIST
    def addList(self,ID,LNAME,URL):
        self.action.add_list(ID,LNAME,URL)

    #添加LIST_SONG
    def addList_Song(self,LID,SID):
        self.action.add_list_song(LID,SID)


    #删除LIST_SONG
    def delete_ListSongByLID(self,LID):
        query_filter =LIST_SONG.LID==LID
        self.action.delete_by_filter(LIST_SONG,query_filter)

    #删除LIST
    def delete_list(self,ID):
        query_filter=LIST.ID==ID
        self.action.delete_by_filter(LIST,query_filter)


    #获取所有List,返回ID
    def getAllLists(self):
        L=['新歌榜','热歌榜','飙升榜']
        query_filter=LIST.NAME.notin_(L)
        Lists=self.action.query_all(LIST,query_filter)
        listsIds=[]
        for l in Lists:
            listsIds.append(l.ID)
        return listsIds

    #获取所有Album

    def getAllAlbums(self):
        query_filter = True
        Albums=self.action.query_all(ALBUM,query_filter)
        albumsIds=[]
        for a in Albums:
            albumsIds.append(a.ID)
        return albumsIds
# L=Logic_Song()
#
# lists=L.getAllLists()
# for l in lists:
#     print(l.ID)
# r=L.fuzzyQuerySongsByVname('张杰')
# print(len(r))
# query_filter = SONG.VNAME.like('张杰')
# action = implement_actions()
# r=action.query_all(SONG,query_filter)
# print(len(r))

# r=L.getAlbumById(599604030000001)
# print(r.ID)
# print(r.NAME)
# print(r.URL)
