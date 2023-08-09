import logging
import os,sys
from datetime import datetime

# create directory
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR, exist_ok = True)

# create .log file with current time stramp log_2023_H_M_S.log
CURRENT_TIME_STRAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STRAMP}.log"

# output 

log_file_path = os.path.join(LOG_DIR,file_name)

# using basic config we create log directory
logging.basicConfig(filename = log_file_path,
                    filemode = "w",
                    format = '[%(asctime)s] %(name)s - %(levelname)s - %(message)s', 
                    level = logging.INFO )