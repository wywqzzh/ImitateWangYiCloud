from sqlalchemy import Column, String, INT, CHAR, VARCHAR, SMALLINT, Boolean,BIGINT
from sqlalchemy.ext.declarative import declarative_base
from implement.implement import implement_actions
Base = declarative_base()


class SONG(Base):
    __tablename__ = 'SONG'
    ID = Column(BIGINT, primary_key=True)
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

    def __init__(self, ID, NAME,URL):
        self.ID = ID
        self.NAME = NAME
        self.URL=URL


class ALBUM(Base):
    __tablename__ = 'ALBUM'
    ID = Column(BIGINT, primary_key=True)
    NAME = Column(VARCHAR(200), nullable=False)
    URL = Column(VARCHAR(200), nullable=True)

    def __init__(self, ID, NAME, URL):
        self.ID = ID
        self.NAME = NAME
        self.URL = URL
class VOCALIST(Base):
    __tablename__='VOCALIST'
    ID=Column(BIGINT,primary_key=True)
    NAME=Column(VARCHAR(200),nullable=False)
    def __init__(self,ID,NAME):
        self.ID=ID
        self.NAME=NAME
# ac=implement_actions()
# q=ALBUM.AID==82437132
# s=ac.query_all(ALBUM,q)[0]
# print(s.AID)
