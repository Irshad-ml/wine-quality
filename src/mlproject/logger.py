import logging
import os
from datetime import datetime


logging_format = "[%(asctime)s]: %(lineno)d %(module)s %(levelname)s %(message)s"

log_file_name = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

log_dir ='logs'
log_path = os.path.join(os.getcwd(),log_dir)
os.makedirs(log_path,exist_ok=True)

log_file_path = os.path.join(log_path,log_file_name)

logging.basicConfig(
    filename=log_file_path,
    format=logging_format,
    level=logging.INFO
    
)

