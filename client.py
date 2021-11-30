import mongo5
#db="mydatabase",col="mycol",host="127.0.0.1"
#m = mongo5.Mongo("mydatabase","mycol","127.0.0.1")
m = mongo5.Mongo()

#print(m.insert_one({"a":2}))
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
#print(m.insert_many(mylist))
#print(m.find_one())
print(m.find())
#print(m.find_one_params({ "_id": 14, "name": "Viola", "address": "Sideway 1633"}))
#print(m.find_filter({ "_id": 14, "name": "Viola", "address": "Sideway 1633"}))
    # sort("name", 1) #ascending
    # sort("name", -1) #descending
#print(m.sort("name"))
#print(m.delete_one({ "_id": 14, "name": "Viola", "address": "Sideway 1633"}))
#print(m.delete_many())
#print(m.drop())
#query= { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
#new_value = { "name": "reza", "address": "hedayat"}
#print(m.update_one(query,new_value))

