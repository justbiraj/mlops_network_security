import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            data= pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = json.loads(data.T.to_json()).values()
            return list(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGODB_URI)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            logger.logging.info(f"Data inserted successfully into {self.database}.{self.collection}")
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    database = "network_security_db"
    collection ="NetworkData"
    network_object = NetworkDataExtract()
    records = network_object.csv_to_json_converter(file_path=FILE_PATH)
    num_records = network_object.insert_data_to_mongodb(records=records, database=database, collection=collection)
    print(f"Number of records inserted: {num_records}")