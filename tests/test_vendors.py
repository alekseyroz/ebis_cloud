"""Tests for VendorsMixin (ebis_cloud/_vendors.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_vendor_listing_lists_uses_get(mock_api: MockApi):
    mock_api.set_response({"TermsID": []})

    mock_api.client.get_vendor_listing_lists(list_names=["TermsID", "ShipMethodID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/vendor/listing/lists"
    assert mock_api.captured.params == {"name": "TermsID,ShipMethodID"}


def test_get_vendor_listing_omits_none_kwargs_and_false_defaults(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.get_vendor_listing(vendor_name="Acme", cities=["Dallas"])

    body = mock_api.captured.json_body
    assert body == {"VendorName": "Acme", "Cities": ["Dallas"]}
    assert "IncludeInactive" not in body
    assert "HasMedia" not in body
    assert "IDAccessible" not in body
    assert mock_api.captured.path == "/api/vendor/listing"


def test_add_update_vendors_batch_mode_sends_only_vendor_batch(mock_api: MockApi):
    mock_api.set_response({"Data": [{"ID": 1, "MessageID": "OK"}]})

    batch = [{"Mode": "Insert", "VendorName": "Acme"}]
    result = mock_api.client.add_update_vendors(vendor_batch=batch)

    assert mock_api.captured.json_body == {"VendorBatch": batch}
    assert result == {"Data": [{"ID": 1, "MessageID": "OK"}]}


def test_add_update_vendors_single_record_mode_excludes_unset_fields(mock_api: MockApi):
    mock_api.set_response({"Data": {}})

    mock_api.client.add_update_vendors(mode="Insert", vendor_name="Acme", email="a@acme.test")

    body = mock_api.captured.json_body
    assert body == {"Mode": "Insert", "VendorName": "Acme", "Email": "a@acme.test"}
    assert "ChangeToName" not in body
    assert "VendorBatch" not in body
    assert mock_api.captured.path == "/api/vendor/addupdate"
