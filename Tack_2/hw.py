import argparse
from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb://localhost:27017/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db=client.mds

parser = argparse.ArgumentParser(description="Application cats")

parser.add_argument("--action", help = "create, update, read, delete, read_by_name, add_feature_by_name, delete_all")
parser.add_argument("--id", help = "id")
parser.add_argument("--name", help = "name")
parser.add_argument("--age", help = "age")
parser.add_argument("--features", help = "features", nargs="+")

args= vars(parser.parse_args())
action = args["action"]
pk = args["id"]
name = args["name"]
age = args["age"]
features = args["features"]

def read():
    return db.cats.find()


def create():
    name = input("Enter name: ")
    age = input("Enter age: ")
    features = input("Enter features: ")
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    return db.cats.insert_one(cat)


def update():

    name = input("Enter name: ")
    age = input("Enter age: ")
    feature = input("Enter feature: ")
    new_cat = {

        "age": age,
        "feature": feature
    }
    return db.cats.update_one({"name": name}, {"$set": new_cat})

def delete_by_name():
    name = input("Enter name: ")
    return db.cats.delete_one({"name": name})

def delete_all():
    confirmation = input("Are you sure you want to delete all records? (yes/no): ")
    if confirmation.lower() == "yes":
        return db.cats.delete_many({})
    else:
        print("Deletion cancelled.")

def read_by_name():
    name = input("Enter name: ")
    docum = db.cats.find_one({"name": name})
    if docum is not None:
        return docum
    else:
        print("Cat not exist ")

def add_feature_by_name():
    name = input("Enter name: ")
    feature = input("Enter new feature: ")
    return db.cats.update_one({"name": name}, {"$push": {"features": feature}})

if __name__ == "__main__":
    match action:
        case "read":
            results = read()
            [print(cat) for cat in results]

        case "read_by_name":
            result = read_by_name()
            print(result)

        case "create":
            result = create()
            print(result)

        case "update":
            result = update()
            print(result)

        case "delete":
            result = delete_by_name()
            print(result)

        case "delete_all":
            result = delete_all()
            print(result)

        case "add_feature":
            result = add_feature_by_name()
            print(result)

        case _:
            print("Unknown action")


