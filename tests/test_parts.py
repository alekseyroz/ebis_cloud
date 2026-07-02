"""Tests for PartsMixin (ebis_cloud/_parts.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_masterpart_listing_lists_uses_get(mock_api: MockApi):
    mock_api.set_response({"PartTypeID": []})

    mock_api.client.get_masterpart_listing_lists(list_names=["PartTypeID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/masterpart/listing/lists"
    assert mock_api.captured.params == {"name": "PartTypeID"}


def test_get_masterpart_listing_omits_none_optional_filters(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.get_masterpart_listing(part_number_like="ABC")

    body = mock_api.captured.json_body
    assert body == {"PartNumberLike": "ABC"}
    assert "DescriptionLike" not in body
    assert "SupplierID" not in body
    assert "HasGeneralLocation" not in body
    assert mock_api.captured.path == "/api/masterpart/listing"


def test_get_masterpart_listing_includes_range_filters_and_returns_response(mock_api: MockApi):
    mock_api.set_response({"Data": [{"PartNumber": "ABC-1"}]})

    result = mock_api.client.get_masterpart_listing(
        general_cost_range=[10, 100], has_general_location=True
    )

    body = mock_api.captured.json_body
    assert body["GeneralCostRange"] == [10, 100]
    assert body["HasGeneralLocation"] is True
    assert result == {"Data": [{"PartNumber": "ABC-1"}]}
