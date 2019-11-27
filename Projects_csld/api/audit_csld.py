import tornado.web
import tornado.ioloop
import json
from models.audit_model import Audit
from connect import session
import warnings


warnings.filterwarnings("ignore")
# 详情列表
class AuditApi(tornado.web.RequestHandler):
    def get(self):
        rows = session.query(Audit).all()
        au_list = []
        for i in rows:
            dic = {
                "id": i.id,
                "username": i.username,
                "state": i.state,
                "audit_state": i.audit_state,
                "email": i.email,
                "operaition": i.operaition
            }
            au_list.append(dic)
        print(au_list)
        print("查询成功")
        if au_list:
            return self.write({'message': '成功', 'success': True, 'code': 200, 'data': au_list})
        else:
            return self.write({"errcode": 400, "success": False,"message":"查询详情列表失败"})


#搜索查询
class SearchAudit(tornado.web.RequestHandler):
    def get(self):
        datas = self.request.body
        print("postman传过来的:",datas)
        data_dict = json.loads(datas)
        critern = set()

        if "username" in data_dict:
            critern.add(Audit.username == data_dict["username"])
        if "id" in data_dict:
            critern.add(Audit.id == data_dict["id"])
        res = Audit().get_data(*critern)
        result = []
        for r in res:
            result.append({
                "id": r.id,
                "username": r.username,
                "state": r.state, # 开通类别
                "audit_state": r.audit_state, # 审核状态
                "email": r.email,
                "operaition": r.operaition, # 操作
            })
        self.write(json.dumps(result))
        print("查询到的",result)
        if result:
            return self.write({'message': '成功', 'success': True, 'code': 200, 'data': result})
        else:
            return self.write({"errcode": 400, "success": False,"message":"搜索查询失败"})


# 添加用户审核
class IntoAudit(tornado.web.RequestHandler):
    def post(self):
        datas = self.request.body
        data_dict = json.loads(datas)
        res = Audit().insert_data(data_dict)
        if res is True:
            # return self.get()
            return self.write({'message': '添加成功', 'success': True, 'code': 200, 'data': res})
        else:
            return self.write({"errcode": 400, "success": False,"message":"新增失败，请重新添加"})


# 修改审核用户
class UpdataAudit(tornado.web.RequestHandler):
    def put(self):
        body_datas = self.request.body
        print("body字典：",body_datas)
        headers_datas = self.request.headers
        print("headers字典：",headers_datas)

        data_dict = json.loads(body_datas)

        res = Audit().update_data(data_dict,data_dict["id"])
        if res is True:
            return self.write({'message': '修改成功', 'success': True, 'code': 200, 'data': res})
        else:
            self.write({"errcode": 400, "success": False,"message":"修改失败，请查询字段等信息，重新修改"})


#删除审核用户
class DeleteAudit(tornado.web.RequestHandler):
    def delete(self):
        datas = self.request.body
        data_dict = json.loads(datas)
        res = Audit().delete_data(data_dict["id"])
        if res is True:
            return self.write({'message': '删除成功', 'success': True, 'code': 200, 'data': res})
        else:
            self.write({"errcode": 400, "success": False, "message": "删除失败"})
