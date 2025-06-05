from requests import request as req
from dataclasses import dataclass
from typing import DefaultDict
import toml

ALLOWED_METHODS = ["get", "post", "delete", "patch"]

@dataclass
class ApiRequestHandler: 
    endpoint: str
    params: dict
    json: dict
    method: str = "get"
    base_url: str = "https://infrajp.jaupesca.com.br"
    
    def make_api_call(
        self 
    ) -> dict:
        if self.method.lower() not in ALLOWED_METHODS:
            raise ValueError
        resp = req(
            method=self.method,
            url=f"{self.base_url}/{self.endpoint}",
            params=self.params,
            json=self.json
            )
        return resp.json()
    