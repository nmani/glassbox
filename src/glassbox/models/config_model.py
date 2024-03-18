
from typing import Any, Annotated, List, Dict, TypeVar, Optional, Union
import logging.config
from pydantic import (
    Field,
    AnyUrl,
    BaseModel,
    IPvAnyAddress,
    PastDatetime,
    RootModel,
    UrlConstraints,
    ValidationError,
    ValidationInfo,
    field_validator
)
import yaml
from credentials_model import Credentials
# Load the config file
with open('logger_conf.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# Get a logger object
logger = logging.getLogger(__name__)


class Config(BaseModel):
    GLASSBOX_CREDS: Credentials
    GLASSBOX_BASEURL: Annotated[AnyUrl, UrlConstraints(
        max_length=300, allowed_schemes=["http", "https"], host_required=True
    )]

    @field_validator("GLASSBOX_BASEURL")
    @classmethod
    def _chk_baseurl(cls, v: str, info: ValidationError):
        pass
