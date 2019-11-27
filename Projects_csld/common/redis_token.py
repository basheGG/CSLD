import redis
import json

r = redis.Redis(host='127.0.0.1', port=6379, password='', db=1, decode_responses=True)


class Token():
    Token = ""
    Id = ""
    Type = ""
    Permissions = []

    def LoadToken(self, token):
        print('***********************************************')
        print(token)
        print('***********************************************')
        j = r.get("FaceMakeMoney:{Token}".format(Token=token))
        o = json.loads(j)
        self.Token = o["Token"]
        self.Id = o["Id"]
        self.Type = o["Type"]
        return self