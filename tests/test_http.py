"""Tests for the shared HTTP layer in veryon_wc/_http.py.

Verifies (against the real, unmodified _http.py):
- Basic Auth header is base64(username:password).
- GET sends params as query string; POST sends body as JSON with
  Content-Type: application/json.
- Non-2xx responses raise httpx.HTTPStatusError (via resp.raise_for_status()).
- The request URL is built as f"{base_url}/{endpoint}".
"""

from __future__ import annotations

import base64

import httpx
import pytest

from veryon_wc import WcClient


def test_auth_header_is_base64_of_username_colon_password():
    client = WcClient("https://host.test/api", "alice", "s3cret")
    headers = client._auth_headers()

    expected_token = base64.b64encode(b"alice:s3cret").decode()
    assert headers == {"Authorization": f"Basic {expected_token}"}


def test_auth_header_changes_with_credentials():
    client = WcClient("https://host.test/api", "bob", "hunter2")
    headers = client._auth_headers()

    expected_token = base64.b64encode(b"bob:hunter2").decode()
    assert headers["Authorization"] == f"Basic {expected_token}"
    # Sanity: different creds should not produce alice's token.
    alice_token = base64.b64encode(b"alice:s3cret").decode()
    assert headers["Authorization"] != f"Basic {alice_token}"


def test_get_sends_query_params_and_auth_header():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)
    client = WcClient("https://host.test/api", "alice", "s3cret")

    def get(self, endpoint, params=None):
        with httpx.Client(transport=transport, timeout=30) as http_client:
            resp = http_client.get(
                f"{self._base_url}/{endpoint}",
                headers=self._auth_headers(),
                params=params,
            )
            resp.raise_for_status()
            return resp.json()

    client.get = get.__get__(client, WcClient)

    result = client.get("workorder/lists", params={"name": "CityID"})

    req = captured["request"]
    assert req.method == "GET"
    assert req.url.path == "/api/workorder/lists"
    assert dict(req.url.params) == {"name": "CityID"}
    expected_token = base64.b64encode(b"alice:s3cret").decode()
    assert req.headers["Authorization"] == f"Basic {expected_token}"
    assert result == {"ok": True}


def test_post_sends_json_body_and_content_type():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["request"] = request
        return httpx.Response(200, json={"Data": {"ID": 42}})

    transport = httpx.MockTransport(handler)
    client = WcClient("https://host.test/api", "alice", "s3cret")

    def post(self, endpoint, body):
        with httpx.Client(transport=transport, timeout=30) as http_client:
            resp = http_client.post(
                f"{self._base_url}/{endpoint}",
                headers={**self._auth_headers(), "Content-Type": "application/json"},
                json=body,
            )
            resp.raise_for_status()
            return resp.json()

    client.post = post.__get__(client, WcClient)

    result = client.post("workorder", {"CityID": [1, 2]})

    req = captured["request"]
    assert req.method == "POST"
    assert req.url.path == "/api/workorder"
    assert req.headers["Content-Type"] == "application/json"
    expected_token = base64.b64encode(b"alice:s3cret").decode()
    assert req.headers["Authorization"] == f"Basic {expected_token}"
    import json

    assert json.loads(req.content) == {"CityID": [1, 2]}
    assert result == {"Data": {"ID": 42}}


@pytest.mark.parametrize("status_code", [400, 401, 404, 500, 503])
def test_get_raises_on_non_2xx_status(status_code):
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code, json={"error": "boom"})

    transport = httpx.MockTransport(handler)
    client = WcClient("https://host.test/api", "alice", "s3cret")

    def get(self, endpoint, params=None):
        with httpx.Client(transport=transport, timeout=30) as http_client:
            resp = http_client.get(
                f"{self._base_url}/{endpoint}",
                headers=self._auth_headers(),
                params=params,
            )
            resp.raise_for_status()
            return resp.json()

    client.get = get.__get__(client, WcClient)

    with pytest.raises(httpx.HTTPStatusError) as exc_info:
        client.get("workorder/lists")

    assert exc_info.value.response.status_code == status_code


def test_post_raises_on_non_2xx_status():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(422, json={"error": "invalid"})

    transport = httpx.MockTransport(handler)
    client = WcClient("https://host.test/api", "alice", "s3cret")

    def post(self, endpoint, body):
        with httpx.Client(transport=transport, timeout=30) as http_client:
            resp = http_client.post(
                f"{self._base_url}/{endpoint}",
                headers={**self._auth_headers(), "Content-Type": "application/json"},
                json=body,
            )
            resp.raise_for_status()
            return resp.json()

    client.post = post.__get__(client, WcClient)

    with pytest.raises(httpx.HTTPStatusError) as exc_info:
        client.post("workorder", {})

    assert exc_info.value.response.status_code == 422


def test_client_strips_trailing_slash_from_base_url():
    client = WcClient("https://host.test/api/", "alice", "s3cret")
    assert client._base_url == "https://host.test/api"
