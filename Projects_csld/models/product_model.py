from sqlalchemy import Column,Integer,String
from connect import Base,session

class ProductModel(Base):
    __tablename__ = 'offline_product'  # 表名字
    id = Column(Integer,primary_key=True)
    product_name = Column(String(20))
    version = Column(String(20),default=None)
    infos = Column(String(20),default=None)
    pro_sys = Column(String(20),default=None)
    channel = Column(String(20),default=None)
    opernation = Column(Integer,default=None)

    def get_data(self,*critern):
        args = session.query(ProductModel).filter(*critern).all()
        return args

    def insert_data(self,datas):

        try:
            if "product_name" in datas:
                product_name = datas["product_name"]
            else:
                product_name = None
            if "version" in datas:
                version = datas["version"]
            else:
                version = None
            if "infos" in datas:
                infos = datas["infos"]
            else:
                infos = None
            if "pro_sys" in datas:
                pro_sys = datas["pro_sys"]
            else:
                pro_sys = None
            if "channel" in datas:
                channel = datas["channel"]
            else:
                channel = None
            if "opernation" in datas:
                opernation = datas["opernation"]
            else:
                opernation = None
            dao = ProductModel(product_name=product_name,version=version,infos=infos,pro_sys=pro_sys,channel=channel,opernation=opernation)
            # session.add(add_data)  # 添加一条
            # session.add_all(add_datas)  # 添加多条
            session.add(dao)
            session.commit()
            print('新增成功')
            return True
        except:
            session.rollback()
            print('新增失败')


    def update_data(self,datas,id):
        try:
            datas.pop("id")
            print(datas)
            session.query(ProductModel).filter(ProductModel.id == id).update(datas)
            session.commit()
            return True
        except:
            session.rollback()

    def delete_data(self,id):
        try:
            """删除数据，默认开始事务"""
            rows = session.query(ProductModel).filter(ProductModel.id == id).first()
            session.delete(rows)
            session.commit()
            return True
        except:
            session.rollback()


