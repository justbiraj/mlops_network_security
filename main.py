from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidaion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


import sys


if __name__=='__main__':

    # try:
    taningpipelineconig=TrainingPipelineConfig()
    dataingestionconfig = DataIngestionConfig(taningpipelineconig)
    data_ingestion = DataIngestion(dataingestionconfig)
    datainjestionarfificts = data_ingestion.initiate_data_ingestion()
    logging.info("ingees comp")
    print(datainjestionarfificts)
    daravalidationconfig = DataValidationConfig(taningpipelineconig)
    daravalidation = DataValidaion(datainjestionarfificts,daravalidationconfig)
    datadalidartif=daravalidation.initiate_data_validation()
    print(datadalidartif )

    
    
    # except Exception as e:
    #     raise NetworkSecurityException(e, sys)
