from sqlalchemy import Column, String, INT, CHAR, VARCHAR, SMALLINT, Boolean,BIGINT
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class SONG(Base):
    __tablename__ = 'SONG'
    ID = Column(VARCHAR(20), primary_key=True)
    SNAME = Column(VARCHAR(200), nullable=False)
    VNAME = Column(VARCHAR(200), nullable=True)
    SWORDSURL = Column(VARCHAR(50), nullable=True)
    SIMAGEURL = Column(VARCHAR(50), nullable=True)
    SAUDIOURL = Column(VARCHAR(50), nullable=False)

    def __init__(self, ID, SNAME, VNAME, SWORDSURL, SIMAGEURL, SAUDIOURL):
        self.ID = ID
        self.SNAME = SNAME
        self.VNAME = VNAME
        self.SWORDSURL = SWORDSURL
        self.SIMAGEURL = SIMAGEURL
        self.SAUDIOURL = SAUDIOURL


class LIST(Base):
    __tablename__ = 'LIST'
    ID = Column(BIGINT, primary_key=True)
    NAME = Column(VARCHAR(200), nullable=False)
    URL=Column(VARCHAR(200),nullable=True)
    TYPE=Column(INT)
    STYLE=Column(VARCHAR(200))
    def __init__(self, ID, NAME,URL,TYPE,STYLE):
        self.ID = ID
        self.NAME = NAME
        self.URL=URL
        self.TYPE=TYPE
        self.STYLE=STYLE


class ALBUM(Base):
    __tablename__ = 'ALBUM'
    ID = Column(BIGINT, primary_key=True)
    NAME = Column(VARCHAR(200), nullable=False)
    URL = Column(VARCHAR(200), nullable=True)
    STYLE=Column(VARCHAR(200))
    def __init__(self, ID, NAME, URL,STYLE):
        self.ID = ID
        self.NAME = NAME
        self.STYLE=STYLE
        self.URL = URL
class VOCALIST(Base):
    __tablename__='VOCALIST'
    ID=Column(BIGINT,primary_key=True)
    NAME=Column(VARCHAR(200),nullable=False)
    def __init__(self,ID,NAME):
        self.ID=ID
        self.NAME=NAME


class USERS(Base):
    __tablename__='USERS'
    ID=Column(BIGINT,primary_key=True)
    NICKNAME=Column(VARCHAR(200),nullable=False)
    PASSWORD=Column(VARCHAR(200),nullable=False)
    PROBLEM=Column(VARCHAR(200),nullable=False)
    ANSWER=Column(VARCHAR(200),nullable=False)
    UTYPE=Column(INT)
    Prohibit=Column(INT)
    def __init__(self,ID,NICKNAME,PASSWORD,PROBLEM,ANSWER,UTYPE,Prohibit):
        self.ID=ID
        self.NICKNAME=NICKNAME
        self.PASSWORD=PASSWORD
        self.PROBLEM=PROBLEM
        self.ANSWER=ANSWER
        self.UTYPE=UTYPE
        self.Prohibit=Prohibit
# ac=implement_actions()
# q=USERS.ID=='dasd'
# s=ac.query_all(USERS,q)
# s=s[0]
# print(s.ID)
