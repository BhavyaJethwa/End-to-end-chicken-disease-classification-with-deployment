from Chicken_disease_classification.config.configuration import ConfigurationManager
from Chicken_disease_classification.components.Training_model import Training
from Chicken_disease_classification import logger

stage_name = "Training"

class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()