# -*- encoding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

engine = create_engine('sqlite:///db.sqlite3', echo=True)

Base = declarative_base(bind=engine)


def db_connect():
    return engine


def create_table(engine):
    # 不存表，创建并初始化 investevent_rules
    if not engine.dialect.has_table(engine, 'investevent_rules'):
        Base.metadata.create_all(engine)
        sql_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rules.sql')
        with open(sql_file) as file:
            line = file.readline()
            engine.execute(line)
