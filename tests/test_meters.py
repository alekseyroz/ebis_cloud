"""Tests for MetersMixin (ebis_cloud/_meters.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_meter_reading_lists_uses_get(mock_api: MockApi):
    mock_api.set_response({"CityID": []})

    mock_api.client.get_meter_reading_lists(list_names=["CityID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/equipment/meter/lists"
    assert mock_api.captured.params == {"name": "CityID"}


def test_get_meter_readings_requires_reading_dates_and_defaults_hierarchy_nested(
    mock_api: MockApi,
):
    mock_api.set_response({"Data": []})

    mock_api.client.get_meter_readings(reading_dates=["2024-01-01", "2024-01-31"])

    body = mock_api.captured.json_body
    assert body == {"ReadingDates": ["2024-01-01", "2024-01-31"]}
    # hierarchy default "nested" should be omitted since it matches the default
    assert "Hierarchy" not in body
    assert mock_api.captured.path == "/api/equipment/meter"


def test_get_meter_readings_sends_hierarchy_when_non_default(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.get_meter_readings(reading_dates=["2024-01-01"], hierarchy="flat")

    body = mock_api.captured.json_body
    assert body["Hierarchy"] == "flat"


def test_add_update_meter_readings_builds_body_with_assets_and_flags(mock_api: MockApi):
    mock_api.set_response({"Data": [{"EBisID": 1, "MessageID": "OK"}]})

    assets = [{"EBisID": 1, "Reading": 1234}]
    result = mock_api.client.add_update_meter_readings(
        assets=assets, apply_timezone_conversion=True
    )

    body = mock_api.captured.json_body
    assert body["Assets"] == assets
    assert body["ApplyTimezoneConversion"] is True
    assert "UseReadingDate" not in body
    assert mock_api.captured.path == "/api/equipment/meter/addupdate"
    assert result == {"Data": [{"EBisID": 1, "MessageID": "OK"}]}
