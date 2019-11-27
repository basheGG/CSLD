import tornado.web
import tornado.ioloop
from common.uils import DeviceSign,GetConsul,GetShebei
from common.redis_token import Token
import json
from models.member_model import registers
from tornado import gen


class MemberApi(tornado.web.RequestHandler):
    def vericion(self):
        datas = self.request.body
        data_dict = json.loads(datas)
        sign = data_dict["sign"]

        if "AC_CODE" in data_dict:
            # 调用数据获取值
            AC_CODE = data_dict["AC_CODE"]
            args = GetConsul().get_data(AC_CODE)
            print(args)
            res = DeviceSign(IMEI=args["IMEI"], MAC=args["MAC"], Timestamp=args["Timestamp"]).Sign()
            print('前端传递的sign为{}'.format(sign))
            print('加密后的sign为{}'.format(res))
            if sign == res:
                shop_id = args["shopID"]
                merchart_Id = args["merchartId"]
                if shop_id == 0:
                    return {"message": "该设备未绑定", "success": False,"errcode":4001}
                if merchart_Id == 0:
                    return {"message": "该设备未注册", "success": False,"errcode":4002}
            else:
                return {"message": "sign错误", "success": False,"errcode":4003}
        else:
            if "token" in data_dict and  "shopID" in data_dict:
                token = data_dict["token"]
                shopID = data_dict["shopID"]
                if token is None:
                    return {"message": "token不能为空","success":False,"errcode":4004}
                elif shopID is None:
                    return {"message": "shopID不能为空","success":False,"errcode":4005}
                else:
                    res_token = Token().LoadToken(token)
                    print('*******************************************')
                    print(res_token.__dict__)
                    print('*******************************************')
                    # 开始进行验证设备是否是当前商户的
                    sbid = GetShebei().get_data(res_token.Id,shopID)
                    if sbid != True:
                        return {"message": "该设备不存在", "success": False, "errcode": 4007}
            else:
                return {"message": "不能为空", "success": False,"errcode":4006}

    def get(self):
        res = self.vericion()
        if res is not None:
            if res["errcode"] == 4001:
                self.write({"message": "该设备未绑定", "success": False})
            elif res["errcode"] == 4002:
                self.write({"message": "该设备未注册", "success": False})
            elif res["errcode"] == 4003:
                self.write({"message": "sign错误", "success": False})
            elif res["errcode"] == 4004:
                self.write({"message": "token不能为空", "success": False})
            elif res["errcode"] == 4005:
                self.write({"message": "shopID不能为空", "success": False})
            elif res["errcode"] == 4006:
                self.write({"message": "不能为空", "success": False})
            elif res["errcode"] == 4007:
                self.write({"message": "该设备不存在", "success": False})
        else:
            m_args = registers().get_data()
            result = []
            for i in m_args:
                result.append({
                    "activation_code":i.activation_code
                })
            self.write(json.dumps(result))
            # self.render(json.dumps(result))
            # return json.dumps(result)
            # raise gen.Return(self.render(json.dumps(result)))


