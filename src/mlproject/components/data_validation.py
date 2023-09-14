import os
from src.mlproject.logger import logging
from src.mlproject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config
        
    def validation_all_columns(self) -> bool:
        try:
            validation_status=None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)
            all_schema = list(self.config.all_schema.keys())
            for col in all_columns:
                if col in all_schema:
                    validation_status=True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status:{validation_status}")
                else:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        
            return validation_status
        except Exception as e:
            raise e
                