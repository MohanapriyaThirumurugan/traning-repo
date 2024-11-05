import pymongo

dburl="mongodb+srv://mohana:mohana@cluster0.cqguvdh.mongodb.net/mentorassign?retryWrites=true&w=majority&appName=Cluster0"

myclient=pymongo.MongoClient(dburl)
# print(myclient)
mydb = myclient["mydatabase"]
# print(myclient.list_database_names())
mycol = mydb["customers"]
print(mydb.list_collection_names())

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

# print(x)

#CREATE MANY DATA TO INSERT

mydict1 =[
           { "name": "John WICK", "address": "Highway 37",
           "location":"karapakam"},
           { "name": "John", "address": "Highway 35",
           "location":"chennai"},
           { "name": "MOHANA", "address": "Highway 36",
           "location":"tambaram"},
           { "name": "PRITA", "address": "Highway 39",
           "location":"chrompet"},
            ]

# Y=mycol.insert_many(mydict1)
# print(Y)

# FIND METHOD THE DATA

# findquery={"name":"mohana"}

# mydoc=mycol.find(findquery)

# for i in mydoc:
#  print(i)

 #DELETE MERTHOD IN MONGODB

#  delete={"name":"PRIYA"}
#  mydelete=mycol.delete_one(delete)

#  print(mydelete)

 # update the value
# Check if a document with "name": "PRIYA" exists before updating
if mycol.count_documents({"name": "PRIYA"}) > 0:
    # Define filter and new values
    update = {"name": "PRIYA"}
    new_value = {"$set": {"name": "PRIYAhello"}}
    
    # Perform the update operation
    v1 = mycol.update_one(update, new_value)
    
    # Check if the document was modified
    if v1.modified_count > 0:
        print("Document updated successfully.")
    else:
        print("Document matched but no changes were made (already up-to-date).")
else:
    print("No document with 'name': 'PRIYA' was found in the collection.")





