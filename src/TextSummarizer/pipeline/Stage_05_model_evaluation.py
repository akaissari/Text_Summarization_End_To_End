from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.evaluation import ModelEvaluation
from TextSummarizer.logging import logger


STAGE_NAME = "Data Evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_model_evaluation_config()
        evaluator = ModelEvaluation(config=evaluation_config)
        evaluator.evaluate()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e