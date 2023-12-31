from Chicken_disease_classification.components.prepare_base_model import PrepareBaseModel 
from Chicken_disease_classification.config.configuration import ConfigurationManager
from Chicken_disease_classification import logger

stage_name = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()




if __name__ == "__main__":
    try:
        logger.info(f"{stage_name} started")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"{stage_name} completed")
    except Exception as e:
        raise e 