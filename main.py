from Chicken_disease_classification import logger

from Chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

Stage_name = "Data Ingestion"


try:
    logger.info(f"{Stage_name} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{Stage_name} Completed")

except Exception as e:
    logger.exception(e)
    raise e

