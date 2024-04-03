import os
import requests
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.utils.common import *
from src.textSummarizer.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        '''if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"Downloaded {filename} with following headers: \n{headers}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists of size {get_size(Path(self.config.local_data_file))}") '''
     
        if not os.path.exists(self.config.local_data_file):
            response = requests.get(self.config.source_URL)
            with open(self.config.local_data_file, 'wb') as f:
                f.write(response.content)
            logger.info(f"Downloaded {self.config.local_data_file} from {self.config.source_URL}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists of size {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)