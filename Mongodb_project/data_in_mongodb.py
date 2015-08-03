'''mongoimport --db users --collection contacts --type csv --headerline --file /opt/backups/contacts.csv'''

""" 
Add a single line of code to the insert_autos function that will insert the
automobile data into the 'autos' collection. The data variable that is
returned from the process_file function is a list of dictionaries, as in the
example in the previous video.
"""
from pymongo import  MongoClient
import pprint
client= MongoClient("mongodb://localhost:27017")
db= client.examples

def find():
    query ={"country":{"$ne":"United States"}}
    cities=db.cities1.find(query)
    num_cities=0
    for c in cities:
        pprint.pprint(c)
        num_cities=+1
        
        print "number of cities :%d\n", num_cities
               
        
if __name__ == '__main__':
    find()