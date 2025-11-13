from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidaion
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
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
    datatransformationconfig = DataTransformationConfig(taningpipelineconig)
    print(datadalidartif )
    datatransfformation = DataTransformation(datadalidartif,datatransformationconfig)
    datatransarti=datatransfformation.initiate_data_transformation()
    print(datatransarti)


    
    
    # except Exception as e:
    #     raise NetworkSecurityException(e, sys)
