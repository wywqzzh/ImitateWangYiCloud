from service.Leaderboard import Logic_Leaderboard
from service.song import Logic_Song
from tools.Mysnow import MySnow
import time

class leaderboardController():
    def __init__(self, s=1):
        self.s = s
        self.logic_leaderboard = Logic_Leaderboard()
        self.logic_song = Logic_Song()
        self.mysnow=MySnow()

    def deleteLeaderboard(self):
        NAMES=['飙升榜','新歌榜','热歌榜']
        for name in NAMES:
            LIST=self.logic_song.getListByNAME(name)
            if LIST==None:
                continue
            for  list in LIST:
                id=list.ID
                self.logic_song.delete_ListSongByLID(id)
                self.logic_song.delete_list(id)
    def createList(self,args):
        #创建飙升榜
        solarId=self.mysnow.get_id()
        solarName='飙升榜'
        solarUrl='/imgs/n_blist/飙升榜.jpg'
        self.logic_song.addList(solarId,solarName,solarUrl,0)
        solarSong=args['solarArgs']['ids']
        for sid in solarSong:
            self.logic_song.addList_Song(solarId,sid)

        #创建新歌榜
        newId = self.mysnow.get_id()
        newName = '新歌榜'
        newUrl = '/imgs/n_blist/新歌榜.jpg'
        self.logic_song.addList(newId, newName, newUrl,0)
        newSong = args['newArgs']['ids']
        for sid in newSong:
            self.logic_song.addList_Song(newId, sid)

        #创建热歌榜
        hotId = self.mysnow.get_id()
        hotName = '热歌榜'
        hotUrl = '/imgs/n_blist/热歌榜.jpg'
        self.logic_song.addList(hotId, hotName, hotUrl,0)
        hotSong = args['hotArgs']['ids']
        for sid in hotSong:
            self.logic_song.addList_Song(hotId, sid)

        return solarId,newId,hotId
    def Leaderboard(self):
        self.deleteLeaderboard()
        solarsongId = self.logic_leaderboard.soarLeaderboard()
        newsongId = self.logic_leaderboard.newLeaderboard()
        hotsongId = self.logic_leaderboard.hotLeaderboard()


        solarArgs = {}
        solarArgs.update({"ids":solarsongId})
        solarNames=[]
        for i in range(len(solarsongId)):
            solarSong = self.logic_song.getSongsByIdList([solarsongId[i]])[0]
            solarNames.append(solarSong.SNAME)
        solarArgs.update({"names":solarNames})

        newArgs = {}
        newArgs.update({"ids": newsongId})
        newNames = []
        for i in range(len(newsongId)):
            newSong = self.logic_song.getSongsByIdList([newsongId[i]])[0]
            newNames.append(newSong.SNAME)
        newArgs.update({"names": newNames})

        hotArgs = {}
        hotArgs.update({"ids": hotsongId})
        hotNames = []
        for i in range(len(hotsongId)):
            hotSong = self.logic_song.getSongsByIdList([hotsongId[i]])[0]
            hotNames.append(hotSong.SNAME)
        hotArgs.update({"names": hotNames})

        args={}
        args.update({"solarArgs":solarArgs})
        args.update({"newArgs":newArgs})
        args.update({"hotArgs": hotArgs})
        solarId,newId,hotId=self.createList(args)
        args['solarArgs'].update({"Id":solarId})
        args['newArgs'].update({"Id": newId})
        args['hotArgs'].update({"Id": hotId})
        return args

    def setPlayMessage(self,sid):
        songPlayMessage=self.logic_leaderboard.getPlayMessageBySid(sid)
        preTime=songPlayMessage.PRETIME
        currentTime=int(time.time())
        num=songPlayMessage.NUM+1
        DNUM=num-songPlayMessage.PRENUM
        nextTime=songPlayMessage.PRETIME+86400
        update_hash={
            "NUM":num
        }
        DTIME=currentTime-preTime
        if DTIME>=86400:
            change={
                "DNUM":DNUM,
                "PRENUM":num,
                "PRETIME":currentTime
            }
            update_hash.update(change)
        self.logic_leaderboard.updatePlayMessage(sid,update_hash)
# l = leaderboardController()
# l.deleteLeaderboard()
# l.Leaderboard()
