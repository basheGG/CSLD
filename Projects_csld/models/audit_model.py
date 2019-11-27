# -*- coding:utf-8 -*-
from sqlalchemy import Column,Integer,String
from connect import Base,session


class Audit(Base):
    __tablename__ = 'offline_member_audit'  # 商户审核
    id = Column(Integer, primary_key=True)
    username = Column(String(255)) # 用户名
    state = Column(Integer) # 开通类别
    audit_state = Column(Integer) # 审核状态
    email = Column(String(255))
    operaition = Column(Integer) #操作

    def get_data(self,*critern):
        m_args = session.query(Audit).filter(*critern).all()
        # print("查询成功")
        return m_args

    def insert_data(self,datas):
        try:
            if "username" in datas:
                username = datas["username"]
            else:
                username = None
            if "state" in datas:
                state = datas["state"]
            else:
                state = None
            if "audit_state" in datas:
                audit_state = datas["audit_state"]
            else:
                audit_state = None
            if "email" in datas:
                email = datas["email"]
            else:
                email = None
            if "operaition" in datas:
                operaition = datas["operaition"]
            else:
                operaition = None
            dao = Audit(username=username,state=state,audit_state=audit_state,email=email,operaition=operaition)

            session.add(dao)
            session.commit()
            print('新增成功')
            return True
        except:
            session.rollback()
            print('新增失败')


    def update_data(self,datas,id):
        try:
            print("请求过来的数据",datas)
            datas.pop("id")
            session.query(Audit).filter(Audit.id == id).update(datas)
            session.commit()
            print("更新成功")
            return True
        except:
            session.rollback()
            print("更新失败")

    def delete_data(self,id):
        try:
            """删除数据，默认开始事务"""
            rows = session.query(Audit).filter(Audit.id == id).first()
            session.delete(rows)
            session.commit()
            print("删除成功")
            return True
        except:
            session.rollback()
            print("删除失败")

