"""Tests for EquipmentMixin (veryon_wc/_equipment.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_equipment_listing_lists_uses_get_and_joins_names(mock_api: MockApi):
    mock_api.set_response({"CityID": []})

    mock_api.client.get_equipment_listing_lists(list_names=["CityID", "VehicleTypeID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/equipment/listing/lists"
    assert mock_api.captured.params == {"name": "CityID,VehicleTypeID"}


def test_get_equipment_listing_lists_omits_name_param_when_none(mock_api: MockApi):
    mock_api.set_response({})

    mock_api.client.get_equipment_listing_lists()

    assert mock_api.captured.params == {}


def test_get_equipment_listing_omits_none_filters_and_false_flags(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.get_equipment_listing(asset_no="A123", vehicle_type_ids=[1, 2])

    body = mock_api.captured.json_body
    assert body == {"AssetNo": "A123", "VehicleTypeID": [1, 2]}
    assert "InactiveInclude" not in body
    assert "OnlyInactive" not in body
    assert "SerialNo" not in body
    assert mock_api.captured.method == "POST"
    assert mock_api.captured.path == "/api/equipment/listing"


def test_add_update_equipment_batch_mode_sends_only_batch_key(mock_api: MockApi):
    mock_api.set_response({"Data": [{"EBisID": 1, "MessageID": "OK"}]})

    batch = [{"Mode": "Insert", "CityNo": "C01"}]
    result = mock_api.client.add_update_equipment(equipment_batch=batch)

    assert mock_api.captured.json_body == {"EquipmentBatch": batch}
    assert result == {"Data": [{"EBisID": 1, "MessageID": "OK"}]}


def test_add_update_equipment_single_record_mode_excludes_unset_fields(mock_api: MockApi):
    mock_api.set_response({"Data": {}})

    mock_api.client.add_update_equipment(mode="Insert", city_id=5, asset_no="A1")

    body = mock_api.captured.json_body
    assert body == {"Mode": "Insert", "CityID": 5, "AssetNo": "A1"}
    assert "EBisID" not in body
    assert "EquipmentBatch" not in body
