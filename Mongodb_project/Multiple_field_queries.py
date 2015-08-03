from pymongo import  MongoClient
import pprint 
client =MongoClient("Mongodb://localhost:27017")
db= client.examples

def find():
autos= db.autos.find({"manufacturer":"Toyota","class":"mid-size car"})
for a in autos:
    pprint.pprint(a)
    
        