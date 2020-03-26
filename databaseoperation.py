import pymongo
from bson import ObjectId
# Connected Database
connection = pymongo.MongoClient('localhost', 27017)
# create Database
database = connection['mydb_01']
# create Collection
collection =database['mycol_01']

print("database connected") 


def insert_record(data):
    document = collection.insert_one(data)
    return document.inserted_id


def update_or_create(document_id, data):
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set": data}, upsert=True)
    return document.acknowledged


def update_existing(document_id, data):
    document = collection.update_one({'_id': ObjectId(document_id)}, {"$set":data})
    return document.acknowledged


def get_single_record(document_id):
    data= collection.find_one({'_id': ObjectId(document_id)})
    return data


def get_multiple_record():
    data = collection.find()
    return list(data)


def remove_record(document_id):
    document = collection.delete_one({'_id': ObjectId(document_id)})
    return document.acknowledged


# Close Database
connection.close()


# # insert record
# data = {"Name": "Arun","Address": "goregoan"}
# id = insert_record(data)
# print(id)
#
# # retrive sepecific record
# document_id ='5e7b16e13b61b22a8d54c2b5'
# record= get_single_record(document_id)
# print(record)
#
# # retrive all record
# record = get_multiple_record()
# print(record)
#
# # update specific record
# document_id ='5e7b16e13b61b22a8d54c2b5'
# data = {'Name': 'Hiren'}
# ack = update_existing(document_id, data)
# print(ack)
#
# # remove specific record
# document_id ='5e7b16e13b61b22a8d54c2b5'
# ack = remove_record(document_id)
# print(ack)
#
# # update specific record if not exist _id then create records.
# document_id ='5e7b16e13b61b22a8d54c2b5'
# data = {'Name': 'Hiren',"Address": "vivar"}
# ack = update_or_create(document_id, data)
# print(ack)