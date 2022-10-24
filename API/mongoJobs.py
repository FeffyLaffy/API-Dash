#MIT License

#Copyright (c) 2022 Feffy

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import pymongo
from datetime import datetime
import random
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")

def check(mycol, id):
    myquery = { "id": id }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        return True, x
    return False, None

def create_db():
    dblist = client.list_database_names()
    if "musedash" in dblist:
        mydb = client["musedash"]
        return mydb
    else:
        mydb = client["musedash"]
        return mydb

def create_collection(mydb):
    colllist = mydb.list_collection_names()
    if "PlayersData" in colllist:
        data = mydb["PlayersData"]
        return data
    else:
        data = mydb["PlayersData"]
        return data

def findDocument(mycol, id):
    data=mycol.find_one({'uid': id})
    if data is None:
        return None
    return data
        
def create_data_players(id, ip, name):
    data= {
        "created_at": str(datetime.utcnow()),
        "updated_at": str(datetime.utcnow()),
        "user_id": id,
        "nickname": name,
        "uid": id,
        "ip_address": ip,
    }
    return data

class FindData:
    def __init__(self, id, ip):
        self.id=id
        self.ip=ip

    def get_data_find_by_id(self):
        data= {
            "created_at": 1,
            "updated_at": str(datetime.utcnow()),
            "user_id": 1,
            "nickname": 1,
            "uid": self.id,
            "ip_address": self.ip
        }
        mydb = client["musedash"]
        collect = mydb["PlayersData"]
        x = collect.find_one({}, data)
        print(x)
        return x
        
    def get_data_find_by_ip(self):
        mydb = client["musedash"]
        collist = mydb.list_collection_names()
        for x in collist:
            x = mydb[x].find_one({}, {"ip_address": self.ip})
        return x

class Data:
    def __init__(self, id, ip, name):
        self.id=id
        self.ip=ip
        self.name=name
        
    def get_or_make_data(self):
        db=create_db()
        collection=create_collection(db)
        get=findDocument(collection, self.id)
        if get is None:
            data=create_data_players(self.id, self.ip, self.name)
            print(data)
            collection.insert_one(data)
            return data
        else:
            return get

