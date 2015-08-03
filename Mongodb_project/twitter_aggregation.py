#Aggregartion method
#Group Tweets By user
#Count Each User's Tweets
#Sort into Descending Order
#Select user at top
from pymongo import MongoClient
import pprint

client =MongoClient("mongodb://localhost:27017")
db =client.examples

 #2.Aggregation Methodology followers friend ratio
    #Highest follower to friend ratio
    #$match operator-filter
    #$project operator shaping the things
    

def highest_ratio():
    result= db.tweets.aggregate([{"$match":{"user.friends_count":{"$gt":0},"user.followers_count":{"$gt":0}}},
                                 {"$project":{"ratio":{"$divide":["$user.followers_count","$user.friends_count"]},"screen_name":"$user.screen_name"}},
                                 {"$sort":{"ratio":-1}},{"$limit":1}])
    
    #1.Aggregation Methodology
    #group based on screen_name that user field
    #$sum cumulator operator
   
    return result


if __name__ =='__main__':
    result= highest_ratio()
    pprint.pprint(result)
    for item in result:
        print item
    
    