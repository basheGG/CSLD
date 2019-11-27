import tornado.web
import tornado.ioloop
import json
from models.product_model import ProductModel


class ProductApi(tornado.web.RequestHandler):
    def get(self):
        datas = self.request.body
        data_dict = json.loads(datas)
        critern = set()

        if "productnames" in data_dict:
            critern.add(ProductModel.product_name == data_dict["productnames"])
        if "id" in data_dict:
            critern.add(ProductModel.id == data_dict["id"])
        res = ProductModel().get_data(*critern)
        result = []
        for r in res:
            result.append({
                "id": r.id,
                "version": r.version,
                "pro_sys": r.pro_sys,
                "opernation": r.opernation,
                "infos": r.infos,
                "product_name": r.product_name,
                "channel": r.channel,
            })
        self.write(json.dumps(result))

    def post(self):
        datas = self.request.body
        data_dict = json.loads(datas)
        res = ProductModel().insert_data(data_dict)
        if res is True:
            return self.get()
        else:
            self.write({"errcode": 400, "success": False,"errormsg":"新增失败，请重新添加"})


    def put(self):
        datas = self.request.body
        data_dict = json.loads(datas)
        res = ProductModel().update_data(data_dict,data_dict["id"])
        if res is True:
            return self.get()
        else:
            self.write({"errcode": 400, "success": False,"errormsg":"修改失败，请查询字段等信息，重新修改"})

    def delete(self):
        datas = self.request.body
        data_dict = json.loads(datas)
        res = ProductModel().delete_data(data_dict["id"])
        if res is True:
            return self.get()
        else:
            self.write({"errcode": 400, "success": False, "errormsg": "删除失败"})