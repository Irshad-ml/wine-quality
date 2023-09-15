import os
import urllib.request as request
import zipfile
from  pathlib import Path
from src.mlproject.logger import logging
from src.mlproject.utils.common import get_size
from src.mlproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
        
    def download_file(self):
        print("source file:",self.config.source_url)
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_url,
                filename=self.config.local_data_file
            )
            
            print(f"header from urlretrieves{headers}")
            logging.info(f"{filename} downloaded successfully ")
            
        else:
            logging.info(f"file already exist of size {get_size(Path(self.config.local_data_file))}")
            
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        