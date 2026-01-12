from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    
    def __init__(self):
        pass
    
    def main(self):
        
        obj=ConfigurationManager()
        data_validation_config=obj.get_data_validation_config()
        data_validation=DataValidation(data_validation_config)
        data_validation.validate_columns()
        
        