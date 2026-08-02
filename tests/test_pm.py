"""Tests for PmMixin (veryon_wc/_pm.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_upcoming_pm_lists_uses_get(mock_api: MockApi):
    mock_api.set_response({"ZoneID": []})

    mock_api.client.get_upcoming_pm_lists(list_names=["ZoneID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/equipment/pmupcoming/lists"
    assert mock_api.captured.params == {"name": "ZoneID"}


def test_get_upcoming_pm_omits_none_kwargs_and_false_flags(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.get_upcoming_pm(city_ids=[1, 2], is_powered=None)

    body = mock_api.captured.json_body
    assert body == {"CityID": [1, 2]}
    assert "IsPowered" not in body
    assert "ShowAllUpcomingWo" not in body
    assert mock_api.captured.path == "/api/equipment/pmupcoming"


def test_get_upcoming_pm_returns_parsed_json(mock_api: MockApi):
    mock_api.set_response({"Data": [{"EBisID": 7, "DueDate": "2024-02-01"}]})

    result = mock_api.client.get_upcoming_pm(show_all_upcoming_wo=True)

    assert mock_api.captured.json_body == {"ShowAllUpcomingWo": True}
    assert result == {"Data": [{"EBisID": 7, "DueDate": "2024-02-01"}]}
