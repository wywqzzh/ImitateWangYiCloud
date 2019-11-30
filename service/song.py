from Model.Base import SONG,ALBUM,LIST
from Model.Relation import ALBUM_SONG,LIST_SONG
from implement.implement import implement_actions



class Logic_Song():
    def __init__(self):
        self.action = implement_actions()

    def getSongsByIdList(self,idLits):
        action = implement_actions()
        query_filter = SONG.ID.in_(idLits)
        result = action.query_all(SONG, query_filter)
        return result
    def getSongAlbumByAID(self,AID):
        query_filter=ALBUM_SONG.AID==AID
        result=self.action.query_all(ALBUM_SONG,query_filter)
        return result
    def getSongListByLID(self, LID):
        query_filter = LIST_SONG.LID == LID
        result = self.action.query_all(LIST_SONG, query_filter)
        return result
    def getAlbumById(self,ID):
        query_filter=ALBUM.ID==ID
        result=self.action.query_all(ALBUM,query_filter)[0]
        return result
    def getListById(self,ID):
        query_filter=LIST.ID==ID
        result=self.action.query_all(LIST,query_filter)[0]
        return result
# L=Logic_Song()
# r=L.getAlbumById(599604030000001)
# print(r.ID)
# print(r.NAME)
# print(r.URL)