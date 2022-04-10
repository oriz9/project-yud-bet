import pymongo
from pymongo import MongoClient


# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://oriz9:oriz9oriz9!@cluster0.xh3gq.mongodb.net/first?retryWrites=true&w=majority"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
db = client["first"]
collection = db["first"]

def add_account(name, password):
    post = {"name": name, "password": password}
    collection.insert_one(post)

def search(name):
    result = collection.find({"name": "gilad"})
    for result in result:
        print(result)

def getPasw_name(name):
    #return your pasword using the name
    passs = ""
    result = collection.find({"name": f"{name}"})
    for result in result:
        try:
            passs = result["password"]
        except UnboundLocalError:
            return "bad name"
        print(passs)
    return(passs)

#add_account("ori", "123")
#search("gilad")
#print(getPasw_name("ori"))