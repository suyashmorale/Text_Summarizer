from textsummerizer.config.configuration import ConfigurationManager
from textsummerizer.components.model_evaluation import ModelEvaluation


class ModelEvaluationTrainingPipeline:
    config = ConfigurationManager()
    model_evaluation_config = config.get_model_evalution_config()
    model_evaluation = ModelEvaluation(config=model_evaluation_config)
    model_evaluation.eval()
