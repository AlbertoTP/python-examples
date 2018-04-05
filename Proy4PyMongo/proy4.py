# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 20:52:14 2018

@author: AlbertoTP
"""

import datetime
import pprint
import pymongo
from pymongo import MongoClient

myClient=MongoClient()
db=myClient.mydb
users=db.users

user1={"username":"beto",
       "password":"mypassword",
       "hobbies":["python","games","pizza"]}
user_id=users.insert_one(user1).inserted_id
pprint.pprint(users.find_one())

user2={"username":"user",
       "password":"pass",
       "hobbies":["java","eat","pizza"]}
user_id=users.insert_one(user2).inserted_id
pprint.pprint(users.find_one({"username":"user"}))

#insert multiple documents
usuarios=[{"username":"third",
       "password":"pass",
       "hobbies":["program","sleep"]},
       {"username":"four",
       "password":"pwd",
       "hobbies":["games","pizza"]},
        {"username":"five",
       "password":"contra",
       "hobbies":["series","soda"]},
        {"username":"six",
       "password":"123456",
       "hobbies":["eat","eat","pizza"]}]
       
result = users.insert_many(usuarios)
print (result.inserted_ids)

print ("# Doc: ",users.find().count())

print ("Find condition username: four",users.find({"username":"four"}).count())
print ("Multiple find conditions, username:four, password:pwd ",users.find({"username":"four","password":"pwd"}).count())

current_date=datetime.datetime.now()
print (current_date)

user3={"username":"date",
       "date": current_date}
user_id=users.insert_one(user3).inserted_id
pprint.pprint(users.find_one({"username":"date"}))

old_date=datetime.datetime(2016,8,10)

"""
Name 	Description
$eq 	Matches values that are equal to a specified value.
$gt 	Matches values that are greater than a specified value.
$gte 	Matches values that are greater than or equal to a specified value.
$in 	Matches any of the values specified in an array.
$lt 	Matches values that are less than a specified value.
$lte 	Matches values that are less than or equal to a specified value.
$ne 	Matches all values that are not equal to a specified value.
$nin 	Matches none of the values specified in an array.

"""
print ()
print ("date gte (greater than or equivalent)")
print (users.find({"date": {"$gte": old_date} }).count())
print ("date lte (less than or equivalent)")
print (users.find({"date": {"$lte": old_date} }).count())
print ("Exists field date")
print (users.find({"date": {"$exists": True} }).count())
print ("Diferent ne(not equal) beto")
print (users.find({"username": {"$ne": "beto"} }).count())

result = db.users.create_index([("username", pymongo.ASCENDING)],unique=True)
#unique campo con valor unico
print (sorted(list(db.users.index_information())))


"""
#Other example
client = MongoClient()
#client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
#or db = client['test-database']
collection = db.test_collection
#or collection = db['test-collection']

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
        
posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id
#Getting a Single Document With find_one()
pprint.pprint(posts.find_one())
#find_one() also supports querying on specific elements that the resulting document must match. To limit our results to a document with author “Mike” we do:
pprint.pprint(posts.find_one({"author": "Mike"}))
#Querying By ObjectId We can also find a post by its _id, which in our example is an ObjectId:
pprint.pprint(posts.find_one({"_id": post_id}))
"""