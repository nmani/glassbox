from typing import List
from pydantic import (
    BaseModel,
    RootModel,
    ValidationError,
    ValidationInfo,
    field_validator,
    IPvAnyAddress
)

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
    sessionTags: str #Specific to the org/ap/app. Fix to be generic
    sessionCurrentDimensions: str #Fix to dict()
    avgDownloadTime: int
    avgResponseSize: int
    sessionStartTimeTS: int
    sessionEndTimeTS: int
    numOfPages: int
    queryId: str