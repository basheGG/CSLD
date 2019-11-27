import json
from common.uils import DeviceSign,GetConsul,GetShebei
from common.redis_token import Token

class VerifyC():

    def vericion(self,data_dict):
        sign = data_dict["sign"]

        if "AC_CODE" in data_dict:
            # 开始验证AC_CODE
            AC_CODE = data_dict["AC_CODE"]
            args = GetConsul().get_data(AC_CODE)
            print(args)
            res = DeviceSign(IMEI=args["IMEI"], MAC=args["MAC"], Timestamp=args["Timestamp"]).Sign()
            print('加密前的sign?{}'.format(sign))
            print('加密后的sign?{}'.format(res))
            if sign == res:
                shop_id = args["shopID"]
                merchart_Id = args["merchartId"]
                if shop_id == 0:
                    return {"message": "该设备未绑定", "success": False, "errcode": 4001}
                if merchart_Id == 0:
                    return {"message": "该设备未注册", "success": False, "errcode": 4002}
            else:
                return {"message": "sign错误", "success": False, "errcode": 4003}
        else:
            if "token" in data_dict and "shopID" in data_dict:
                token = data_dict["token"]
                shopID = data_dict["shopID"]
                if token is None:
                    return {"message": "token不能为空", "success": False, "errcode": 4004}
                elif shopID is None:
                    return {"message": "shopID不能为空", "success": False, "errcode": 4005}
                else:
                    res_token = Token().LoadToken(token)
                    print('*******************************************')
                    print(res_token.__dict__)
                    print('*******************************************')
                    # 开始进行设备验证
                    sbid = GetShebei().get_data(res_token.Id, shopID)
                    if sbid != True:
                        return {"message": "该设备不存在", "success": False, "errcode": 4007}

            else:
                return {"message": "不能为空", "success": False, "errcode": 4006}