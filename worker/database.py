import os
from datetime import datetime, UTC

from pymongo import MongoClient


def save_interface_status(router_ip, interfaces):
    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DB_NAME")

    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db["interface_status"]

    data = {
        "router_ip": router_ip,
        "timestamp": datetime.now(UTC),
        "interfaces": interfaces,
    }
    collection.insert_one(data)
    client.close()
