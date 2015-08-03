from pymongo import  MongoClient
import pprint 
import sys
connection = MongoClient("mongodb://localhost")
# get a handle to the school database
def insert_doc():
    db = connection.school
    people = db.people
    
    print "insert, reporting for duty"
    richard = {"name":"Richard kreuter", "company": "MongoDB", "interests": ['horses', 'skydiving', 'gardening']}
    andre = {"_id":"erlichson", "name":"Andrew Erlichson", "company": "MongoDB", "interests":{'running', 'singing'}}

    try:
        people.insert_one(richard)
        people.insert_one(andre)
        people
        
    except Exception as e:
        print "Unexpected error:", type(e), e
        
    print (richard)

insert_doc()            