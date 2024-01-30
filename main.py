from textsummerizer.pipeline.stage_01_data_ingetion import DataIngetionTrainingPipeline
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