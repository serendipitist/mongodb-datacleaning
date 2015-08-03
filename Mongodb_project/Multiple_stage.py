#Who has mentioned most unique user
from pymongo import MongoClient
import pprint
client =MongoClient("mongodb://localhost:27017")
db=client.examples


def user_mentions():
    result=db.tweets.aggregate([{"$unwind":"$entities.user_mentions"},
                                {"$group":{"_id":"$user.screen_name",
                                           "$mset":{
                                                   "$addToSet":"$entities.user_mentions.screen_name"}}},
                                                   {"$unwind":"$mset"}, #we end up calculate
                                                   {"$group":{"_id":"$_id","count" :{"$sum":1}}},
                                                   {"$sort":{"count":-1}},
                                                   {"$limit":10}])
    return result
                                                                                 
if __name__ == 'main':
    result=user_mentions()
    pprint.pprint(result)
    
    