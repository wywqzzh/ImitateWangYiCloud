# db_mg.py
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from Model.SC import Course
# from sqlalchemy import Column, CHAR, VARCHAR, SMALLINT, Boolean, func,and_
# from sqlalchemy.ext.declarative import declarative_base
# from Model.Base import USERS
# from Model.Relation import Leaderboard
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc
import urllib
import sqlalchemy

class implement_actions():
    def __init__(self):
        # self.engine = create_engine('mssql+pymssql://root:wywq100539@127.0.0.1:1433/school', echo=True)
        # DBsession = sessionmaker(bind=self.engine)  # 创建DBsession类
        # self.session = DBsession()  # 创建对象
        self.quoted = urllib.parse.quote_plus(
            'DRIVER={ODBC Driver 17 for SQL Server};Server=127.0.0.1;Database=MusicSystem;UID=root;PWD=wywq100539;Port=1433;')
        self.engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(self.quoted))
        self.session = sessionmaker(self.engine)()

    def add_obj(self, obj):  # 添加内容
        self.session.add(obj)
        self.session.commit()  # 提交
        return obj

    def add_user_list(self,uid,lid):
        sql="INSERT INTO USER_LIST(UID, LID) VALUES ('{0}','{1}')".format(uid,lid)
        conn = self.engine.connect()
        conn.execute(sql)
        conn.close()
    def add_user(self, ID, NIKENAME, PASSWORD, PROBLEM, ANSWER):
        sql = "INSERT INTO USERS(ID, NICKNAME, PASSWORD, PROBLEM, ANSWER,UTYPE,Prohibit ) VALUES ('{0}','{1}','{2}','{3}','{4}',0,0)".format(
            ID, NIKENAME, PASSWORD, PROBLEM, ANSWER)
        conn = self.engine.connect()
        conn.execute(sql)
        conn.close()

    def add_list(self, ID, LNAME, URL,type):
        sql = "INSERT INTO LIST(ID, NAME, URL,TYPE) VALUES ('{0}','{1}','{2}',{3})".format(ID, LNAME, URL,type)
        conn = self.engine.connect()
        conn.execute(sql)
        conn.close()

    def add_list_song(self, LID, SID):
        sql = "INSERT INTO LIST_SONG(LID, SID) VALUES ('{0}','{1}')".format(LID, SID)
        conn = self.engine.connect()
        conn.execute(sql)
        conn.close()
    def add_user_list(self,UID,LID):
        sql = "INSERT INTO USER_LIST(UID, LID) VALUES ('{0}','{1}')".format(UID, LID)
        conn = self.engine.connect()
        conn.execute(sql)
        conn.close()
    def query_all(self, target_class, query_filter):  # 查询内容
        result_list = self.session.query(target_class).filter(query_filter).all()
        return result_list

    def Query_All(self, target_class):  # 查询内容
        result_list = self.session.query(target_class).all()
        return result_list

    def update_by_filter(self, obj, update_hash, query_filter):  # 更新内容
        self.session.query(obj).filter(query_filter).update(update_hash)
        self.session.commit()

    def delete_by_filter(self, obj, query_filter):  # 删除内容
        self.session.query(obj).filter(query_filter).delete()
        self.session.commit()

    def close(self):  # 关闭session
        self.session.close()

    def execute_sql(self, sql_str):  # 执行sql语句
        return self.session.execute(sql_str)

    def query_all_order(self, target_class, query_filter, order):
        result_list = self.session.query(target_class).filter(query_filter).order_by(desc(order)).all()
        return result_list

# user=USERS(15837716655,'hehe','wywq100539','ss','ss')
# im=implement_actions()
# im.add_user(15837716655,'hehe','wywq100539','ss','ss')
# q=Leaderboard.SID==599592620000001
# update_hash={"NUM":2,"DNUM":1}
# s=im.update_by_filter(Leaderboard,update_hash,q)
# print(len(s))
