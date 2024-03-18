
from pydantic import (
    BaseModel,
    field_validator)

import logging.config
import yaml

# Load the config file
with open('logger_conf.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# Get a logger object
logger = logging.getLogger(__name__)

class HTTPStatusCode(BaseModel):
    code: int
    count: int

    @field_validator("code","count")
    @classmethod
    def validator_ints(cls, v: int) -> int:
        if not isinstance(v, int):
            logger.error(f"Value is not an integer: {v}")
            raise ValueError("Value is not an integer")
        if v < 0:
            logger.error(f"Value is not a positive integer: {v}")
            raise ValueError("Value is not a positive integer")
        return v
    