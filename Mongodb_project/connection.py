import pymongo

import sys
from exception import doc
connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
scores = db.scores

def find():
    print "find, reporting for the duty"
    query = {'type':'exam', 'score':{'$gt':50, '$lt':70}}
    # projection = {'student_id':1, '_id':0}
    try:
        cursor = scores.find(query)
    except Exception as e :
        print "Unexpected error:" , type(e), e
        
    sanity = 0 
    
    for doc in cursor:
        print doc
        sanity = sanity + 1
        if (sanity > 10):
            break
        
        
find()
        
        
