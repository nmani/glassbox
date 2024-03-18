
from pydantic import BaseModel, IPvAnyAddress, field_validator
import logging.config
import yaml

# Load the config file
with open('logger_conf.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

# Configure the logging module with the config file
logging.config.dictConfig(config)

# Get a logger object
logger = logging.getLogger(__name__)


class ClickStream(BaseModel):
    analyzerId: str
    componentID: int
    cookiesbytes: int
    customerDimensions: str
    downloadtime: int
    httpresponsecode: int
    labels: str | None = None
    pageIds: str
    pages: str
    probeId: str
    responsesize: int
    serverip: IPvAnyAddress
    tags: str
    timestamp: int
    str: str
    uri: str
    uuid: str

    @field_validator("analyzerId","customerDimensions","pageIds","pages","probeId","str","uri","uuid")
    @classmethod
    def validator_str(cls, v: str) -> str:
        if not isinstance(v, str):
            logger.error(f"Value is not a string: {v}")
            raise ValueError("Value is not a string")
        return v
    
    @field_validator("componentID","cookiesbytes","downloadtime","httpresponsecode","responsesize","timestamp")
    @classmethod
    def validator_int(cls, v: int) -> int:
        if not isinstance(v, int):
            logger.error(f"Value is not an integer: {v}")
            raise ValueError("Value is not an integer")
        if v < 0:
            logger.error(f"Value is not a positive integer: {v}")
            raise ValueError("Value is not a positive integer")
        return v