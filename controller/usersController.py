from service.users import Logic_Users
from service.song import Logic_Song
from tools.tools import getJsonByPath
from flask import url_for
import re

class usersController():
    def __init__(self, s=1):
        self.s = s
        self.logic_users=Logic_Users()
        self.logic_song=Logic_Song()
        self.regex=re.compile('^\d{11}$')


    #判断用户名是否存在
    def isExist(self,ID):
        print(ID)
        if self.regex.search(ID)==None:
            return False
        user=self.logic_users.getUserByID(ID)
        if len(user)>=1:
            return True
        return False


    #判断用户名密码是否匹配
    def loginSuccess(self,ID,PASSWORD):
        if self.regex.search(ID)==None:
            return False,''
        user=self.logic_users.getUserByID(ID)
        if len(user)==0:
            return False,''
        user=user[0]
        if user.PASSWORD==PASSWORD:
            return True,user.NICKNAME
        return False,''

    #添加用户
    def addUser(self,ID,NIKENAME,PASSWORD,PROBLEM,ANSWER):
        self.logic_users.addUser(ID,NIKENAME,PASSWORD,PROBLEM,ANSWER)

    #
    def giveUserListMessage(self,userName):
        UID=self.logic_users.getUidByUserName(userName)
        listsIds=self.logic_users.getListsByUid(UID)
        args={'name':'我创建的歌单'}
        Lists=[]
        for i,listId in enumerate(listsIds):

            arg={}
            List=self.logic_song.getListById(listId)
            LNAME=List.NAME
            arg.update({'name':LNAME,'id':listId})
            Lists.append(arg)
        args.update({"lists":Lists})
        return args
    def addSongToUserList(self,sid,lid):
        x=self.logic_song.getListSong(lid,sid)
        if len(x)!=0:
            return False
        self.logic_song.addList_Song(lid,sid)
        return True

    def deleteSongList(self,sid,lid):
        self.logic_song.delete_ListSongByLIDAndSID(lid,sid)
    # def getUserListMessage(self,username):
    #     ULits=self.logic_users.getUserListsByUsername(username)
    #     LID=[]
    #     LNAME=[]
    #     for ulist in ULits:
    #         LID.append(ulist.LID)
    #         list=self.logic_song.getListById(ulist.LID)
    #         LNAME.append(list.NAME)
    #     data={
    #         'ULID':LID,
    #         'ULNAME':LNAME
    #     }
    #     return data

# u=usersController()
# print(u.giveUserListMessage('倾我一生一世念'))



