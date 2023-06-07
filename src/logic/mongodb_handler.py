import pymongo
import uuid


def user_db_handler(steamid, server, db, collection):
    client = pymongo.MongoClient(server)
    db = client[db]
    collection = db[collection]

    existing_document = collection.find_one({'steamid': steamid})

    if existing_document:
        print(f"Document with steamid {steamid} already exists.")
        userId = existing_document['userId']
        token = existing_document['token']
        return userId, token
    else:
        userId = str(uuid.uuid4())
        token = str(uuid.uuid4())

        new_document = {
            'steamid': steamid,
            'userId': userId,
            'token': token
        }

        collection.insert_one(new_document)
        return userId, token

