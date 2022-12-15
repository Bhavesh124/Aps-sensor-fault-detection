from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collections_as_dataframe
import sys,os
from sensor.entity import config_entity
from sensor.components.dataingestion import DataIngestion
from sensor.components.datavalidation import DataValidation


'''def test_logger_and_exception():
    try:
        result = 3/10
        print(result)
    except Exception as e:
        raise SensorException(e,sys)'''


if __name__=="__main__":
    try:
        #get_collections_as_dataframe(database_name="aps",collection_name="sensor")
        training_pipeline_config = config_entity.TrainingPipelineConfig()

         #data ingestion
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config) 
        print(data_ingestion_config.to_dict())
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        #data validation
        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config = training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,
                                        data_ingestion_artifact=data_ingestion_artifact)
        data_validation_artifact = data_validation.initiate_data_validation()
        
    except Exception as e:
        print(e)
