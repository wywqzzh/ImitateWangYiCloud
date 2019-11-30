# db_mg.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.SC import Course
import sqlalchemy
from sqlalchemy import Column, CHAR, VARCHAR, SMALLINT, Boolean, func
import urllib
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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
