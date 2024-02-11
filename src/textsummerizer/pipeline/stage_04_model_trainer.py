from textsummerizer.config.configuration import ConfigurationManager
from textsummerizer.components.model_trainer import ModelTrainer


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_training_config)
        model_trainer.train()