"""Shared pytest fixtures for the veryon_wc test suite.

Provides a WcClient wired to an httpx.MockTransport so tests can assert on
outgoing requests (method, URL, params, JSON body, auth headers) without any
real network access, and control the mocked JSON response per test.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

import httpx
import pytest

from veryon_wc import WcClient

BASE_URL = "https://example.veryonwc.test/api"
USERNAME = "test-user"
PASSWORD = "test-pass"


@dataclass
class CapturedRequest:
    """Records the single most recent outgoing request seen by the mock transport."""

    request: httpx.Request | None = None

    @property
    def method(self) -> str:
        assert self.request is not None
        return self.request.method

    @property
    def url(self) -> httpx.URL:
        assert self.request is not None
        return self.request.url

    @property
    def path(self) -> str:
        assert self.request is not None
        return self.request.url.path

    @property
    def params(self) -> dict:
        assert self.request is not None
        return dict(self.request.url.params)

    @property
    def json_body(self) -> dict:
        assert self.request is not None
        if not self.request.content:
            return {}
        return json.loads(self.request.content)

    @property
    def headers(self) -> httpx.Headers:
        assert self.request is not None
        return self.request.headers


@dataclass
class MockApi:
    """Test double bundling the WcClient, the captured request, and a settable response."""

    client: WcClient
    captured: CapturedRequest
    _response_payload: dict = field(default_factory=dict)
    _response_status: int = 200

    def set_response(self, payload: dict, status_code: int = 200) -> None:
        self._response_payload = payload
        self._response_status = status_code


@pytest.fixture
def mock_api() -> MockApi:
    captured = CapturedRequest()
    box = {"payload": {}, "status": 200}

    def handler(request: httpx.Request) -> httpx.Response:
        captured.request = request
        return httpx.Response(box["status"], json=box["payload"])

    transport = httpx.MockTransport(handler)

    client = WcClient(BASE_URL, USERNAME, PASSWORD)

    # Patch get/post on the instance to route through the mock transport while
    # reusing the exact same request-building logic as the real HttpMixin.
    def get(self, endpoint, params=None):
        with httpx.Client(transport=transport, timeout=30) as http_client:
            resp = http_client.get(
                f"{self._base_url}/{endpoint}",
                headers=self._auth_headers(),
                params=params,
            )
            resp.raise_for_status()
            return resp.json()

    def post(self, endpoint, body):
        with httpx.Client(transport=transport, timeout=30) as http_client:
            resp = http_client.post(
                f"{self._base_url}/{endpoint}",
                headers={**self._auth_headers(), "Content-Type": "application/json"},
                json=body,
            )
            resp.raise_for_status()
            return resp.json()

    client.get = get.__get__(client, WcClient)
    client.post = post.__get__(client, WcClient)

    api = MockApi(client=client, captured=captured)

    def set_response(payload: dict, status_code: int = 200) -> None:
        box["payload"] = payload
        box["status"] = status_code

    api.set_response = set_response  # type: ignore[method-assign]

    return api
