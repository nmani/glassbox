from pydantic import BaseModel, field_validator

import logging.config
import yaml

# Load the config file
with open('logger_conf.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# Get a logger object
logger = logging.getLogger(__name__)



class Credentials(BaseModel):
    username: str
    password: str

    @field_validator('username','password')
    @classmethod
    def validator_str(cls,v:str) -> str:
        try:
            if not isinstance(v, str):
                logger.error(f"Value is not a string: {v}")
                raise ValueError("Value is not a string")
            return v
        except Exception as e:
            logger.error(f"Error validating username or password: {e}")
            