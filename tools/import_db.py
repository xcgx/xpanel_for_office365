import configparser
from urllib.parse import quote_plus as urlquote

import sqlalchemy

from file_initialization import formed_files

db_conf = configparser.ConfigParser()
path = "../config/db.config"
db_conf.read(path)

news = formed_files()


def connect_mysql():
    username = db_conf.get("mysql", "username")
    password = db_conf.get("mysql", "password")
    dbhost = db_conf.get("mysql", "dbhost")
    dbport = db_conf.get("mysql", "dbport")
    dbname = db_conf.get("mysql", "dbname")

    DB_CONNECT = f'mysql+pymysql://{username}:{urlquote(password)}@{dbhost}:{dbport}/{dbname}?charset=utf8'

    conn = sqlalchemy.create_engine(DB_CONNECT, max_overflow=50,  # 超过连接池大小外最多创建的连接
                                    pool_size=50,  # 连接池大小
                                    pool_timeout=60,  # 池中没有线程最多等待的时间，否则报错
                                    pool_recycle=3600,  # 多久之后对线程池中的线程进行一次连接的回收（重置）
                                    encoding='utf-8',
                                    echo=False,
                                    pool_pre_ping=True
                                    )
