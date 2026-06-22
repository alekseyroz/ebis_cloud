"""Base HTTP client mixin for eBis Cloud API."""

from base64 import b64encode
from typing import Any

import httpx


class HttpMixin:
    _base_url: str
    _username: str
    _password: str

    def _auth_headers(self) -> dict[str, str]:
        token = b64encode(f"{self._username}:{self._password}".encode()).decode()
        return {"Authorization": f"Basic {token}"}

    def get(self, endpoint: str, params: dict | None = None) -> Any:
        with httpx.Client(timeout=30) as client:
            resp = client.get(
                f"{self._base_url}/{endpoint}",
                headers=self._auth_headers(),
                params=params,
            )
            resp.raise_for_status()
            return resp.json()

    def post(self, endpoint: str, body: dict) -> Any:
        with httpx.Client(timeout=30) as client:
            resp = client.post(
                f"{self._base_url}/{endpoint}",
                headers={**self._auth_headers(), "Content-Type": "application/json"},
                json=body,
            )
            resp.raise_for_status()
            return resp.json()
