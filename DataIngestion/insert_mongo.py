import json
from pymongo import MongoClient


MONGO_URI = "mongodb://localhost:27017"

DB_NAME = "Handler_Threat_intel"
COLLECTION_NAME = "ip_reports"


def insert_indicators(data):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    if data:
        collection.insert_many(data)
        print(f"✅ Inserted {len(data)} indicators into MongoDB")
    else:
        print("⚠️ No data to insert")


if __name__ == "__main__":
    with open("normalized_indicators.json", "r") as f:
        normalized_data = json.load(f)

    insert_indicators(normalized_data)
