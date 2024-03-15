from typing import Dict
from .http.http_client import GlassboxHTTPClient
from .models import GBFullSession, Credentials
from .config import Configuration

class GlassboxClient:
    def __init__(self, baseurl: str, *, credentials: Dict[str,str], **kwargs) -> None:
        pass

    def login(self):
        pass

    def _chk_baseurl(self):
        pass

    def __enter_(self):
        pass

    def __exit__(self, *exc_details):
        pass

output = GlassboxClient(baseurl='https:///', credentials={"username": "asdfasdfdfs", "asdfsa11df": "adsadsfdsa"})