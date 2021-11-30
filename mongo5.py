import pymongo

class Mongo:

    def __init__(self,db="mydatabase",col="mycol",host="127.0.0.1",port=27017,password=''):
        self.host = host
        self.port = port
        self.password = password
        self.m = pymongo.MongoClient("mongodb://{host}:{port}".format(host=self.host,port=self.port))
        self.db = self.m[db]
        self.col = self.db[col]
    
    def insert_one(self,obj_data):
        self.col.insert_one(obj_data)
    
    def insert_one(self,obj_data):
        r= self.col.insert_one(obj_data)
        return r.inserted_id
    

    def insert_many(self,obj_data):
        r= self.col.insert_many(obj_data)
        return r.inserted_ids
    
    def find_one(self):
        r= self.col.find_one()
        return r

    
    def find(self,limit=0):
        r= self.col.find().limit(limit)
        data = []
        for i in r:
            data.append(i)
        return data

    
    #Return only the names and addresses, not the _ids:
    def find_one_params(self,one_obj):
        r= self.col.find({},one_obj)
        data = []
        for i in r:
            data.append(i)
        return data
    

    #When finding documents in a collection, 
    #you can filter the result by using a query object.
    def find_filter(self,myquery):
        r= self.col.find(myquery)
        data = []
        for i in r:
            data.append(i)
        return data
    
    # sort("name", 1) #ascending
    # sort("name", -1) #descending
    def sort(self,key,gradiant=1):
        r= self.col.find().sort(key,gradiant)
        data = []
        for i in r:
            data.append(i)
        return data



    
    def delete_one(self,query):
        data = []
        find= self.col.find()
        r= self.col.delete_one(query)
        for i in find:
            data.append(i)
        return data
    

    def delete_many(self,query={}):
        r= self.col.delete_many(query)
        return r.deleted_count

#The drop() method returns true if the collection was dropped successfully, 
#and false if the collection does not exist.
    def drop(self):
        r= self.col.drop()
        return r


    def update_one(self,query,new_value):
        data = []
        find= self.col.find()
        values = { "$set": new_value }
        r= self.col.update_one(query,values)
        for i in find:
            data.append(i)
        return data
    
    def update_many(self,query,new_value):
        values = { "$set": new_value }
        r= self.col.update_one(query,values)
        return r.modified_count
    
