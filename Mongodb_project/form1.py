import sys
import pymongo
from exception import doc
from pydoc import Doc

connection =pymongo.MongoClient("mongodb://localhost")
db= connection.test
users= db.users
doc={'firstname':'Andrew','lastname':'Erlichson'}
print doc
print "about to insert the document"

try :
    users.insert_one(doc)
except:Exception  e:
    
    print "insert failed:",e
    
print Docprint "inserting again"
    