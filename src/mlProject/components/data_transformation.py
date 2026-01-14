
from src.mlProject.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
from src.mlProject.Logging import get_logger
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from scipy.sparse import save_npz
import numpy as np
import joblib

logger=get_logger(__name__)

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config=config
        
        pass
    
    def drop_columns(self):
        df=pd.read_csv(self.config.local_data_file)
        df.drop(columns=['City','Signup_Quarter'],inplace=True)
        return df
    
    def fill_missing_data(self):
        df=self.drop_columns()
        df['Age']=df['Age'].fillna(df['Age'].median())
        df['Session_Duration_Avg']=df['Session_Duration_Avg'].fillna(df['Session_Duration_Avg'].mean())
        df['Pages_Per_Session']=df['Pages_Per_Session'].fillna(df['Pages_Per_Session'].mean())
        df['Wishlist_Items']=df['Wishlist_Items'].fillna(df['Wishlist_Items'].mean())
        df['Days_Since_Last_Purchase']=df['Days_Since_Last_Purchase'].fillna(df['Days_Since_Last_Purchase'].median())
        df['Discount_Usage_Rate']=df['Discount_Usage_Rate'].fillna(df['Discount_Usage_Rate'].mean())
        df['Returns_Rate']=df['Returns_Rate'].fillna(df['Returns_Rate'].mean())
        df['Email_Open_Rate']=df['Email_Open_Rate'].fillna(df['Email_Open_Rate'].mean())
        df['Customer_Service_Calls']=df['Customer_Service_Calls'].fillna(df['Customer_Service_Calls'].mean())
        df['Product_Reviews_Written']=df['Product_Reviews_Written'].fillna(df['Product_Reviews_Written'].mean())
        df['Social_Media_Engagement_Score']=df['Social_Media_Engagement_Score'].fillna(df['Social_Media_Engagement_Score'].mean())
        df['Mobile_App_Usage']=df['Mobile_App_Usage'].fillna(df['Mobile_App_Usage'].mean())
        df['Payment_Method_Diversity']=df['Payment_Method_Diversity'].fillna(df['Payment_Method_Diversity'].mean())
        df['Credit_Balance']=df['Credit_Balance'].fillna(df['Credit_Balance'].mean())
        
        return df
    
    
    
    def train_test_split(self):
        df=self.fill_missing_data()
        train,test=train_test_split(df,test_size=0.2,random_state=42)
        train.to_csv(self.config.train_csv,index=False)
        test.to_csv(self.config.test_csv,index=False)
        
        logger.info("data splitted in to training and test sets")
    
    
    def get_preprocessor(self,df: pd.DataFrame):
        num_pipeline=Pipeline(
            steps=[
                ("scaler", StandardScaler())
            ]
        )
        
        cat_pipeline=Pipeline(
            steps=[
                ('onehot',OneHotEncoder())
            ]
        )
        
        
        numerical_cols=df.select_dtypes(include=['int','float']).columns.tolist()
        numerical_cols.remove(self.config.target_column)
        
        cat_cols=df.select_dtypes(include=['object']).columns.tolist()
        
        
        preprocessor=ColumnTransformer(
            transformers=[
                ("num",num_pipeline,numerical_cols),
                ('cat',cat_pipeline,cat_cols)
            ]
        )
        
        return preprocessor
        
    def transformed(self):
        train_df=pd.read_csv(self.config.train_csv)
        test_df=pd.read_csv(self.config.test_csv)
        preprocessor =  self.get_preprocessor(train_df)
        X_train=train_df.drop(columns=[self.config.target_column])
        y_train=train_df[self.config.target_column]
        X_test=test_df.drop(columns=[self.config.target_column])
        y_test=test_df[self.config.target_column]
        
        X_train_transformed=preprocessor.fit_transform(X_train)
        X_test_transformed=preprocessor.transform(X_test)
        
        joblib.dump(X_train_transformed,self.config.X_train_trans)
        joblib.dump(X_test_transformed,self.config.X_test_trans)
        joblib.dump(y_train,self.config.y_train)
        joblib.dump(y_test,self.config.y_test)
       
        
        
        
    
        
        
        
        
        