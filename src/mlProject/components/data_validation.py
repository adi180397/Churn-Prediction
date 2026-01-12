import pandas as pd
from src.mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config=config
    
    def validate_columns(self):
        validation_satage=None
        df=pd.read_csv(self.config.local_data_file)
        columns=list(df.columns)
        all_schema=self.config.schema.keys()
        for column in columns:
            if column not in all_schema:
                validation_satage=False
                
                with open(self.config.status_file,'w') as f:
                    f.write('validation_stage : {}'.format(validation_satage))
            
            else:
                validation_satage=True
                with open(self.config.status_file,'w') as f:
                    f.write('validation_stage : {}'.format(validation_satage))
                    
        return validation_satage
    
                
            
        
        
        
        