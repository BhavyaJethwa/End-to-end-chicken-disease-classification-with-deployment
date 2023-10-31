from Chicken_disease_classification import logger

from Chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Chicken_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

Stage_name1 = "Data Ingestion"


try:
    logger.info(f"{Stage_name1} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{Stage_name1} Completed")

except Exception as e:
    logger.exception(e)
    raise e

Stage_name2 = "Prepare base model"


try:
    logger.info(f"{Stage_name2} started")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"{Stage_name2} Completed")

except Exception as e:
    logger.exception(e)
    raise e
