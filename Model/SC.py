# Person.py
from sqlalchemy import Column, String, INT,CHAR,VARCHAR,SMALLINT,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Course(Base):  # 定义一个类，继承Base
    __tablename__ = 'Course'
    CNO = Column(CHAR(10), primary_key=True)
    # CNO = Column(CHAR(10), primary_key=True, nullable=False)
    CNAME = Column(VARCHAR(30))
    # CNAME = Column(VARCHAR(30), nullable=False)
    CCREDIT=Column(SMALLINT,nullable=True)
    # CCREDIT = Column(SMALLINT)
    sssss=Column(SMALLINT,nullable=True)
    # sss = Column(SMALLINT)
    PERIOD=Column(SMALLINT,nullable=True)
    # PERIOD = Column(SMALLINT)

    def __init__(self, CNO, CNAME,CCREDIT,sssss,PERIOD):
        self.CNO=CNO
        self.CNAME=CNAME
        self.CCREDIT=CCREDIT
        self.sssss=sssss
        self.PERIOD=PERIOD
class Course1(Base):
    __tablename__ = 'hehe'
    CNO=Column(CHAR(10),primary_key=True,nullable=False)
    CNAME=Column(VARCHAR(30),nullable=False)
    CCREDIT=Column(SMALLINT)
    sss=Column(SMALLINT)
    PERIOD=Column(SMALLINT)
    x=Column(Boolean)