import argparse
from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = f"mongodb://localhost:27017/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db=client.mds

parser = argparse.ArgumentParser(description="Application cats")

parser.add_argument("--action", help = "create, update, read, delete")
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

def create(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    return db.cats.insert_one(cat)


def update():
    pass


def delete():
    pass

if __name__ == "__main__":
    match action:
        case "read":
            results = read()
            [print(cat) for cat in results]

        case "create":
            result = create(name, age, features)
            print(vars(result))
        case "update":
            update()
        case "delete":
            delete()
        case _:
            print("Unknown action")
