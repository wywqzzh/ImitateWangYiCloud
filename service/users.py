from Model.Base import USERS
from Model.Relation import USER_LIST
from implement.implement import implement_actions
from sqlalchemy import text,and_


class Logic_Users():
    def __init__(self):
        self.action = implement_actions()

    # 根据用户名查找
    def getUserByID(self, ID):
        query_filter = USERS.ID == text(ID)
        users = self.action.query_all(USERS, query_filter)
        return users

    # 添加用户
    def addUser(self, ID, NIKENAME, PASSWORD, PROBLEM, ANSWER):
        self.action.add_user(ID, NIKENAME, PASSWORD, PROBLEM, ANSWER)

    #根据用户昵称查询用户ID
    def getUidByUserName(self,username):
        query_filter = USERS.NICKNAME == username
        Uid=self.action.query_all(USERS,query_filter)
        if len(Uid)>=1:
            return Uid[0].ID
        else:
            return None

    def getUserListsByUsername(self,username):
        query_filter=USERS.NICKNAME==username
        UID=self.action.query_all(USERS,query_filter)[0].ID
        query_filter=USER_LIST.UID==UID
        ULists=self.action.query_all(USER_LIST,query_filter)
        return ULists

    #根据用户ID查找歌单,返回歌单ID
    def getListsByUid(self,UID):
        query_filter=USER_LIST.UID==UID
        user_lists=self.action.query_all(USER_LIST,query_filter)
        listsIds=[]
        for i in user_lists:
            listsIds.append(i.LID)
        return listsIds

    def getAllUser(self):
        query_filter=True
        Users=self.action.query_all(USERS,query_filter)
        return Users

    def changeAdminOruser(self,username,Utype):
        if Utype==0:
            data={"UTYPE":1}
        else:
            data = {"UTYPE": 0}
        query_filter=USERS.NICKNAME==username
        self.action.update_by_filter(USERS,data,query_filter)

    def changeProhibit(self, username, Prohibit):
        if Prohibit == 0:
            data = {"Prohibit": 1}
        else:
            data = {"Prohibit": 0}
        query_filter = USERS.NICKNAME == username
        self.action.update_by_filter(USERS, data, query_filter)

    def deleteUserListTable(self,username,lid):
        query_filter = USERS.NICKNAME == username
        UID = self.action.query_all(USERS, query_filter)[0].ID
        query_filter =and_(USER_LIST.UID == UID,USER_LIST.LID==lid)
        self.action.delete_by_filter(USER_LIST,query_filter)

    def deleteUser(self,username):
        query_filter =USERS.NICKNAME==username
        self.action.delete_by_filter(USERS,query_filter)

    def addUserListTable(self,uid,lid):
        self.action.add_user_list(uid,lid)
