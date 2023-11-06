from Chicken_disease_classification.config.configuration import ConfigurationManager
from Chicken_disease_classification.components.evaluation import Evaluation
from Chicken_disease_classification import logger

stage_name = "Evaluation"

class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()