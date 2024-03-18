from datetime import datetime, timedelta, UTC
from typing import Any, Annotated, List, Dict
from pydantic import (
    Field,
    BaseModel,
    PastDatetime)
import logging.config
import yaml

# Load the config file
with open('logger_conf.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# Get a logger object
logger = logging.getLogger(__name__)

# need to put you in utils later...
def _default_searchts(hours_back: int = 168):
    return datetime.now(UTC) - timedelta(hours=hours_back)


class SessionDetail(BaseModel):
    sessionguid: str
    mergeSessions: bool = False
    startsTime: PastDatetime = Field(default_factory=_default_searchts)

    @field_validator("sessionguid")
    @classmethod
    def validator_str(cls, v: str) -> str:
        try:
            if not isinstance(v, str):
                logger.error(f"Value is not a string: {v}")
                raise ValueError("Value is not a string")
            return v
        except Exception as e:
            logger.error(f"Error validating sessionguid: {e}")
            raise e