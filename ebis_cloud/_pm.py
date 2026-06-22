"""Preventive maintenance API methods."""

from typing import Any


class PmMixin:
    def get_upcoming_pm_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying upcoming PMs.

        Available list names: CityID, RegionID, SummarizeBy, SummarizeByDateGroup,
        VehicleTypeID, ZoneID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("equipment/pmupcoming/lists", params=params)

    def get_upcoming_pm(
        self,
        city_ids: list[int | str] | None = None,
        is_powered: str | None = None,
        region_ids: list[int | str] | None = None,
        show_all_upcoming_wo: bool = False,
        summarize_by: int | str | None = None,
        summarize_by_date_group: int | str | None = None,
        vehicle_type_ids: list[int | str] | None = None,
        zone_ids: list[int | str] | None = None,
        id_accessible: bool = False,
        language: str | None = None,
    ) -> dict:
        """
        Retrieve upcoming preventive maintenance (PM) information for equipment.

        Use get_upcoming_pm_lists() to discover valid ID/name values.

        Args:
            city_ids: Filter by city IDs or names.
            is_powered: Filter by powered status — "yes", "no", or "all".
            region_ids: Filter by region IDs or names.
            show_all_upcoming_wo: If True, include all upcoming work orders, not just the next due.
            summarize_by: Group/summarize results by this field ID or name.
            summarize_by_date_group: Secondary date grouping for the summary.
            vehicle_type_ids: Filter by vehicle type IDs or names.
            zone_ids: Filter by zone IDs or names.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            language: Language for generic list parameter lookups (default: "English").

        Returns:
            Upcoming PM records for matching equipment.
        """
        body: dict[str, Any] = {}

        if city_ids is not None:
            body["CityID"] = city_ids
        if is_powered is not None:
            body["IsPowered"] = is_powered
        if region_ids is not None:
            body["RegionID"] = region_ids
        if show_all_upcoming_wo:
            body["ShowAllUpcomingWo"] = True
        if summarize_by is not None:
            body["SummarizeBy"] = summarize_by
        if summarize_by_date_group is not None:
            body["SummarizeByDateGroup"] = summarize_by_date_group
        if vehicle_type_ids is not None:
            body["VehicleTypeID"] = vehicle_type_ids
        if zone_ids is not None:
            body["ZoneID"] = zone_ids
        if id_accessible:
            body["IDAccessible"] = True
        if language is not None:
            body["Language"] = language

        return self.post("equipment/pmupcoming", body)
