"""Service request API methods."""

from typing import Any


class ServiceRequestsMixin:
    def get_service_request_addupdate_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when adding or updating service requests.

        Available list names: StatusID, CategoryID, PriorityID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("servicerequest/addupdate/lists", params=params)

    def add_update_service_request(
        self,
        mode: str,
        asset_related_id: int | None = None,
        id: int | None = None,
        sr_number: str | None = None,
        status_id: int | None = None,
        category_id: int | None = None,
        priority_id: int | None = None,
        description: str | None = None,
        location: str | None = None,
        request_by_name: str | None = None,
        request_by_phone: str | None = None,
        request_by_email: str | None = None,
        request_by_location: str | None = None,
        did_tag_equipment: bool | None = None,
        defer_reject_notes: str | None = None,
        latitude: float | None = None,
        longitude: float | None = None,
        is_system_created: bool | None = None,
        is_invalid_telemetry_reason: str | None = None,
        extra_log_info: str | None = None,
        debug_notifications: bool = False,
    ) -> dict:
        """
        Add or update a service request in eBis Cloud.

        Use get_service_request_addupdate_lists() to find valid IDs for
        StatusID, CategoryID, and PriorityID.

        Mode values:
        - "Insert": Create a new service request.
        - "Update": Update an existing service request.

        Args:
            mode: (Required) "Insert" to create, "Update" to modify an existing record.
            asset_related_id: Equipment ID to associate with the service request. Required for Insert.
            id: eBis service request ID — used to identify the record for Update.
            sr_number: Service request number — alternative identifier for Update.
            status_id: Status ID for the service request.
            category_id: Category ID or name. Required for Insert.
            priority_id: Priority ID or name. Required for Insert.
            description: Description of the service request. Required for Insert.
            location: Physical location of the equipment. Required for Insert.
            request_by_name: Name of the person making the request. Required for Insert.
            request_by_phone: Phone number of the requestor.
            request_by_email: Email address of the requestor.
            request_by_location: Location of the requestor. Required for Insert.
            did_tag_equipment: Whether the equipment was physically tagged.
            defer_reject_notes: Notes for a deferred or rejected service request.
            latitude: GPS latitude of the equipment location.
            longitude: GPS longitude of the equipment location.
            is_system_created: If True, mark the record as system-created.
            is_invalid_telemetry_reason: Reason string if the telemetry data is invalid.
            extra_log_info: Additional information to include in the log.
            debug_notifications: If True, enable debug output for notifications.

        Returns:
            Dict with Data containing MessageID, MessageText, ID, and Mode.
        """
        body: dict[str, Any] = {
            "Mode": mode,
        }

        if asset_related_id is not None:
            body["AssetRelatedID"] = asset_related_id
        if id is not None:
            body["ID"] = id
        if sr_number is not None:
            body["SrNumber"] = sr_number
        if status_id is not None:
            body["StatusID"] = status_id
        if category_id is not None:
            body["CategoryID"] = category_id
        if priority_id is not None:
            body["PriorityID"] = priority_id
        if description is not None:
            body["Description"] = description
        if location is not None:
            body["Location"] = location
        if request_by_name is not None:
            body["RequestByName"] = request_by_name
        if request_by_phone is not None:
            body["RequestByPhone"] = request_by_phone
        if request_by_email is not None:
            body["RequestByEmail"] = request_by_email
        if request_by_location is not None:
            body["RequestByLocation"] = request_by_location
        if did_tag_equipment is not None:
            body["DidTagEquipment"] = did_tag_equipment
        if defer_reject_notes is not None:
            body["DeferRejectNotes"] = defer_reject_notes
        if latitude is not None:
            body["Latitude"] = latitude
        if longitude is not None:
            body["Longitude"] = longitude
        if is_system_created is not None:
            body["IsSystemCreated"] = is_system_created
        if is_invalid_telemetry_reason is not None:
            body["IsInvalidTelemetryReason"] = is_invalid_telemetry_reason
        if extra_log_info is not None:
            body["ExtraLogInfo"] = extra_log_info
        if debug_notifications:
            body["DebugNotifications"] = True

        return self.post("servicerequest/addupdate", body)
