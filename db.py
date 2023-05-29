import pymongo

mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)

db = client["TODO"]
collection = db["todo"]

def create(data):
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

def all():
    response = collection.find({}) # {} - filter {"_id":0} will exclude _id during find
    result = []
    for x in response:
        x["_id"] = str(x["_id"]) # id should in str type
        result.append(x)
    return result

def get_one(condition):
    response = collection.find_one({"name":condition})
    response["_id"] = str(response["_id"])
    return response

def update(name,data):
    data=dict(data)
    response = collection.update_one({"name":data["name"]},{"$set":{"description":data['description']}})
    return response.modified_count

def delete(name):
    response = collection.delete_one({"name":name})
    return response.deleted_count 
