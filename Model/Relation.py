from sqlalchemy import Column, String, INT, CHAR, VARCHAR, SMALLINT, Boolean, PrimaryKeyConstraint, BIGINT, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LIST_SONG(Base):
    __tablename__ = 'LIST_SONG'
    LID = Column(BIGINT, ForeignKey("LIST.ID"))
    SID = Column(BIGINT, ForeignKey("SONG.ID"))
    __table_args__ = (
        PrimaryKeyConstraint('LID', 'SID'),
    )

    def __init__(self, AID, SID):
        self.AID = AID
        self.SID = SID


class ALBUM_SONG(Base):
    __tablename__ = 'ALBUM_SONG'
    AID = Column(BIGINT, ForeignKey("ALBUM.ID"))
    SID = Column(BIGINT, ForeignKey("SONG.ID"))
    __table_args__ = (
        PrimaryKeyConstraint('AID', 'SID'),
    )

    def __init__(self, AID, SID):
        self.AID = AID
        self.SID = SID


class VOCALIST_ALBUM(Base):
    __tablename__ = 'VOCALIST_ALBUM'
    VID = Column(BIGINT, ForeignKey("VOCALIST.ID"))
    AID = Column(BIGINT, ForeignKey("ALBUM.ID"))
    __table_args__ = (
        PrimaryKeyConstraint('VID', 'AID'),
    )

    def __init__(self, VID, AID):
        self.VID = VID
        self.AID = AID


class VOCALIST_SONG(Base):
    __tablename__ = 'VOCALIST_SONG'
    VID = Column(BIGINT, ForeignKey("VOCALIST.ID"))
    SID = Column(BIGINT, ForeignKey("SONG.ID"))
    __table_args__ = (
        PrimaryKeyConstraint('VID', 'SID'),
    )

    def __init__(self, VID, SID):
        self.VID = VID
        self.SID = SID


class SONG_VOCALIST(Base):
    __tablename__ = 'SONG_VOCALIST'
    SID = Column(BIGINT, ForeignKey("SONG.ID"))
    VID = Column(BIGINT, ForeignKey("VOCALIST.ID"))
    __table_args__ = (
        PrimaryKeyConstraint('SID', 'VID'),
    )

    def __init__(self, SID, VID):
        self.SID = SID
        self.VID = VID


class Leaderboard(Base):
    __tablename__ = 'Leaderboard'
    SID = Column(BIGINT, primary_key=True)
    INITTIME = Column(BIGINT, nullable=False)
    PRETIME = Column(BIGINT, nullable=False)
    PRENUM = Column(BIGINT, nullable=False)
    NUM = Column(BIGINT, nullable=False)
    DNUM = Column(BIGINT, nullable=False)

    def __init__(self, SID, INITTIME, PRETIME, PRENUM, NUM, DNUM):
        self.SID = SID
        self.INITTIME = INITTIME
        self.PRETIME = PRETIME
        self.PRENUM = PRENUM
        self.NUM = NUM
        self.DNUM = DNUM



class USER_LIST(Base):
    __tablename__ = 'USER_LIST'
    UID=Column(BIGINT,ForeignKey("USERS.ID"))
    LID=Column(BIGINT,ForeignKey("LIST.ID"))
    __table_args__ = (
        PrimaryKeyConstraint('UID', 'LID'),
    )
    def __init__(self,UID,LID):
        self.UID=UID
        self.LID=LID
# from implement.implement import implement_actions
# ac=implement_actions()
# q=USER_LIST.UID==15861161811
# s=ac.query_all(USER_LIST,q)
# for i in s:
#     print(i.LID)
# u=USER_LIST(15861161811,602735910000001)
# ac.add_user_list(15861161811,602735910000001)
# print(s.SID)
# s=ac.query_all(ALBUM_SONG,q)[0]
# print(s.AID)
