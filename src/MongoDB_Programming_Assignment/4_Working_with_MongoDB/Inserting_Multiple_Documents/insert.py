from autos import process_file


def insert_autos(infile, db):
    autos = process_file(infile)

    # Your code here. Insert the data in one command
    for a in autos:
        db.autos.insert(a)
        # db.posts.insert(infile)


  
if __name__ == "__main__":
    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    print insert_autos('autos-small.csv', db)
