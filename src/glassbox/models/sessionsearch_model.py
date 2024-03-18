from datetime import datetime, timedelta, UTC
from typing import Any, Annotated, List, Dict, Union


from pydantic import (
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

def _default_searchts(hours_back: int = 168):
    return datetime.now(UTC) - timedelta(hours=hours_back)

class SessionsSearch(BaseModel):
    sessionguid: Union[str, List[str], None] = None
    limit: Annotated[int, Field(strict=True, gt=0, le=5000)] = 100
    starts: PastDatetime = Field(default_factory=_default_searchts)
    endts: PastDatetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator("limit")
    @classmethod
    def validate_limit(cls, v: int) -> int:
        if not isinstance(v, int):
            logger.error(f"Value is not an integer: {v}")
            raise ValueError("Value is not an integer")
        if v < 0:
            logger.error(f"Value is not a positive integer: {v}")
            raise ValueError("Value is not a positive integer")
        if v > 5000:
            logger.error(f"Value is greater than 5000: {v}")
            raise ValueError("Value is greater than 5000")
        return v
