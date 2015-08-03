from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db=client.examples

def main():
    city=db.cities1.update({"name":"Munchen","country":"Germany"},{"$unset":{"isoCountryCode":""}})


    #db.cities1.save(city)

if __name__ == '__main__':
        main()