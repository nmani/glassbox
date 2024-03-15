from typing import Any, Union, Optional, Dict
from os import environ
from urllib.parse import urlparse
from .models import Config, Credentials

class Configuration:
    def __init__(
            self, *, 
            credentials: Optional[Dict[str, str]],
            baseurl: str = "",
            connection_timeout: float = 300, 
            connection_verify: Union[bool, str] = False,
            **kwargs: Any
    ) -> None:
        self.glassbox_baseurl = baseurl
        self.credentials = credentials
        self.baseurl = baseurl

    def _baseurl_parse(self):
        parse_url= urlparse(self.baseurl)

    def _authcreds(self):
        if self.credentials:
            return Credentials(
                username=self.credentials['username'],
                password=self.credentials['password'],
                )


    
