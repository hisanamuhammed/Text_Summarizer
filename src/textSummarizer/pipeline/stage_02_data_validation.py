from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_validation import DataValidation
from src.textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_Validation_config = config.get_data_validation_config()
        data_Validation = DataValidation(config=data_Validation_config)
        data_Validation.validate_all_files_exist()