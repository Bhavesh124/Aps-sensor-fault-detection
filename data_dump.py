import pymongo
import pandas as pd
import json
import os
from sensor.config import mongo_client

# mongodb_url = os.getenv('MONGO_DB_URL')
# client = pymongo.MongoClient(mongodb_url)

DATA_FILE_PATH = (r"C:\Users\Ranjit Singh\Desktop\Aps-sensor-fault-detection\aps_failure_training_set1.csv")
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns:{df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    print("inserted documented :- ",mongo_client[DATABASE_NAME][COLLECTION_NAME].count_documents())