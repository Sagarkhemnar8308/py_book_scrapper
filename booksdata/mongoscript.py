from pymongo import MongoClient
import datetime

client = MongoClient('mongodb+srv://sagarkhemnar143:zipzap%40123@cluster0.hjygr.mongodb.net/')

db = client.scrapy

collection = db.test_collection

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id
