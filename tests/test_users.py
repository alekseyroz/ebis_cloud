"""Tests for UsersMixin (veryon_wc/_users.py)."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from conftest import MockApi


def test_get_user_lists_uses_get(mock_api: MockApi):
    mock_api.set_response({"TechGroupID": []})

    mock_api.client.get_user_lists(list_names=["TechGroupID"])

    assert mock_api.captured.method == "GET"
    assert mock_api.captured.path == "/api/user/lists"
    assert mock_api.captured.params == {"name": "TechGroupID"}


def test_get_users_omits_none_and_false_defaults(mock_api: MockApi):
    mock_api.set_response({"Data": []})

    mock_api.client.get_users(profile_name="Tech", city_ids=[1, 2])

    body = mock_api.captured.json_body
    assert body == {"ProfileName": "Tech", "CityID": [1, 2]}
    assert "ShowInactive" not in body
    assert "ValidEmails" not in body
    assert "HasMedia" not in body
    assert mock_api.captured.path == "/api/user"


def test_logout_users_batch_mode_sends_only_user_batch(mock_api: MockApi):
    mock_api.set_response({"Data": [{"MessageID": "OK"}]})

    batch = [{"LogoutUserID": 1}]
    result = mock_api.client.logout_users(user_batch=batch)

    assert mock_api.captured.json_body == {"UserBatch": batch}
    assert mock_api.captured.path == "/api/user/logout"
    assert result == {"Data": [{"MessageID": "OK"}]}


def test_logout_users_single_mode_omits_unset_fields(mock_api: MockApi):
    mock_api.set_response({"Data": {"MessageID": "OK"}})

    mock_api.client.logout_users(logout_user_id=7, stop_active_timers=True)

    body = mock_api.captured.json_body
    assert body == {"StopActiveTimers": True, "LogoutUserID": 7}
    assert "SessionLogout" not in body
    assert "SsoID" not in body
