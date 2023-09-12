import os,sys 
from datetime import datetime

# artifact -> pipeline folder -> timestramp -> output

def get_current_time_stramp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


CURRENT_TIME_STRAMP = get_current_time_stramp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = "Data"
DATA_DIR_KEY = "finalTrain.csv"


# New_machine_learning/Data_Dir/Data_Dir/Key

ARTIFACT_DIR_KEY = "Artifact"

# Data Ingstion related variable
DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"

# Data Transformation related variable

DATA_TRANSFORMATION_ARTIFACT = "data_transformation"
DATA_PREPROCESSED_DIR = "processor"
DATA_TRANSFORMATION_PROCESSING_OBJ = "processor.pkl"
DATA_TRANFORMATION_DIR = "transformation"
TRANSFROM_TRAIN_DIR_KEY = "train.csv"
TRANSFROM_TEST_DIR_KEY = "test.csv"

# artifact / data_transformation /(processor -> processor.pkl and feature_engg.pkl) and (transfromation -> train.csv and test.csv)

# Model Training

MODEL_TRAINER_KEY = "model_trainer"
MODEL_OBJECT = "model.pkl"
