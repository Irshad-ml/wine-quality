from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_validation import DataValidation



class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validation_all_columns()
        except Exception as e:
            raise e