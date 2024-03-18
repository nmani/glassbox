from typing import Any, Annotated, List, TypeVar, Optional, Union
from clickstream_model import ClickStream
from httpstatuscode_model import HTTPStatusCode
from sessionsearch_model import SessionsSearch
from pydantic import BaseModel, IPvAnyAddress, PastDatetime, field_validator, create_model

import logging.config
import yaml

# Load the config file
with open('logger_conf.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# Get a logger object
logger = logging.getLogger(__name__)


class GBFullSession(BaseModel):
    session_id: str
    resultCode: int 
    ClickStream: List[ClickStream]
    httpStatusCodes: List[HTTPStatusCode]
    clientIPs: List[IPvAnyAddress]
    serverIPs: List[IPvAnyAddress]
    userAgent: str
    userNames: str
    appIds: List[int]
    sessionTags: Any #Specific to the org/ap/app. Fix to be generic?
    sessionCurrentDimensions:  Optional[create_model('sessionCurrentDimensions',type=(str, ...))] #need to ask if i need to make a python file that handles the dict
    avgDownloadTime: int
    avgResponseSize: int
    sessionStartTimeTS: SessionsSearch.starts
    sessionEndTimeTS: SessionsSearch.endts
    numOfPages: int
    queryId: str

    
    @field_validator("userAgent")
    @classmethod
    def validate_userAgent(cls, v:str) -> str:
        try:
            if not isinstance(v, str):
                logger.error(f"Value is not a string: {v}")
                raise ValueError("Value is not a string")
                logger.error(f"User agent is not valid: {v}")
            return v
        except Exception as e:
            logger.error(f"Error in user agent validation: {e}", exc_info=True)
    @field_validator("appIds")
    @classmethod
    def validate_int_list(cls,v:List[int]) -> List[int]:
        try:
            if not isinstance(v, list):
                logger.error(f"Value is not a list: {v}")
                raise ValueError("Value is not a list")
            elif len(v) == 0:
                logger.error(f"List is empty: {v}")
                raise ValueError("List is empty")
            return v
        except Exception as e:
            logger.error(f"Error in list validation: {e}", exc_info=True)

    @field_validator("resultCode","avgDownloadTime","avgResponseSize","numOfPages")
    @classmethod
    def validate_ints(cls, v:int) -> int:
        try:
            if not isinstance(v, int):
                logger.error(f"Value is not an integer: {v}")
                raise ValueError("Value is not an integer")
            elif v <= 0:
                logger.error(f"Value is not a positive integer: {v}")
                raise ValueError("Value is not a positive integer")
            return v
        except Exception as e:
            logger.error(f"Error in integer validation: {e}", exc_info=True)
