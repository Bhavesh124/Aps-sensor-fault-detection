from sensor import utils
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact 
from sensor.exception import SensorException
from sensor.logger import logging
import pandas as pd
import numpy as np 
import os,sys
from sklearn.model_selection import train_test_split

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Exporting Collection data as pandas dataframe")
            #Exporting collection data as pandas dataframe
            df:pd.DataFrame = utils.get_collections_as_dataframe(
                database_name = self.data_ingestion_config.database_name, 
                collection_name = self.data_ingestion_config.collection_name)

            logging.info("save data in feature store")
            
            #replace na with nan
            df.replace(to_replace="na",value=np.nan,inplace=True)

            #save data in feature store
            logging.info("create feature store if not available")
            #create fea if not available
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exist_ok=True)
            #Save df to feature store folder
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=False,header=True)

            logging.info("split dataset into train and test set")
            #split dataset into train and test set
            train_df,test_df = train_test_split(df,test_size=self.data_ingestion_config.test_size,random_state=42)

            logging.info("create dataset directory folder if not available")
            #create dataset directory folder if not available
            dataset_dir=os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir,exist_ok=True)

            logging.info("save df to feature store folder")
            #save dfto feature store folder
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path,index=False,header=True)
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path,index=False,header=True)

            #prepare artifact
            data_ingestion_artifact=DataIngestionArtifact(
                feature_store_file_path = self.data_ingestion_config.feature_store_file_path,
                train_file_path = self.data_ingestion_config.train_file_path,
                test_file_path = self.data_ingestion_config.test_file_path)

            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise SensorException(e, sys)