# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import bcrypt

class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users
        
    def insert_user(self,data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        uid = self.Users.insert({"username":data.username,
                                 "name":data.name,
                                 "email":data.email,
                                 "password":hashed})
        print ("UID is ",uid)
        
#        myuser = self.Users.find_one({data.username})
#        if bcrypt.checkpw("MyPassword".encode(), myuser["password"]):
#            print ("this matches")