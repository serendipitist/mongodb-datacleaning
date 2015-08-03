"""projection where u will send find all results document , I only want to see name"""

from pymongo import MongoClient
import pprint
client =MongoClient("mongodb://localhost:27017")
db = client.examples

def find():
    projection={"_id":0,"name":1}
    query=({"manufacturer":"Toyota","class": "mid-size car"})
    autos=(query)
    
    for a in autos:
        pprint.pprint(a)
if __name__ == '__main__':
        find()