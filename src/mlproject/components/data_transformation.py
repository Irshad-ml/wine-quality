import os
from src.mlproject.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from src.mlproject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config
        
    # Here we can perform all kind of DataPreprocessing steps before the data to the model
    # Handle Missing values , Duplicated records and Outliers
    # Feature Engineering  and data transformation (Scaling and OnehotEncoded)
    
    def train_test_split(self):
        data_df = pd.read_csv(self.config.data_path)
        train_df , test_df = train_test_split(data_df,test_size=0.25,random_state=25)
        
        train_df.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test_df.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        
        logging.info("Splitted data into train and test")
        logging.info(f"Shape of the train data: {train_df.shape}")
        logging.info(f"Shape of the train data: {test_df.shape}")
        
        print(f"Shape of the train data: {train_df.shape}")
        print(f"Shape of the train data: {test_df.shape}")