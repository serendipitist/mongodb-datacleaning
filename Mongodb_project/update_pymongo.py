from pymongo import MongoClient
import datetime
import sys

connection = MongoClient("mongodb://localhost")

def add_review_date_using_update_one(student_id):
    print "updating record using update_one anf $set"
    db = connection.school
    scores = db.scores
    
    try:
        score = scores.find_one({'student_id':student_id, 'type':'homework'})
        print "before", score
        
        # update using set
        record_id = score['_id']
        result = scores.update_one({'_id':record_id}, {'$set':{'review_date':datetime.datetime.utcnow()}})
        
        print "num matched:", result.matched_count
        score = score.find_one({'_id':record_id})
        print "after:" , score
        
    except Exception as e:
            raise
        
add_review_date_using_update_one(10)
# add_review_date_for_all()


def ad_review_dates_for_all():
    print"updating record using update_one and $set"
