import sys
from pymongo import MongoClient
import pprint
client = MongoClient("mongodb://localhost:27017")
db = client.test
users= db.users

doc={'firstname':'Shireesha','lastname':'Parampalli'}
print doc
print "about to insert the document"
try :
    users.insert(doc)
except:
    print "insert failed:", sys.exc_info()[0]
    print doc
    print "inserting again"

try :
    users.insert(doc)
except:
    print "Second insert failed:", sys.exc_info()[0]
    print doc
    print "inserting again"