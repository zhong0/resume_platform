from backend.log.logTemplate import JSONLogger
from pymongo import MongoClient
from pymongo.errors import PyMongoError

logger = JSONLogger("basicInfoDao").get_logger()

class basicInfoDao:
    def __init__(self, uri, username, password, db_name, collection_name):
        self.client = MongoClient(uri, username=username, password=password)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def updateUserInfo(self, account, data):
        try:
            user = self.collection.find_one({"account": account})

            if user:
                self.collection.update_one(
                    { "_id" : user["_id"]},
                    { "$set": data }
                )
                logger.info(f"Update user Successfully")
                return True
                  
            else:   
                self.collection.insert_one(data)
                return True

        except PyMongoError as e:
            logger.error(f"Update user Fail: {e}")
            return False
    
    def getUserBasicInfo(self, account):
        try:
            results = self.collection.find_one({"account": account},{
                    "name_cn": 1,
                    "name_en": 1,
                    "phone": 1,
                    "email": 1,
                    "github": 1,
                    "linkedin": 1,
                    "_id": 0
                })
            return results
        except PyMongoError as e:
            logger.error(f"Get the user basic intro fail: {e}")
            return []



    def __del__(self):
        self.client.close()