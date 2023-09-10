from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.logger import logging


STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config_manager = ConfigurationManager()
            data_ingestion_config = config_manager.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            
        except Exception as e :
            raise e