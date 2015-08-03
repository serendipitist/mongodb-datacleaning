

from pymongo import MongoClient
import pprint
client = MongoClient("mongodb://localhost:27017")
db = client.m101
people= db.people
person = {'name':'Shireesha', 'role' : 'Engineer', 
              'address': {'address1': 'Sirimane',
                          'street':'661 8th A Main 3rd stage, 3rd block',
                          'state': 'Karnataka',
                          'city': 'Bangalore'},
              'interests': ['Reading Books','yoga']}
people.insert(person)

    
                                                                    