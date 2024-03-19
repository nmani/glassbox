from ast import AsyncFunctionDef
import logging
from typing import Dict, Optional, Tuple

from ..http import HTTPClient
from requests import Request, Session, hooks
from requests.adapters import HTTPAdapter

_logger = logging.getLogger(__name__)
class GlassboxHTTPClient(HTTPClient):
    def __init__(
        self,
        logger: logging.Logger = _logger,
        request_hooks: Optional[Dict[str, object]] = None,
        timeout: Optional[float] = None,
        proxy: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = 3
    ) -> None:
        super().__init__(logger, timeout)
        self.session = Session()
        self.session.mount("https://", HTTPAdapter(max_retries=max_retries))

        self.request_hooks = request_hooks or hooks.default_hooks()
        self.proxy = proxy if proxy else {}
    
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
    ):
        session = self.session or Session()

        kwargs = {
            "method": method.upper(),
            "url": url,
            "params": params,
            "headers": headers,
            "auth": auth,
            "hooks": self.request_hooks,
            "json": data
        }
        req = Request(**kwargs)
        req_prep = session.prepare_request(req)

        # Add logic for verify/certs? Fix me
        settings = session.merge_environment_settings(
            req_prep.url, self.proxy, None, None, None
        )

        self.debug_request(req)
        resp = session.send(
            req_prep,
            allow_redirects=allow_redirects,
            timeout=timeout,
            **settings,
        )

        self.debug_response(resp.status_code, resp)
        output = int(resp.status_code), resp.text, resp.headers

        return output
        
    