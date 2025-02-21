import json
from backend.log.logTemplate import JSONLogger
from backend.dao.basicInfoDao import basicInfoDao
from utils.genSecure import decrypt
import utils.params as const

logger = JSONLogger("basicInfoSvc").get_logger()

class basicInfoSvc:
    def __init__(self):
        self.username = decrypt(const.username, bytes.fromhex(const.key))
        self.password = decrypt(const.password, bytes.fromhex(const.key))
        self.dao = basicInfoDao(const.uri, self.username, self.password, const.db_name, const.collection_user)

    def updateResume(self, data):
        try:
            data = json.loads(data)
            # 用 account 去搜值
            if "account" in data.keys():
                account = data["account"]
                if self.dao.updateUserInfo(account, data):
                    return True
                else:
                    return False
            else:
                return False
            
        except Exception as e:
            logger.error(f"updateResume Fail: {e}")
    
    def getUserBasicInfo(self, data):
        try:
            data = json.loads(data)
            if "account" in data.keys():
                account = data["account"]
                result = self.dao.getUserBasicInfo(account)
                if result:
                    return result
                else:
                    return None
            else:
                return None
            
        except Exception as e:
            logger.error(f"getUserBasicInfo Fail: {e}")

