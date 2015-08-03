import pymongo

import sys


# establish a connection to the Database
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.test
things = db.things

def using_upsert():
    print "updating with upsert"
    
    try:
        # lets remove all stuff from things
        things.drop()
        
        things.update_one({'thing':'apple'}, {'$set':{'color':'red'}}, upsert=True)
        things.update_many({'thing':'banana'}, {'$set':{'color':'yellow'}}, upsert=True)
        things.replace_one({'thing':'pear'}, {'color':'green'}, upsert=True)
        
        apple = things.find_one({'thing':'apple'})
        print "apple:", apple 
        banana = things.find_one({'thing':'banana'})
        print "banana:", banana
        
        
    except Exception as e:
        print "Unexpected error:", type(e), e
        
        
using_upsert()
        
        
