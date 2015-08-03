from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

tesla_s={
         "manufacturer":"TeslaMotors",
         "class":"full-size",
         "body style": "5-door liftback",
         },{
          "country" :"The Netherlands"
          }
         
db = client.examples
db.autos.insert(tesla_s)
for a in db.autos.find():
    pprint.pprint(a)
    
#working example