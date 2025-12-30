from pymongo import MongoClient

from bson.objectid import ObjectId


def get_connection():
    client = MongoClient(
        host='localhost',
        port=27017,
        # username='user',
        # password='pass',
        # authSource='admin'
    )
    db = client['contactsdb']
    collection = db['contacts']
    return collection


class DatabaseService:

    @staticmethod
    def get_all_contacts(collection):
        contacts = []
        for contact in collection.find():
            contact["_id"] = str(contact["_id"])
            contacts.append(contact)
        return contacts


    @staticmethod
    def create_contact(first_name,last_name,phone_number,collection):
        document = {
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number
        }
        result = collection.insert_one(document)
        return result.inserted_id


    @staticmethod
    def update_contact(contact_id, first_name, last_name, phone_number,collection):
        result = collection.update_one(
            {"_id": ObjectId(contact_id) },
            {"$set": {"first_name": first_name, "last_name": last_name,"phone_number":phone_number}}  # update
        )
        return result.matched_count > 0

    @staticmethod
    def delete_contact(contact_id,collection):
        result = collection.delete_one({"_id": ObjectId(contact_id)})
        return result.deleted_count > 0



















