from src.mlProject.Logging import get_logger

logger=get_logger(__name__)
from src.mlProject.pipeline.data_ingestion_stage import DataIngestionTrainingPipeline
from src.mlProject.pipeline.data_validation_stage import DataValidationTrainingPipeline



STAGE_NAME='Data_ingestion_training_pipeline'

if __name__=='__main__':
    
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
        STAGE_NAME="Data_validation_training_pipeline"
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e
    

