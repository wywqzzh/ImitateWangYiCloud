import sqlalchemy
from sqlalchemy import Column,CHAR,VARCHAR,SMALLINT,Boolean,func
# import urllib
# from sqlalchemy.ext.declarative import declarative_base
# # from data import Course
# from Model.SC import Course
# from sqlalchemy.orm import sessionmaker
# quoted = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};Server=127.0.0.1;Database=school;UID=root;PWD=wywq100539;Port=1433;')
# engine = sqlalchemy.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
# session=sessionmaker(engine)()
# ss=Course.CNO=='C01'and Course.sssss==1
# courses=session.query(Course).filter(None).all()
# s=session.query(Course).filter(Course.sssss==1).all()
# for i in courses:
#     print(type(i))
def getJsonByPath(path):
    f = open('', encoding='UTF-8')  # 设置文件对象
    line = f.readline()
    line = line[:-1]
    x = ''
    c = {}
    while line:
        c.update({line[:11]: line[11:]})
        line = f.readline()
        line = line[:-1]
    return c
