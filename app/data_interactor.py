from pymongo import MongoClient
from contact import Contact
from bson.objectid import ObjectId
import os


def get_connection():
    mongo_host = os.getenv("MONGO_HOST", "localhost")
    mongo_port = int(os.getenv("MONGO_PORT", 27017))
    mongo_db = os.getenv("MONGO_DB", "contactsdb")

    client = MongoClient(host=mongo_host, port=mongo_port)
    db = client[mongo_db]
    return db["contacts"]


class DatabaseService:

    @staticmethod
    def get_all_contacts(collection):
        contacts = []
        for document in collection.find():
            document = Contact(
                id = str(document["_id"]),
                first_name = document["first_name"],
                last_name =document["last_name"],
                phone_number = document["phone_number"]
            )
            contacts.append(document)
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



















