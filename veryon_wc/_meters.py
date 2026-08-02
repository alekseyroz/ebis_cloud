"""Meter readings API methods."""

from typing import Any


class MetersMixin:
    def get_meter_reading_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying meter readings.

        Available list names: CityID, ControllerID, CostCenterID, CustomerID, DepartmentID,
        Engine1ID, FleetConfigID, Make1ID, MeterProfileID, Model1ID, MotorID, PartsCatalogID,
        PmDocID, Power1ID, RegionID, TelemetryIntegID, UserStatusID, VehicleTypeID,
        WorkCenterID, ZoneID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("equipment/meter/lists", params=params)

    def get_meter_readings(
        self,
        reading_dates: list[str],
        after_paint_date: list[str] | None = None,
        any_license_due_next_days: int | None = None,
        asset_no: str | None = None,
        asset_no_multiple: list[str] | None = None,
        banner_status: str | None = None,
        battery_mgmt_id: str | None = None,
        city_ids: list[int | str] | None = None,
        city_no_like: str | None = None,
        city_no_multiple: list[str] | None = None,
        contractor: str | None = None,
        controller_ids: list[int | str] | None = None,
        cost_center_ids: list[int | str] | None = None,
        customer_ids: list[int | str] | None = None,
        department_ids: list[int | str] | None = None,
        ebis_ids: list[int] | None = None,
        engine1_ids: list[int | str] | None = None,
        engine1_serial: str | None = None,
        engine1_spec_no: str | None = None,
        fleet_config_ids: list[int | str] | None = None,
        front_axel_serial: str | None = None,
        has_date_based_schedule: bool = False,
        has_license_no: str | None = None,
        has_linked_parts_list_override: str | None = None,
        has_meter_based_schedule: bool = False,
        has_pm_part_kit: str | None = None,
        has_pm_part_kit_override: str | None = None,
        has_pm_schedules: str | None = None,
        has_seatbelt: str | None = None,
        inactive_include: bool = False,
        last_pm_over_days_ago: int | None = None,
        lease_expires_next_days: int | None = None,
        license_no: str | None = None,
        make1_ids: list[int | str] | None = None,
        meter_profile_ids: list[int | str] | None = None,
        model1_ids: list[int | str] | None = None,
        motor_ids: list[int | str] | None = None,
        only_inactive: bool = False,
        only_with_telemetry: bool = False,
        only_with_valid_warranty: bool = False,
        parts_catalog_ids: list[int | str] | None = None,
        pm_doc_ids: list[int | str] | None = None,
        power1_ids: list[int | str] | None = None,
        rear_axel_serial: str | None = None,
        reflectivity: str | None = None,
        region_ids: list[int | str] | None = None,
        rental_expires_next_days: int | None = None,
        serial_no: str | None = None,
        show_license_no: bool = False,
        stationary_loc_multiple: list[str] | None = None,
        surplus: str | None = None,
        telemetry_integ_ids: list[int | str] | None = None,
        telemetry_key: str | None = None,
        transmission_serial: str | None = None,
        user_status_ids: list[int | str] | None = None,
        vehicle_type_ids: list[int | str] | None = None,
        vin: str | None = None,
        warranty_expires_in_days: int | None = None,
        work_center_ids: list[int | str] | None = None,
        year_built: list[int] | None = None,
        zone_ids: list[int | str] | None = None,
        hierarchy: str = "nested",
        id_accessible: bool = False,
        language: str | None = None,
    ) -> dict:
        """
        Retrieve meter reading history for selected equipment.

        Use get_meter_reading_lists() to discover valid ID/name values.

        Args:
            reading_dates: (Required) Date range to retrieve readings within,
                           e.g. ["2024-01-01", "2024-01-31"].
            after_paint_date: Filter equipment painted after these dates.
            any_license_due_next_days: Return equipment with any license due within N days.
            asset_no: Fragment search on asset number.
            asset_no_multiple: Filter by multiple exact asset numbers.
            banner_status: Fragment search on banner status.
            battery_mgmt_id: Fragment search on battery management ID.
            city_ids: Filter by city IDs or names.
            city_no_like: Fragment search on city number.
            city_no_multiple: Filter by multiple exact city numbers.
            contractor: Filter by contractor status — "yes", "no", or "all".
            controller_ids: Filter by controller IDs or names.
            cost_center_ids: Filter by cost center IDs or names.
            customer_ids: Filter by customer IDs or names.
            department_ids: Filter by department IDs or names.
            ebis_ids: Filter by specific eBis equipment IDs.
            engine1_ids: Filter by primary engine IDs or names.
            engine1_serial: Fragment search on primary engine serial number.
            engine1_spec_no: Fragment search on primary engine spec number.
            fleet_config_ids: Filter by fleet configuration IDs or names.
            front_axel_serial: Fragment search on front axle serial number.
            has_date_based_schedule: If True, return only equipment with a date-based PM schedule.
            has_license_no: Filter by license number presence — "yes", "no", or "all".
            has_linked_parts_list_override: Filter by linked parts list override — "yes", "no", or "all".
            has_meter_based_schedule: If True, return only equipment with a meter-based PM schedule.
            has_pm_part_kit: Filter by PM part kit presence — "yes", "no", or "all".
            has_pm_part_kit_override: Filter by PM part kit override — "yes", "no", or "all".
            has_pm_schedules: Filter by PM schedule presence — "yes", "no", or "all".
            has_seatbelt: Filter by seatbelt presence — "yes", "no", or "all".
            inactive_include: If True, include inactive equipment.
            last_pm_over_days_ago: Return equipment whose last PM was more than N days ago.
            lease_expires_next_days: Return equipment whose lease expires within N days.
            license_no: Fragment search on license number.
            make1_ids: Filter by primary make IDs or names.
            meter_profile_ids: Filter by meter profile IDs or names.
            model1_ids: Filter by primary model IDs or names.
            motor_ids: Filter by motor IDs or names.
            only_inactive: If True, return only inactive equipment.
            only_with_telemetry: If True, return only equipment with telemetry.
            only_with_valid_warranty: If True, return only equipment with a valid warranty.
            parts_catalog_ids: Filter by parts catalog IDs or names.
            pm_doc_ids: Filter by PM document IDs or names.
            power1_ids: Filter by primary power source IDs or names.
            rear_axel_serial: Fragment search on rear axle serial number.
            reflectivity: Filter by reflectivity status — "yes", "no", or "all".
            region_ids: Filter by region IDs or names.
            rental_expires_next_days: Return equipment whose rental expires within N days.
            serial_no: Fragment search on equipment serial number.
            show_license_no: If True, include license number fields in the response.
            stationary_loc_multiple: Filter by multiple stationary location values.
            surplus: Filter by surplus status — "yes", "no", or "all".
            telemetry_integ_ids: Filter by telemetry integration IDs or names.
            telemetry_key: Fragment search on telemetry key.
            transmission_serial: Fragment search on transmission serial number.
            user_status_ids: Filter by user status IDs or names.
            vehicle_type_ids: Filter by vehicle type IDs or names.
            vin: Fragment search on VIN.
            warranty_expires_in_days: Return equipment whose warranty expires within N days.
            work_center_ids: Filter by work center IDs or names.
            year_built: Filter by year(s) built.
            zone_ids: Filter by zone IDs or names.
            hierarchy: Response structure — "nested" (default) or "flat".
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            language: Language for generic list parameter lookups (default: "English").

        Returns:
            Meter reading history records for the matching equipment within the date range.
        """
        body: dict[str, Any] = {
            "ReadingDates": reading_dates,
        }

        if after_paint_date is not None:
            body["AfterPaintDate"] = after_paint_date
        if any_license_due_next_days is not None:
            body["AnyLicenseDueNextDays"] = any_license_due_next_days
        if asset_no is not None:
            body["AssetNo"] = asset_no
        if asset_no_multiple is not None:
            body["AssetNoMultiple"] = asset_no_multiple
        if banner_status is not None:
            body["BannerStatus"] = banner_status
        if battery_mgmt_id is not None:
            body["BatteryMgmtID"] = battery_mgmt_id
        if city_ids is not None:
            body["CityID"] = city_ids
        if city_no_like is not None:
            body["CityNoLike"] = city_no_like
        if city_no_multiple is not None:
            body["CityNoMultiple"] = city_no_multiple
        if contractor is not None:
            body["Contractor"] = contractor
        if controller_ids is not None:
            body["ControllerID"] = controller_ids
        if cost_center_ids is not None:
            body["CostCenterID"] = cost_center_ids
        if customer_ids is not None:
            body["CustomerID"] = customer_ids
        if department_ids is not None:
            body["DepartmentID"] = department_ids
        if ebis_ids is not None:
            body["EBisID"] = ebis_ids
        if engine1_ids is not None:
            body["Engine1ID"] = engine1_ids
        if engine1_serial is not None:
            body["Engine1Serial"] = engine1_serial
        if engine1_spec_no is not None:
            body["Engine1SpecNo"] = engine1_spec_no
        if fleet_config_ids is not None:
            body["FleetConfigID"] = fleet_config_ids
        if front_axel_serial is not None:
            body["FrontAxelSerial"] = front_axel_serial
        if has_date_based_schedule:
            body["HasDateBasedSchedule"] = True
        if has_license_no is not None:
            body["HasLicenseNo"] = has_license_no
        if has_linked_parts_list_override is not None:
            body["HasLinkedPartsListOverride"] = has_linked_parts_list_override
        if has_meter_based_schedule:
            body["HasMeterBasedSchedule"] = True
        if has_pm_part_kit is not None:
            body["HasPmPartKit"] = has_pm_part_kit
        if has_pm_part_kit_override is not None:
            body["HasPmPartKitOverride"] = has_pm_part_kit_override
        if has_pm_schedules is not None:
            body["HasPmSchedules"] = has_pm_schedules
        if has_seatbelt is not None:
            body["HasSeatbelt"] = has_seatbelt
        if inactive_include:
            body["InactiveInclude"] = True
        if last_pm_over_days_ago is not None:
            body["LastPmOverDaysAgo"] = last_pm_over_days_ago
        if lease_expires_next_days is not None:
            body["LeaseExpiresNextDays"] = lease_expires_next_days
        if license_no is not None:
            body["LicenseNo"] = license_no
        if make1_ids is not None:
            body["Make1ID"] = make1_ids
        if meter_profile_ids is not None:
            body["MeterProfileID"] = meter_profile_ids
        if model1_ids is not None:
            body["Model1ID"] = model1_ids
        if motor_ids is not None:
            body["MotorID"] = motor_ids
        if only_inactive:
            body["OnlyInactive"] = True
        if only_with_telemetry:
            body["OnlyWithTelemetry"] = True
        if only_with_valid_warranty:
            body["OnlyWithValidWarranty"] = True
        if parts_catalog_ids is not None:
            body["PartsCatalogID"] = parts_catalog_ids
        if pm_doc_ids is not None:
            body["PmDocID"] = pm_doc_ids
        if power1_ids is not None:
            body["Power1ID"] = power1_ids
        if rear_axel_serial is not None:
            body["RearAxelSerial"] = rear_axel_serial
        if reflectivity is not None:
            body["Reflectivity"] = reflectivity
        if region_ids is not None:
            body["RegionID"] = region_ids
        if rental_expires_next_days is not None:
            body["RentalExpiresNextDays"] = rental_expires_next_days
        if serial_no is not None:
            body["SerialNo"] = serial_no
        if show_license_no:
            body["ShowLicenseNo"] = True
        if stationary_loc_multiple is not None:
            body["StationaryLocMultiple"] = stationary_loc_multiple
        if surplus is not None:
            body["Surplus"] = surplus
        if telemetry_integ_ids is not None:
            body["TelemetryIntegID"] = telemetry_integ_ids
        if telemetry_key is not None:
            body["TelemetryKey"] = telemetry_key
        if transmission_serial is not None:
            body["TransmissionSerial"] = transmission_serial
        if user_status_ids is not None:
            body["UserStatusID"] = user_status_ids
        if vehicle_type_ids is not None:
            body["VehicleTypeID"] = vehicle_type_ids
        if vin is not None:
            body["Vin"] = vin
        if warranty_expires_in_days is not None:
            body["WarrantyExpiresInDays"] = warranty_expires_in_days
        if work_center_ids is not None:
            body["WorkCenterID"] = work_center_ids
        if year_built is not None:
            body["YearBuilt"] = year_built
        if zone_ids is not None:
            body["ZoneID"] = zone_ids
        if hierarchy != "nested":
            body["Hierarchy"] = hierarchy
        if id_accessible:
            body["IDAccessible"] = True
        if language is not None:
            body["Language"] = language

        return self.post("equipment/meter", body)

    def add_update_meter_readings(
        self,
        assets: list[dict],
        apply_timezone_conversion: bool = False,
        use_reading_date: bool = False,
    ) -> dict:
        """
        Add or update meter readings for a batch of equipment.

        Each asset in the `assets` list must include one of: EBisID, RegNum, or
        TelemetryVendorAssetNo to identify the equipment, plus a Reading value.

        Args:
            assets: (Required) List of asset reading dicts.
            apply_timezone_conversion: If True, apply timezone conversion to reading timestamps.
            use_reading_date: If True, use the reading date rather than the submission date.

        Returns:
            Per-asset results with EBisID, LineNumber, ProfileName, MessageID, MessageText,
            and a Readings list. MessageID is "OK" if all readings succeeded.
        """
        body: dict[str, Any] = {
            "Assets": assets,
        }

        if apply_timezone_conversion:
            body["ApplyTimezoneConversion"] = True
        if use_reading_date:
            body["UseReadingDate"] = True

        return self.post("equipment/meter/addupdate", body)
