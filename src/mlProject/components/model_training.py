from src.mlProject.entity.config_entity import ModelTrainingConfig
from sklearn.ensemble import RandomForestClassifier
import joblib



class ModelTraining:
    def __init__(self,config: ModelTrainingConfig):
        self.config=config
        
    
    def train(self):
        rf=RandomForestClassifier()
        X_train_trans=joblib.load(self.config.X_train_trans)
        X_test_trans=joblib.load(self.config.X_test_trans)
        y_train=joblib.load(self.config.y_train)
        rf.fit(X_train_trans,y_train)
        
        joblib.dump(rf,self.config.model_name)
        