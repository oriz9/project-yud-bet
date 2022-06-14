import pymongo
from pymongo import MongoClient

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://oriz9:oriz9oriz9!@cluster0.xh3gq.mongodb.net/first?retryWrites=true&w=majority"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
db = client["accounts"]
collection = db["accounts"]


#def add_account(name, password):
#    post = {"name": name, "password": password}
#    collection.insert_one(post)

def addd_account(accountdic):
    print(accountdic)
    post = {"name": accountdic["name"], "password": accountdic["password"], "folder": accountdic["folder"]}
    collection.insert_one(post)

def search(name):
    result = collection.find({"name": "gilad"})
    for result in result:
        print(result)


def getPasw_name(name):
    # the_json = get_json_for_name(name)
    # return the_json["password"]
    # return your pasword using the name
    passs = ""
    result = collection.find({"name": f"{name}"})
    for result in result:
        try:
            passs = result["password"]
        except UnboundLocalError:
            return "bad name"
        print(passs)
    return (passs)


# def get_json_for_name(name) -> dict:
#     result = collection.find({"name": f"{name}"})
#     return result[0]

def check_if_admin(name):
    result = collection.find({"name": f"{name}"})
    for i in result:
        if i["folder"] == "admin":
            print("yesseseses")
            return True
        else:
            return False


def getFolders_name(name):
    # the_json=get_json_for_name(name)
    # return the_json["folder"]

    # return the folder using the name
    print(f"the name is {name}")
    folder = ""
    query = {"name": f"{name}"}
    result = collection.find(query)
    print(f"the result: {result}")
    for i in result:
        print(i)
        folder = i["folder"]
    # print(folder)
    return folder

# add_account("ori", "123")
# search("gilad")
# print(getPasw_name("ori"))
