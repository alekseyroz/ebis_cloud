"""Tests for InventoryMixin (veryon_wc/_inventory.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_stock_quantity_detail_lists_uses_get(mock_api: MockApi):
    mock_api.set_response({"StockRoomID": []})

    mock_api.client.get_stock_quantity_detail_lists(list_names=["StockRoomID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/masterpart/quantity/detail/lists"
    assert mock_api.captured.params == {"name": "StockRoomID"}


def test_get_stock_quantity_detail_omits_none_kwargs(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.get_stock_quantity_detail(stock_room_ids=[1, 2], stock_qty=5)

    body = mock_api.captured.json_body
    assert body == {"StockRoomID": [1, 2], "StockQty": 5}
    assert "DescriptionLike" not in body
    assert "IDAccessible" not in body
    assert mock_api.captured.path == "/api/masterpart/quantity/detail"


def test_get_stock_quantity_log_requires_dates_and_omits_optional_none(mock_api: MockApi):
    mock_api.set_response({"Data": [{"PartNumber": "X1", "QtyChange": -1}]})

    result = mock_api.client.get_stock_quantity_log(dates=["2024-01-01", "2024-01-31"])

    body = mock_api.captured.json_body
    assert body == {"Date": ["2024-01-01", "2024-01-31"]}
    assert "User" not in body
    assert "DebugSql" not in body
    assert mock_api.captured.path == "/api/masterpart/quantity/log"
    assert result == {"Data": [{"PartNumber": "X1", "QtyChange": -1}]}
