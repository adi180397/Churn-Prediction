
from src.mlProject.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
from src.mlProject.Logging import get_logger

logger=get_logger(__name__)

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config
        
        pass
    
    def drop_columns(self):
        df=pd.read_csv(self.config.local_data_file)
        df.drop(columns=['City','Signup_Quarter'],inplace=True)
        return df
    
    def train_test_split(self):
        df=self.drop_columns()
        train,test=train_test_split(df,test_size=0.2,random_state=42)
        train.to_csv(self.config.train_csv,index=False)
        test.to_csv(self.config.test_csv,index=False)
        
        logger.info("data splitted in to training and test sets")
        
        
        
        