from datetime import datetime, timedelta, UTC
from typing import Any, Annotated, List, Dict, TypeVar, Optional, Union
import re
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

# need to put you in utils later...
def _default_searchts(hours_back: int = 168):
    return datetime.now(UTC) - timedelta(hours=hours_back)


class SessionDetail(BaseModel):
    sessionguid: str
    mergeSessions: bool = False
    startsTime: PastDatetime = Field(default_factory=_default_searchts)

# Add logic for queries later?
class SessionsSearch(BaseModel):
    sessionguid: Union[str, List[str], None] = None
    limit: Annotated[int, Field(strict=True, gt=0, le=5000)] = 100
    starts: PastDatetime = Field(default_factory=_default_searchts)
    endts: PastDatetime = Field(default_factory=lambda: datetime.now(UTC))

class Credentials(BaseModel):
    username: str
    password: str

    @field_validator('password')
    @classmethod
    def password_validator(cls,v:str):
        password_regex = "((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})"
        if not re.match(password_regex, v):
            raise ValueError("Password must be 8-64 characters and contain at least one number, one uppercase letter, one lowercase letter, and one special character")
        return v    
    

class Config(BaseModel):
    GLASSBOX_CREDS: Credentials
    GLASSBOX_BASEURL: Annotated[AnyUrl, UrlConstraints(
        max_length=300, allowed_schemes=["http", "https"], host_required=True
    )]

    @field_validator("GLASSBOX_BASEURL")
    @classmethod
    def _chk_baseurl(cls, v: str, info: ValidationError):
        pass

class HTTPStatusCode(BaseModel):
    code: int
    count: int

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
    sessionCurrentDimensions: Dict[str] #Fix to dict()
    avgDownloadTime: int
    avgResponseSize: int
    sessionStartTimeTS: PastDatetime
    sessionEndTimeTS: PastDatetime
    numOfPages: int
    queryId: str

    @field_validator('resultCode')
    @classmethod
    def validate_resultcode(cls, v:int):
        if v != 0:
            raise ValueError("Result code is not 0")
        elif v <= 0:
            raise ValueError("Result code is not a positive integer")
        return v
    
    
    