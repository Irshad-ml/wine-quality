from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
            try:
                config = ConfigurationManager()
                data_transform_config=config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transform_config)
                data_transformation.train_test_split()
                
            except Exception as e:
                raise e