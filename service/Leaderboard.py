from implement.implement import implement_actions
from Model.Relation import Leaderboard
import time


class Logic_Leaderboard():
    def __init__(self):
        self.action = implement_actions()

    def newLeaderboard(self):
        Time = int(time.time())
        query_filter = (Time - Leaderboard.INITTIME) > 10
        order = Leaderboard.NUM
        songs = self.action.query_all_order(Leaderboard, query_filter, order)[:10]
        songsId = []
        for s in songs:
            songsId.append(s.SID)
        return songsId

    def hotLeaderboard(self):
        query_filter = True
        order = Leaderboard.NUM
        songs = self.action.query_all_order(Leaderboard, query_filter, order)[:10]
        songsId = []
        for s in songs:
            songsId.append(s.SID)
        return songsId

    def soarLeaderboard(self):
        query_filter = True
        order = Leaderboard.DNUM
        songs = self.action.query_all_order(Leaderboard, query_filter, order)[:10]
        songsId = []
        for s in songs:
            songsId.append(s.SID)
        return songsId


    def getPlayMessageBySid(self,sid):
        query_filter=Leaderboard.SID==sid
        songPlayMessage=self.action.query_all(Leaderboard,query_filter)[0]
        return songPlayMessage

    def updatePlayMessage(self,sid,update_hash):
        query_filter = Leaderboard.SID == sid
        self.action.update_by_filter(Leaderboard,update_hash,query_filter)
# l = Logic_Leaderboard()
# s = l.getPreTimeBySid(599592620000001)
# print(s)
