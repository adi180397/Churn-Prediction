from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_training import ModelTraining

class ModelTrainingPipeline:
    
    def __init__(self):
        pass
    
    def main(self):
        
        obj=ConfigurationManager()
        model_training_config=obj.get_model_training_config()
        model_trainer_obj=ModelTraining(model_training_config)
        model_trainer_obj.train()