from sqlalchemy import Column, String, INT, CHAR, VARCHAR, SMALLINT, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class SONG(Base):
    __tablename__ = 'SONG'
    SID = Column(INT, primary_key=True)
    SNAME = Column(VARCHAR(50), nullable=False)
    VNAME = Column(VARCHAR(50), nullable=True)
    SWORDSURL = Column(VARCHAR(50), nullable=True)
    SIMAGEURL = Column(VARCHAR(50), nullable=True)
    SAUDIOURL = Column(VARCHAR(50), nullable=True)

    def __init__(self, SID, SNAME, VNAME, SWORDSURL, SIMAGEURL, SAUDIOURL):
        self.SID = SID
        self.SNAME = SNAME
        self.VNAME = VNAME
        self.SWORDSURL = SWORDSURL
        self.SIMAGEURL = SIMAGEURL
        self.SAUDIOURL = SAUDIOURL
