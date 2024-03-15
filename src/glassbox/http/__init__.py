from logging import Logger
from typing import Optional, Dict, Tuple, Any

from urllib.parse import urlencode
from requests import Response

class HTTPClient(object):
    def __init__(
        self,
        logger: Logger,
        timeout: Optional[float] = None
    ) -> None:

        self.logger = logger
        self.timeout = timeout
    
    def request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str,object]],
        data: Optional[Dict[str,object]],
        auth: Optional[Dict[str,str]],
        headers: Optional[Tuple[str,str]],
        timeout: Optional[float],
        allow_redirects: bool = False
    ) -> None: # fix later
        raise SystemError("This is an abstract class.")
    
    def debug_request(self, kwargs: Dict[str, Any]) -> None:
        self.logger.debug("### START GLASSBOX API REQUEST ###")
        self.logger.debug(f'{kwargs["method"]}: {kwargs["url"]}')

        if kwargs["params"]:
            self.logger.debug(f'{urlencode(kwargs["params"])}')

        if kwargs["headers"]:
            self.logger.debug(f'{urlencode(kwargs["params"])}')
        self.logger.debug("### STOP GLASSBOX API REQUEST ###")

    def debug_response(self, status_code: int, response: Response) -> None:
        self.logger.debug(f"Response Status Code: {status_code}")
        self.logger.debug(f"Response Headers: {response.headers}")

