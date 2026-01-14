from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass
class DataValidationConfig:
    root_dir: Path
    local_data_file: Path
    status_file: str
    schema: dict
    

@dataclass
class DataTransformationConfig:
    root_dir: Path
    local_data_file: Path
    train_csv: Path
    test_csv: Path
    X_train_trans: Path
    X_test_trans: Path
    y_train: Path
    y_test: Path
    target_column: str
    
@dataclass
class ModelTrainingConfig:
    root_dir: Path
    X_train_trans: Path
    X_test_trans: Path
    y_train: Path
    y_test:  Path
    model_name: str