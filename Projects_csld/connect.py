from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'review'
USERNAME = 'root'
PASSWORD = '123456'

db_url='mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    DATABASE
)


from sqlalchemy.ext.declarative import declarative_base
engine = create_engine(db_url)
Base = declarative_base(engine)



from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
session = Session()


# if __name__=='__main__':
#     print(dir(Base))
#     print(dir(session))


