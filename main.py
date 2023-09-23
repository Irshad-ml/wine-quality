from src.mlproject.logger import logging
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.mlproject.pipeline.stage_04_model_trainer import ModelTrainerPipeline

if __name__ == "__main__" :
    try:
        #we can write all below code in single method create list of stages and unser for loop execute this code
        STAGE_NAME = "Data Ingestion Stage"
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<")
        logging.info(f"------------------------------------------------------")
        
        STAGE_NAME = "Data Validation Stage"
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<")
        logging.info(f"------------------------------------------------------")
        
        STAGE_NAME = "Data Transformation Stage"
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} started <<<<<<<<<<")
        data_transform = DataTransformationTrainingPipeline()
        data_transform.main()
        logging.info(f">>>>>>>>>>>stage {STAGE_NAME} completed <<<<<<<<<")
        
        
        STAGE_NAME = "Model Trainer Stage"
        logging.info(f">>>>>>>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<<")
        model_trainer = ModelTrainerPipeline()
        model_trainer.main()
        logging.info(f">>>>>>>>>>>>>>>>{STAGE_NAME} completed <<<<<<<<<<<<<")
        
        
        
        
    except Exception as e:
        logging.exception(e)
        raise e