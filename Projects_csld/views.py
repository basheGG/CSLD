import tornado.ioloop
import tornado.web
from api.member_csld import MemberApi
from api.product_csld import ProductApi
from api.audit_csld import AuditApi
from api.audit_csld import SearchAudit
from api.audit_csld import IntoAudit
from api.audit_csld import UpdataAudit
from api.audit_csld import DeleteAudit

def make_app():

    return tornado.web.Application([
        (r"/info",MemberApi),
        (r"/product", ProductApi),
        (r"/auditlist", AuditApi), # 详情列表
        (r"/searchaudit", SearchAudit),  # 搜索审核用户
        (r"/intoaudit", IntoAudit),  # 添加审核用户
        (r"/updataaudit", UpdataAudit),  # 更新审核用户
        (r"/deleteaudit", DeleteAudit),  # 删除审核用户
    ])

