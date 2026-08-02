"""Tests for OtcMixin (veryon_wc/_otc.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_otc_listing_lists_uses_get(mock_api: MockApi):
    mock_api.set_response({"StatusID": []})

    mock_api.client.get_otc_listing_lists(list_names=["StatusID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/otc/listing/lists"
    assert mock_api.captured.params == {"name": "StatusID"}


def test_get_otc_listing_omits_none_kwargs_and_defaults_hierarchy_nested(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.get_otc_listing(otc_id=123, include_parts=True)

    body = mock_api.captured.json_body
    assert body == {"OtcID": 123, "IncludeParts": True}
    assert "Hierarchy" not in body  # default "nested" is the omitted default
    assert "BackOrderIs" not in body
    assert "DebugSql" not in body
    assert mock_api.captured.path == "/api/otc/listing"


def test_get_otc_listing_sends_hierarchy_when_non_default_and_returns_response(mock_api: MockApi):
    mock_api.set_response({"Data": [{"OtcID": 1, "EBisMainTypeID": 2}]})

    result = mock_api.client.get_otc_listing(hierarchy="flat")

    body = mock_api.captured.json_body
    assert body == {"Hierarchy": "flat"}
    assert result == {"Data": [{"OtcID": 1, "EBisMainTypeID": 2}]}
