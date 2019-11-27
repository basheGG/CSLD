from sqlalchemy import Column,Integer,String
from connect import Base,session

class registers(Base):
    __tablename__ = 'offline_cash_registers'  # 表名称
    activation_code = Column(String(255), primary_key=True)
    imei = Column(String(255))
    mac = Column(String(255))
    shopkeeper_id = Column(Integer)
    shop_id = Column(Integer)
    sd_code = Column(String(255))
    last_bind_time = Column(String(255))
    online_state = Column(Integer)
    last_login_time = Column(String(255))
    activation_time = Column(String(255))
    bind_time = Column(String(255))
    pre_activation_time = Column(String(255))


    def get_data(self):
        m_args = session.query(registers).all()
        return m_args





