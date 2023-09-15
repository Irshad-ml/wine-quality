from src.mlproject.config.configuration import ConfigurationManager
from src.mlproject.components.data_transformation import DataTransformation
from pathlib import Path

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
            try:
                with open(Path('artifacts/data_validation/status.txt')) as f:
                    status =f.read().split(":")[1]
                if status =="True":                    
                    config = ConfigurationManager()
                    data_transform_config=config.get_data_transformation_config()
                    data_transformation = DataTransformation(data_transform_config)
                    data_transformation.train_test_split()
                else:
                    raise Exception("Your data schema is not valid")
                    
            except Exception as e:
                raise e