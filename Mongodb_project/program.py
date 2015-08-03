import json
import urllib2
import pymongo
# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")
# get a handle to the school database
db = connection.reddit
stories = db.stories
stories.drop()
# get reddit homepage
reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")
parsed = json.loads(reddit_page.read())
for item in parsed['data']['children']:
    print stories.insert_one(item['data'])

