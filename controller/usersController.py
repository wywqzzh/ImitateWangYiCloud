from service.users import Logic_Users
from service.song import Logic_Song
from tools.tools import getJsonByPath
from flask import url_for
from tools.Mysnow import MySnow
import re

class usersController():
    def __init__(self, s=1):
        self.s = s
        self.logic_users=Logic_Users()
        self.logic_song=Logic_Song()
        self.regex=re.compile('^\d{11}$')
        self.mysnow=MySnow()


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
    def giveUserListMessage(self,uid):
        listsIds=self.logic_users.getListsByUid(uid)
        args={'name':'我创建的歌单'}
        Lists=[]
        for i,listId in enumerate(listsIds):

            arg={}
            List=self.logic_song.getListById(listId)
            LNAME=List.NAME
            url=List.URL
            arg.update({'name':LNAME,'id':listId,'url':url})
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
    def getAllUserMessage(self,username):
        Users=self.logic_users.getAllUser()
        Usernames=[]
        Uids=[]
        Utypes=[]
        Uprohibits=[]
        for user in Users:
            if user.NICKNAME!=username:
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

    #管理员与普通用户转换
    def ChangeAdminOrUser(self,username,Utype):
        self.logic_users.changeAdminOruser(username,Utype)
    #账号冻结与解冻转换
    def ChangeProhibit(self,username,Prohibit):
        self.logic_users.changeProhibit(username,Prohibit)

    #删除用户
    def deleteUser(self,username):
        ULists=self.logic_users.getUserListsByUsername(username)
        Lids=[U.LID for U in ULists]
        for lid in Lids:
            self.logic_song.delete_list(lid)
            self.logic_users.deleteUserListTable(username,lid)
        self.logic_users.deleteUser(username)

    #删除歌单
    def deleteList(self,username,lid):
        self.logic_users.deleteUserListTable(username,lid)
        self.logic_song.delete_ListSongByLID(lid)
        self.logic_song.delete_list(lid)

    def addList(self,listName,uid):
        newId=self.mysnow.get_id()
        newUrl = '/imgs/SONG/0.jpg'
        self.logic_song.addList(newId,listName,newUrl,1)
        self.logic_users.addUserListTable(uid,newId)




