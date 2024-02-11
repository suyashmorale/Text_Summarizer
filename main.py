from textsummerizer.pipeline.stage_01_data_ingetion import DataIngetionTrainingPipeline
from textsummerizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummerizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummerizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textsummerizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textsummerizer.logging import logger

STAGE_NAME = 'Data Ingetion Stage'
try:
    logger.info(f'Started {STAGE_NAME}')
    data_ingestion = DataIngetionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'Completed {STAGE_NAME}')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f'Started {STAGE_NAME}')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'Completed {STAGE_NAME}')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation Stage'
try:
    logger.info(f'Started {STAGE_NAME}')
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f'Completed {STAGE_NAME}')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Training Stage'
try:
    logger.info(f'===================== Started {STAGE_NAME} =====================\n')
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f'================= Completed {STAGE_NAME} =====================\n')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Model Evalutaion Stage'
try:
    logger.info(logger.info(f'\n===================== Started {STAGE_NAME} =====================\n'))
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(logger.info(f'\n===================== completed {STAGE_NAME} =====================\n'))
except Exception as e:
    logger.exception(e)
    raise e
