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


    #判断手机号是否存在
    def isExist(self,ID):
        if self.regex.search(ID)==None:
            return False
        user=self.logic_users.getUserByID(ID)
        if len(user)>=1:
            return True
        return False

    def usernameIsExist(self,usernamne):
        userid=self.logic_users.getUidByUserName(usernamne)
        if userid!=None:
            return True
        return False


    #判断用户名密码是否匹配
    def loginSuccess(self,ID,PASSWORD):
        if ID==None:
            return False, '',0,
        if self.regex.search(ID)==None:
            return False,'',0,0
        user=self.logic_users.getUserByID(ID)
        if len(user)==0:
            return False,'',0,0
        user=user[0]
        if user.PASSWORD==PASSWORD:
            return True,user.NICKNAME,user.UTYPE,user.Prohibit
        return False,'',0,0

    #添加用户
    def addUser(self,ID,NIKENAME,PASSWORD,PROBLEM,ANSWER):
        self.logic_users.addUser(ID,NIKENAME,PASSWORD,PROBLEM,ANSWER)

    #根据用户名获取用户歌单信息
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

    #向歌单中添加歌曲
    def addSongToUserList(self,sid,lid):
        x=self.logic_song.getListSong(lid,sid)
        if len(x)!=0:
            return False
        self.logic_song.addList_Song(lid,sid)
        return True

    #获取全部用户信息
    def getAllUserMessage(self):
        Users=self.logic_users.getAllUser()
        Usernames=[]
        Uids=[]
        Utypes=[]
        Uprohibits=[]
        for user in Users:
            Usernames.append(user.NICKNAME)
            Uids.append(user.ID)
            Utypes.append(user.UTYPE)
            Uprohibits.append(user.Prohibit)
        args={
            'Usernames':Usernames,
            'Uids':Uids,
            'Utypes':Utypes,
            'Uprohibits':Uprohibits
        }
        return args

    #删除歌单歌曲
    def deleteSongList(self,sid,lid):
        self.logic_song.delete_ListSongByLIDAndSID(lid,sid)


    def ChangeAdminOrUser(self,username,Utype):
        self.logic_users.changeAdminOruser(username,Utype)

    def ChangeProhibit(self,username,Prohibit):
        self.logic_users.changeProhibit(username,Prohibit)


    def deleteUser(self,username):
        ULists=self.logic_users.getUserListsByUsername(username)
        Lids=[U.LID for U in ULists]
        for lid in Lids:
            self.logic_song.delete_list(lid)
            self.logic_users.deleteUserListTable(username,lid)
        self.logic_users.deleteUser(username)
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



