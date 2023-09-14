from src.mlproject.logger import logging
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline




if __name__ == "__main__" :
    try:
        STAGE_NAME = "Data Ingestion Stage"
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<")
        
        STAGE_NAME = "Data Validation Stage"
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
        data_ingestion = DataValidationTrainingPipeline()
        data_ingestion.main()
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<")
        
    except Exception as e:
        logging.exception(e)
        raise e