"""Tests for ServiceRequestsMixin (ebis_cloud/_service_requests.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_service_request_addupdate_lists_uses_get(mock_api: MockApi):
    mock_api.set_response({"StatusID": []})

    mock_api.client.get_service_request_addupdate_lists(list_names=["StatusID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/servicerequest/addupdate/lists"
    assert mock_api.captured.params == {"name": "StatusID"}


def test_add_update_service_request_insert_mode_omits_none_optional_fields(mock_api: MockApi):
    mock_api.set_response({"Data": {"MessageID": "OK", "ID": 99, "Mode": "Insert"}})

    result = mock_api.client.add_update_service_request(
        mode="Insert",
        asset_related_id=10,
        category_id=1,
        priority_id=2,
        description="Broken light",
        location="Bay 3",
        request_by_name="Jane",
        request_by_location="Bay 3",
    )

    body = mock_api.captured.json_body
    assert body["Mode"] == "Insert"
    assert body["AssetRelatedID"] == 10
    assert body["Description"] == "Broken light"
    # optional fields not provided must be entirely absent, not "None"
    assert "SrNumber" not in body
    assert "DidTagEquipment" not in body
    assert "Latitude" not in body
    assert mock_api.captured.path == "/api/servicerequest/addupdate"
    assert result == {"Data": {"MessageID": "OK", "ID": 99, "Mode": "Insert"}}


def test_add_update_service_request_update_mode_uses_id(mock_api: MockApi):
    mock_api.set_response({"Data": {"MessageID": "OK"}})

    mock_api.client.add_update_service_request(mode="Update", id=5, status_id=3)

    body = mock_api.captured.json_body
    assert body == {"Mode": "Update", "ID": 5, "StatusID": 3}
