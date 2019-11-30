import sqlalchemy
from sqlalchemy import Column,CHAR,VARCHAR,SMALLINT,Boolean,func
import urllib
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

quoted = urllib.parse.quote_plus(
    'DRIVER={ODBC Driver 17 for SQL Server};Server=127.0.0.1;Database=school;UID=root;PWD=wywq100539;Port=1433;')
engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))


conn = engine.connect()


Base = declarative_base(engine)
class Course(Base):
    __tablename__ = 'hehe'
    CNO=Column(CHAR(10),primary_key=True,nullable=False)
    CNAME=Column(VARCHAR(30),nullable=False)
    CCREDIT=Column(SMALLINT)
    sss=Column(SMALLINT)
    PERIOD=Column(SMALLINT)
    x=Column(Boolean)
# Base.metadata.create_all()#将上面定义的内容映射到数据库中，相当于创建表。映射完改变字段，则不会更新映射

#加入数据
session=sessionmaker(engine)()


# for i in range(5,10):
#     course=Course(CNO='JO%s'%i,CNAME='呵呵%s'%i,CCREDIT=i,sss=i+1,PERIOD=2*i,x=(i%2==0))
#     session.add(course)
#     session.commit()

courses=session.query(Course).all()
for i in courses:
    print(i)

courses=session.query(Course.CNO,Course.CNAME).all()
for i in courses:
    print(i)

re=session.query(func.count(Course.CNAME)).first()
print(re)

re=session.query(func.avg(Course.sss)).first()
print(re)