from connect import Base,session
from models.audit_model import Audit
import warnings

def add_user():
    # person = User(username='test1',password ='qwe123')
    # session.add(person)      #add 是添加一条数据， add_all 添加多条数据
    persons = [
        Audit(username='张三', state=1,audit_state=1,email='zhangsan@163.com',operaition=0),
        Audit(username='李四', state=2, audit_state=0, email='lisi@163.com', operaition=0),
        Audit(username='王五', state=3, audit_state=0, email='wangwu@163.com', operaition=0),
        Audit(username='赵六', state=4, audit_state=0, email='zhaoliu@163.com', operaition=0),
    ]
    session.add_all(persons)    #  add_all 添加多条数据
    session.commit()
    print("添加用户成功")

def search_user():
    rows = session.query(Audit).all()
    # rows = session.query(Audit).first()
    for i in rows:
        dic = {
            "id":i.id,
            "username":i.username,
            "state":i.state,
            "audit_state":i.audit_state,
            "email":i.email,
            "operaition":i.operaition
        }
        print(dic)
    print("查询成功")

def updata_user():
    rows = session.query(Audit).filter(Audit.username == 'zhangsan').update({Audit.state: 0})
    session.commit()
    print(rows)
    print("修改成功")

def delect_user():
    rows = session.query(Audit).filter(Audit.username == 'zhangsan')[0]
    print(rows)
    session.delete(rows)
    session.commit()
    print("删除成功")


if __name__ =='__main__':
    warnings.filterwarnings("ignore")
    # add_user()
    search_user()
    # updata_user()
    # delect_user()
