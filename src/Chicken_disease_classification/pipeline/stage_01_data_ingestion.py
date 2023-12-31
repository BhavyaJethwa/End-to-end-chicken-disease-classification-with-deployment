from Chicken_disease_classification.config.configuration import ConfigurationManager
from Chicken_disease_classification.components.data_ingestion import DataIngestion
from Chicken_disease_classification import logger



Stage_name = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__ == "__main__":
    try:
        logger.info(f"{Stage_name} started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{Stage_name} Completed")

    except Exception as e:
        logger.exception(e)
        raise e


















try:
    
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config = data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip_file()

except Exception as e :
    raise e 