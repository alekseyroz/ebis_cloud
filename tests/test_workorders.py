"""Tests for WorkordersMixin (ebis_cloud/_workorders.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_workorder_lists_uses_get_and_omits_name_when_none(mock_api: MockApi):
    mock_api.set_response({"CityID": [{"ID": 1, "Name": "Denver"}]})

    result = mock_api.client.get_workorder_lists()

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/workorder/lists"
    assert mock_api.captured.params == {}
    assert result == {"CityID": [{"ID": 1, "Name": "Denver"}]}


def test_get_workorder_lists_sends_name_param_when_given(mock_api: MockApi):
    mock_api.set_response({"CityID": [{"ID": 1, "Name": "Denver"}]})

    mock_api.client.get_workorder_lists(list_name="CityID")

    assert mock_api.captured.params == {"name": "CityID"}


def test_export_workorders_uses_post_and_omits_none_optional_filters(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.export_workorders(city_ids=[1013, "Denver"])

    assert mock_api.captured.method == "POST"
    assert mock_api.captured.path == "/api/workorder"
    body = mock_api.captured.json_body
    assert body == {"CityID": [1013, "Denver"]}
    # None/False optional kwargs must not appear as literal values in the body.
    assert "CompletedDate" not in body
    assert "CreatedDate" not in body
    assert "IncludeParts" not in body
    assert "Hierarchy" not in body  # default "flat" is omitted


def test_export_workorders_includes_flags_only_when_true(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.export_workorders(
        include_parts=True,
        include_signoffs=True,
        hierarchy="nested",
        id_accessible=True,
    )

    body = mock_api.captured.json_body
    assert body["IncludeParts"] is True
    assert body["IncludeSignoffs"] is True
    assert body["Hierarchy"] == "nested"
    assert body["IDAccessible"] is True
    assert "IncludeBillingOption" not in body


def test_create_update_workorder_builds_expected_body(mock_api: MockApi):
    mock_api.set_response({"Data": {"MessageID": "OK", "ID": 5}})

    result = mock_api.client.create_update_workorder(
        city_id=10,
        aircraft_id=20,
        items=[{"Discrepancy": "leak"}],
    )

    body = mock_api.captured.json_body
    assert body["CityID"] == 10
    assert body["AircraftID"] == 20
    assert body["Items"] == [{"Discrepancy": "leak"}]
    # Booleans that default False should be excluded entirely.
    assert "CreateCityIfNotExists" not in body
    assert "CreateAircraftIfNotExists" not in body
    assert result == {"Data": {"MessageID": "OK", "ID": 5}}
