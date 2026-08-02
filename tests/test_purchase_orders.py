"""Tests for PurchaseOrdersMixin (veryon_wc/_purchase_orders.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_purchase_order_lists_uses_get(mock_api: MockApi):
    mock_api.set_response({"VendorID": []})

    mock_api.client.get_purchase_order_lists(list_names=["VendorID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/purchaseorder/lists"
    assert mock_api.captured.params == {"name": "VendorID"}


def test_export_purchase_orders_omits_none_filters_and_false_flags(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.export_purchase_orders(vendor_ids=[1, 2], part_number="ABC")

    body = mock_api.captured.json_body
    assert body == {"VendorID": [1, 2], "PartNumber": "ABC"}
    assert "IncludeItemDetail" not in body
    assert "Hierarchy" not in body
    assert mock_api.captured.method == "POST"
    assert mock_api.captured.path == "/api/purchaseorder"


def test_export_purchase_orders_includes_true_flags_and_returns_response(mock_api: MockApi):
    mock_api.set_response({"Data": [{"PoNumber": "PO-1"}]})

    result = mock_api.client.export_purchase_orders(
        include_item_detail=True, include_receiving_info=True, hierarchy="nested"
    )

    body = mock_api.captured.json_body
    assert body["IncludeItemDetail"] is True
    assert body["IncludeReceivingInfo"] is True
    assert body["Hierarchy"] == "nested"
    assert result == {"Data": [{"PoNumber": "PO-1"}]}
