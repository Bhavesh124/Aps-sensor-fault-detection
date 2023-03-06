import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    target_column:str = os.getenv('TARGET_COLUMN')
    aws_acess_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_acess_key:str = os.getenv("AWS_SECRET_ACESS_KEY")

env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN= env_var.target_column