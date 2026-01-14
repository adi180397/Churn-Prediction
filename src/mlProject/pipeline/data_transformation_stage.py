from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_transformation import DataTransformation

class DataTranformationPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        
        obj_manager=ConfigurationManager()
        data_tranformation_config=  obj_manager.get_data_datatransformation()

        obj_trans=DataTransformation(data_tranformation_config)

        obj_trans.train_test_split()
        obj_trans.transformed()