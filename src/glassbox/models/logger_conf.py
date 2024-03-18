# Desc: Logger configuration file for the Glassbox application.
import os
import logging.config
import yaml


class GBlogger():
    def __init__(self) -> None:
        if not os.path.exists('logger_conf.yaml'):
            raise FileNotFoundError("Logging configuration file not found")
        with open('logger_conf.yaml','r') as f:
            configs = yaml.safe_load(f)
        logging.config.dictConfig(configs)
        self.logger = logging.getLogger('glassbox')
        self.logger.setLevel(logging.ERROR)
        self.logger.debug("Logger initialized")
