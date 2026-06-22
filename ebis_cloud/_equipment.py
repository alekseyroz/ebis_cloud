"""Equipment API methods."""

from typing import Any


class EquipmentMixin:
    def get_equipment_listing_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying equipment listings.

        Available list names: CityID, ControllerID, CostCenterID, CustomerID, DepartmentID,
        Engine1ID, FleetConfigID, Make1ID, MeterProfileID, Model1ID, MotorID, PartsCatalogID,
        PmDocID, Power1ID, RegionID, TelemetryIntegID, UserStatusID, VehicleTypeID,
        WorkCenterID, ZoneID.

        Args:
            list_names: Optional list of specific list names to return,
                        e.g. ["CityID", "VehicleTypeID"]. If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("equipment/listing/lists", params=params)

    def get_equipment_listing(
        self,
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
        id_accessible: bool = False,
        language: str | None = None,
    ) -> dict:
        """
        Retrieve a general equipment listing based on custom criteria.

        Use get_equipment_listing_lists() to discover valid ID/name values for
        any of the ID filter parameters.

        Args:
            after_paint_date: Filter equipment painted after these dates, e.g. ["2024-01-25"].
            any_license_due_next_days: Return equipment with any license due within N days.
            asset_no: Fragment search on asset number.
            asset_no_multiple: Filter by multiple exact asset numbers, e.g. ["A001", "A002"].
            banner_status: Fragment search on banner status.
            battery_mgmt_id: Fragment search on battery management ID.
            city_ids: Filter by city IDs or names.
            city_no_like: Fragment search on city number.
            city_no_multiple: Filter by multiple exact city numbers, e.g. ["C01", "C02"].
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
            inactive_include: If True, include inactive equipment in the results.
            last_pm_over_days_ago: Return equipment whose last PM was more than N days ago.
            lease_expires_next_days: Return equipment whose lease expires within N days.
            license_no: Fragment search on license number.
            make1_ids: Filter by primary make IDs or names.
            meter_profile_ids: Filter by meter profile IDs or names.
            model1_ids: Filter by primary model IDs or names.
            motor_ids: Filter by motor IDs or names.
            only_inactive: If True, return only inactive equipment.
            only_with_telemetry: If True, return only equipment that has telemetry.
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
            year_built: Filter by year(s) built, e.g. [2001, 2002].
            zone_ids: Filter by zone IDs or names.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            language: Language for generic list parameter lookups (default: "English").

        Returns:
            Equipment listing records matching the requested filters.
        """
        body: dict[str, Any] = {}

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
        if id_accessible:
            body["IDAccessible"] = True
        if language is not None:
            body["Language"] = language

        return self.post("equipment/listing", body)

    def get_out_of_service_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying out-of-service detail.

        Available list names: CityID, CustomerID, DepartmentGroupID, DepartmentID,
        MaintainedByID, MakeID, ModelID, PowerID, RegionID, VehicleTypeID, WorkCenterID.

        Args:
            list_names: Optional list of specific list names to return,
                        e.g. ["CityID", "VehicleTypeID"]. If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("equipment/outofservice/detail/lists", params=params)

    def get_out_of_service_detail(
        self,
        city_ids: list[int | str] | None = None,
        customer_ids: list[int | str] | None = None,
        department_group_ids: list[int | str] | None = None,
        department_ids: list[int | str] | None = None,
        maintained_by_ids: list[int | str] | None = None,
        make_ids: list[int | str] | None = None,
        model_ids: list[int | str] | None = None,
        power_ids: list[int | str] | None = None,
        region_ids: list[int | str] | None = None,
        show_detail: bool = False,
        vehicle_type_ids: list[int | str] | None = None,
        work_center_ids: list[int | str] | None = None,
        id_accessible: bool = False,
    ) -> dict:
        """
        Retrieve a detailed list of equipment currently out of service.

        Use get_out_of_service_lists() to discover valid ID/name values for
        any of the ID filter parameters.

        Args:
            city_ids: Filter by city IDs or names.
            customer_ids: Filter by customer IDs or names.
            department_group_ids: Filter by department group IDs or names.
            department_ids: Filter by department IDs or names.
            maintained_by_ids: Filter by maintained-by organisation IDs or names.
            make_ids: Filter by equipment make IDs or names.
            model_ids: Filter by equipment model IDs or names.
            power_ids: Filter by power source IDs or names.
            region_ids: Filter by region IDs or names.
            show_detail: If True, include additional detail fields in the response.
            vehicle_type_ids: Filter by vehicle type IDs or names.
            work_center_ids: Filter by work center IDs or names.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.

        Returns:
            Out-of-service equipment records matching the requested filters.
        """
        body: dict[str, Any] = {}

        if city_ids is not None:
            body["CityID"] = city_ids
        if customer_ids is not None:
            body["CustomerID"] = customer_ids
        if department_group_ids is not None:
            body["DepartmentGroupID"] = department_group_ids
        if department_ids is not None:
            body["DepartmentID"] = department_ids
        if maintained_by_ids is not None:
            body["MaintainedByID"] = maintained_by_ids
        if make_ids is not None:
            body["MakeID"] = make_ids
        if model_ids is not None:
            body["ModelID"] = model_ids
        if power_ids is not None:
            body["PowerID"] = power_ids
        if region_ids is not None:
            body["RegionID"] = region_ids
        if show_detail:
            body["ShowDetail"] = True
        if vehicle_type_ids is not None:
            body["VehicleTypeID"] = vehicle_type_ids
        if work_center_ids is not None:
            body["WorkCenterID"] = work_center_ids
        if id_accessible:
            body["IDAccessible"] = True

        return self.post("equipment/outofservice/detail", body)

    def get_out_of_service_summary(self, id_accessible: bool = False) -> dict:
        """
        Retrieve live and snapshot out-of-service summary information for equipment.

        This endpoint has no filter parameters — it returns the full summary for all
        equipment accessible to the authenticated user.

        Args:
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.

        Returns:
            Out-of-service summary records including live and snapshot OOS data.
        """
        body: dict[str, Any] = {}

        if id_accessible:
            body["IDAccessible"] = True

        return self.post("equipment/outofservice/summary", body)

    def get_equipment_transfer_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying equipment transfers.

        Available list names: CityID.

        Args:
            list_names: Optional list of specific list names to return,
                        e.g. ["CityID"]. If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("equipment/transfer/lists", params=params)

    def get_equipment_transfers(
        self,
        transfer_dates: list[str],
        city_ids: list[int | str] | None = None,
        id_accessible: bool = False,
    ) -> dict:
        """
        Retrieve the history of equipment transferred between cities.

        Args:
            transfer_dates: (Required) One or more dates to query transfers for,
                            e.g. ["2024-01-25", "2024-01-26"].
            city_ids: Filter by city IDs or names. Use get_equipment_transfer_lists()
                      to find valid values.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.

        Returns:
            Equipment transfer history records for the requested dates and filters.
        """
        body: dict[str, Any] = {
            "TransferDate": transfer_dates,
        }

        if city_ids is not None:
            body["CityID"] = city_ids
        if id_accessible:
            body["IDAccessible"] = True

        return self.post("equipment/transfer", body)

    def get_equipment_addupdate_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when adding or updating equipment.

        Available list names: EquipTypeID, CityID, MeterProfileID, CustomerID, VehicleTypeID,
        ControllerID, MotorID, TelemetryIntegID, UserStatusID, DepartmentID, WorkCenterID,
        CostCenterID, BillingProfileID, ColorID, CurrencyID, ToolCertID, FleetConfigID,
        PartsCatalogID, PmPartKitID, PartListPartKitID, CategoryProfileID, EpaTypeID,
        LocationID, MaintainedByID, AerialMake1ID, AerialModel1ID, AtRiskID, AbeIndicatorID,
        FleetObjectID, LeassorID, PmiTypeID, StepConfigID, SystemStatusID, WorkClassID,
        PoiTypeID, EngineID, MakeID, ModelID, PowerID, TransmissionID, VendorID.

        Args:
            list_names: Optional list of specific list names to return,
                        e.g. ["EquipTypeID", "CityID"]. If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("equipment/addupdate/lists", params=params)

    def add_update_equipment(
        self,
        # Batch mode - mutually exclusive with single-record fields
        equipment_batch: list[dict] | None = None,
        # Single-record mode
        mode: str | None = None,
        # Record identity / lookup
        id: int | None = None,
        ebis_id: int | None = None,
        asset_id_lookup: int | None = None,
        city_abbr_lookup: str | None = None,
        # Core fields (required for Insert)
        city_id: int | None = None,
        city_no: str | None = None,
        equip_type_id: int | None = None,
        meter_profile_id: int | None = None,
        vehicle_type_id: int | None = None,
        # General fields
        customer_id: int | None = None,
        customer2_id: int | None = None,
        make1_id: int | None = None,
        model1_id: int | None = None,
        year_built: int | None = None,
        power1_id: int | None = None,
        engine1_id: int | None = None,
        engine1_serial: str | None = None,
        engine1_spec_no: str | None = None,
        transmission1_id: int | None = None,
        controller_id: int | None = None,
        motor_id: int | None = None,
        serial_no: str | None = None,
        vin: str | None = None,
        asset_no: str | None = None,
        stationary_loc: str | None = None,
        telemetry_integ_id: int | None = None,
        telemetry_vendor_asset_no: str | None = None,
        user_status_id: int | None = None,
        department_id: int | None = None,
        work_center_id: int | None = None,
        cost_center_id: int | None = None,
        billing_profile_id: int | None = None,
        tax_profile_id: int | None = None,
        color_id: int | None = None,
        color_other: str | None = None,
        license_no: str | None = None,
        cost: float | None = None,
        currency_id: int | None = None,
        in_service_date: str | None = None,
        in_service_refurb_date: str | None = None,
        warranty_expires: str | None = None,
        warranty_expires2: str | None = None,
        warranty_notes: str | None = None,
        surplus: bool | None = None,
        cab: bool | None = None,
        is_test: bool | None = None,
        has_seatbelt: bool | None = None,
        reflectivity: bool | None = None,
        ext_warranty: bool | None = None,
        purch_used: bool | None = None,
        disable_pm_wo_create: bool | None = None,
        notes: str | None = None,
        banner_status: str | None = None,
        # Secondary make/model/engine
        make2_id: int | None = None,
        model2_id: int | None = None,
        power2_id: int | None = None,
        engine2_id: int | None = None,
        engine2_serial: str | None = None,
        engine_spec_no2: str | None = None,
        serial_no2: str | None = None,
        # Engine detail
        engine1_hp: int | None = None,
        engine1_capacity: float | None = None,
        engine1_num_cyl: int | None = None,
        engine1_model_year: int | None = None,
        engine1_model_type: str | None = None,
        engine1_family_code: str | None = None,
        engine1_rpm: str | None = None,
        epa_type_id: int | None = None,
        epa_license_no: str | None = None,
        # Calibration / tool cert
        tool_cert_id: int | None = None,
        calib_date: str | None = None,
        due_date: str | None = None,
        label_date: str | None = None,
        calib_schedule: str | None = None,
        # Profile / catalog links
        fleet_config_id: int | None = None,
        parts_catalog_id: int | None = None,
        pm_part_kit_id: int | None = None,
        part_list_part_kit_id: int | None = None,
        category_profile_id: int | None = None,
        pm_parts_kit_disable: bool | None = None,
        # Location / org
        location_id: int | None = None,
        maintained_by_id: int | None = None,
        po_dest_stock_room_id: int | None = None,
        # Vendor
        vendor1_id: int | None = None,
        vendor1_contact: str | None = None,
        vendor2_id: int | None = None,
        vendor2_contact: str | None = None,
        # Dates / financial
        acquisition_date: str | None = None,
        delivery_date: str | None = None,
        replacement_date: str | None = None,
        lease_cost: float | None = None,
        lease_expires: str | None = None,
        retire_date: str | None = None,
        after_paint_date: str | None = None,
        inspection_date: str | None = None,
        rental_start_date: str | None = None,
        rental_expire_date: str | None = None,
        appraisal_value: float | None = None,
        book_value: float | None = None,
        disposal_value: float | None = None,
        sold_fee: float | None = None,
        sold_to: str | None = None,
        # License expiries
        airport_license: str | None = None,
        airport_lic_expire: str | None = None,
        city_lic_expire: str | None = None,
        state_lic_expire: str | None = None,
        county_lic_expire: str | None = None,
        country_lic_expire: str | None = None,
        # Physical / misc
        fuel_capacity: float | None = None,
        obj_length: float | None = None,
        obj_width: float | None = None,
        obj_height: float | None = None,
        obj_gross_weight: float | None = None,
        obj_empty_weight: float | None = None,
        obj_total_weight: float | None = None,
        freon_amount: str | None = None,
        freon_type: str | None = None,
        size_dimension: str | None = None,
        sort_field: str | None = None,
        env_no: str | None = None,
        shea_no: str | None = None,
        usage_indictator: int | None = None,
        gse_eq_count: int | None = None,
        construct_month: int | None = None,
        prior_asset_no: str | None = None,
        prior_owner: str | None = None,
        asset_mgm_no: str | None = None,
        chassis_no: str | None = None,
        eq_part_category: str | None = None,
        plant_section: str | None = None,
        county_reg: str | None = None,
        state_reg: str | None = None,
        country_reg: str | None = None,
        country_manuf: str | None = None,
        planner_group: str | None = None,
        planning_plant: str | None = None,
        identification: str | None = None,
        # Aerial / specialty
        aerial_make1_id: int | None = None,
        aerial_model1_id: int | None = None,
        aerial_serial: str | None = None,
        aerial_year_built: int | None = None,
        product_filter_type_id: int | None = None,
        at_risk_id: int | None = None,
        abe_indicator_id: int | None = None,
        fleet_object_id: int | None = None,
        leassor_id: int | None = None,
        pmi_type_id: int | None = None,
        step_config_id: int | None = None,
        system_status_id: int | None = None,
        work_class_id: int | None = None,
        poi_type_id: int | None = None,
        # Drivetrain serials
        transmission_serial: str | None = None,
        front_axel_serial: str | None = None,
        rear_axel_serial: str | None = None,
        front_torque: str | None = None,
        rear_torque: str | None = None,
        # City No insert helpers
        city_no_insert_type_id: int | None = None,
        city_no_insert_prefix: str | None = None,
        # Conveyor / specialty fields
        belt_type: str | None = None,
        belt_width_between: float | None = None,
        belt_length: str | None = None,
        drive_belt_no: str | None = None,
        clutch_brake_no: str | None = None,
        controller_type: str | None = None,
        bed_length: str | None = None,
        incline_angle: str | None = None,
        degree_of_turn: int | None = None,
        inside_radius: int | None = None,
        mfr_motor_framecode: str | None = None,
        mfr_no: str | None = None,
        master_control_no: str | None = None,
        motor_hp: float | None = None,
        oem: str | None = None,
        reducer_no: str | None = None,
        is_scale: bool | None = None,
        scale_capacity: float | None = None,
        scale_length: float | None = None,
        scale_revenue: float | None = None,
        scale_width: float | None = None,
        scale_height: float | None = None,
        motor_no: str | None = None,
        motor_mfr: str | None = None,
        reducer_mfr: str | None = None,
        reducer_ratio: str | None = None,
        workstation1: str | None = None,
        workstation2: str | None = None,
        # Mode=ChangeCityNo
        change_to_city_no: str | None = None,
        # Mode=ChangeEquipType
        change_to_equip_type_id: int | None = None,
        # Mode=Transfer
        transfer_to_city_id: int | None = None,
        transfer_to_work_center_id: int | None = None,
        transfer_to_cost_center_id: int | None = None,
        transfer_date: str | None = None,
        transfer_notes: str | None = None,
        transfer_inactivate: bool | None = None,
        transfer_activate: bool | None = None,
        transfer_move_open_wos: bool | None = None,
        transfer_void_open_wos: bool | None = None,
        # Mode=PowerChange
        power_change_to_power_id: int | None = None,
        power_change_to_engine_id: int | None = None,
        power_change_to_transmission_id: int | None = None,
        power_change_notes: str | None = None,
        power_change_engine1_serial: str | None = None,
        power_change_engine1_spec_no: str | None = None,
        power_change_engine1_family_code: str | None = None,
        power_change_engine1_rpm: str | None = None,
        power_change_engine1_hp: float | None = None,
        power_change_engine1_capacity: float | None = None,
        power_change_engine1_num_cyl: int | None = None,
        power_change_engine1_model_year: int | None = None,
        # Generic name-based lookups
        engine_id: int | str | None = None,
        make_id: int | str | None = None,
        model_id: int | str | None = None,
        power_id: int | str | None = None,
        telemetry_profile_id: int | str | None = None,
        transmission_id: int | str | None = None,
        vendor_id: int | str | None = None,
        user_validate_temp_token: str | None = None,
    ) -> dict:
        """
        Add or update one or more pieces of equipment in eBis Cloud.

        Supports two calling modes:
        - **Batch mode**: Pass a list of equipment dicts via `equipment_batch`. Each dict
          should contain a `Mode` and whichever fields apply to that record. A `LineNumber`
          in each dict is returned in the response to correlate results.
        - **Single-record mode**: Pass `mode` and individual field parameters directly.

        Equipment is matched (for Update/Activate/etc.) on any of: ID, EBisID,
        AssetIDLookup, CityAbbrLookup, or CityNo.

        Mode values and their requirements:
        - **Insert**: CityNo, CityID, VehicleTypeID, MeterProfileID, EquipTypeID required.
          Use city_no_insert_type_id / city_no_insert_prefix to auto-generate CityNo.
        - **Update**: Any general fields included will be updated.
        - **Activate**: Reactivates the equipment record.
        - **Inactivate**: Inactivates the equipment record.
        - **PowerChange**: Apply fields beginning with `power_change_*`.
        - **ChangeEquipType**: Requires `change_to_equip_type_id`.
        - **ChangeCityNo**: Requires `change_to_city_no`.
        - **Transfer**: Requires `transfer_to_city_id` and `transfer_date`.

        Use get_equipment_addupdate_lists() to find valid IDs for any ID parameter.

        Returns:
            List of per-equipment results, each with EBisID, LineNumber, MessageID,
            MessageText, and an Actions list detailing what was done and whether it succeeded.
        """
        if equipment_batch is not None:
            return self.post("equipment/addupdate", {"EquipmentBatch": equipment_batch})

        body: dict[str, Any] = {}

        if mode is not None:
            body["Mode"] = mode
        if id is not None:
            body["ID"] = id
        if ebis_id is not None:
            body["EBisID"] = ebis_id
        if asset_id_lookup is not None:
            body["AssetIDLookup"] = asset_id_lookup
        if city_abbr_lookup is not None:
            body["CityAbbrLookup"] = city_abbr_lookup
        if city_id is not None:
            body["CityID"] = city_id
        if city_no is not None:
            body["CityNo"] = city_no
        if equip_type_id is not None:
            body["EquipTypeID"] = equip_type_id
        if meter_profile_id is not None:
            body["MeterProfileID"] = meter_profile_id
        if vehicle_type_id is not None:
            body["VehicleTypeID"] = vehicle_type_id
        if customer_id is not None:
            body["CustomerID"] = customer_id
        if customer2_id is not None:
            body["Customer2ID"] = customer2_id
        if make1_id is not None:
            body["Make1ID"] = make1_id
        if model1_id is not None:
            body["Model1ID"] = model1_id
        if year_built is not None:
            body["YearBuilt"] = year_built
        if power1_id is not None:
            body["Power1ID"] = power1_id
        if engine1_id is not None:
            body["Engine1ID"] = engine1_id
        if engine1_serial is not None:
            body["Engine1Serial"] = engine1_serial
        if engine1_spec_no is not None:
            body["Engine1SpecNo"] = engine1_spec_no
        if transmission1_id is not None:
            body["Transmission1ID"] = transmission1_id
        if controller_id is not None:
            body["ControllerID"] = controller_id
        if motor_id is not None:
            body["MotorID"] = motor_id
        if serial_no is not None:
            body["SerialNo"] = serial_no
        if vin is not None:
            body["Vin"] = vin
        if asset_no is not None:
            body["AssetNo"] = asset_no
        if stationary_loc is not None:
            body["StationaryLoc"] = stationary_loc
        if telemetry_integ_id is not None:
            body["TelemetryIntegID"] = telemetry_integ_id
        if telemetry_vendor_asset_no is not None:
            body["TelemetryVendorAssetNo"] = telemetry_vendor_asset_no
        if user_status_id is not None:
            body["UserStatusID"] = user_status_id
        if department_id is not None:
            body["DepartmentID"] = department_id
        if work_center_id is not None:
            body["WorkCenterID"] = work_center_id
        if cost_center_id is not None:
            body["CostCenterID"] = cost_center_id
        if billing_profile_id is not None:
            body["BillingProfileID"] = billing_profile_id
        if tax_profile_id is not None:
            body["TaxProfileID"] = tax_profile_id
        if color_id is not None:
            body["ColorID"] = color_id
        if color_other is not None:
            body["ColorOther"] = color_other
        if license_no is not None:
            body["LicenseNo"] = license_no
        if cost is not None:
            body["Cost"] = cost
        if currency_id is not None:
            body["CurrencyID"] = currency_id
        if in_service_date is not None:
            body["InServiceDate"] = in_service_date
        if in_service_refurb_date is not None:
            body["InServiceRefurbDate"] = in_service_refurb_date
        if warranty_expires is not None:
            body["WarrantyExpires"] = warranty_expires
        if warranty_expires2 is not None:
            body["WarrantyExpires2"] = warranty_expires2
        if warranty_notes is not None:
            body["WarrantyNotes"] = warranty_notes
        if surplus is not None:
            body["Surplus"] = surplus
        if cab is not None:
            body["Cab"] = cab
        if is_test is not None:
            body["IsTest"] = is_test
        if has_seatbelt is not None:
            body["HasSeatbelt"] = has_seatbelt
        if reflectivity is not None:
            body["Reflectivity"] = reflectivity
        if ext_warranty is not None:
            body["ExtWarranty"] = ext_warranty
        if purch_used is not None:
            body["PurchUsed"] = purch_used
        if disable_pm_wo_create is not None:
            body["DisablePmWoCreate"] = disable_pm_wo_create
        if notes is not None:
            body["Notes"] = notes
        if banner_status is not None:
            body["BannerStatus"] = banner_status
        if make2_id is not None:
            body["Make2ID"] = make2_id
        if model2_id is not None:
            body["Model2ID"] = model2_id
        if power2_id is not None:
            body["Power2ID"] = power2_id
        if engine2_id is not None:
            body["Engine2ID"] = engine2_id
        if engine2_serial is not None:
            body["Engine2Serial"] = engine2_serial
        if engine_spec_no2 is not None:
            body["EngineSpecNo2"] = engine_spec_no2
        if serial_no2 is not None:
            body["SerialNo2"] = serial_no2
        if engine1_hp is not None:
            body["Engine1HP"] = engine1_hp
        if engine1_capacity is not None:
            body["Engine1Capacity"] = engine1_capacity
        if engine1_num_cyl is not None:
            body["Engine1NumCyl"] = engine1_num_cyl
        if engine1_model_year is not None:
            body["Engine1ModelYear"] = engine1_model_year
        if engine1_model_type is not None:
            body["Engine1ModelType"] = engine1_model_type
        if engine1_family_code is not None:
            body["Engine1FamilyCode"] = engine1_family_code
        if engine1_rpm is not None:
            body["Engine1Rpm"] = engine1_rpm
        if epa_type_id is not None:
            body["EpaTypeID"] = epa_type_id
        if epa_license_no is not None:
            body["EpaLicenseNo"] = epa_license_no
        if tool_cert_id is not None:
            body["ToolCertID"] = tool_cert_id
        if calib_date is not None:
            body["CalibDate"] = calib_date
        if due_date is not None:
            body["DueDate"] = due_date
        if label_date is not None:
            body["LabelDate"] = label_date
        if calib_schedule is not None:
            body["CalibSchedule"] = calib_schedule
        if fleet_config_id is not None:
            body["FleetConfigID"] = fleet_config_id
        if parts_catalog_id is not None:
            body["PartsCatalogID"] = parts_catalog_id
        if pm_part_kit_id is not None:
            body["PmPartKitID"] = pm_part_kit_id
        if part_list_part_kit_id is not None:
            body["PartListPartKitID"] = part_list_part_kit_id
        if category_profile_id is not None:
            body["CategoryProfileID"] = category_profile_id
        if pm_parts_kit_disable is not None:
            body["PmPartsKitDisable"] = pm_parts_kit_disable
        if location_id is not None:
            body["LocationID"] = location_id
        if maintained_by_id is not None:
            body["MaintainedByID"] = maintained_by_id
        if po_dest_stock_room_id is not None:
            body["PoDestStockRoomID"] = po_dest_stock_room_id
        if vendor1_id is not None:
            body["Vendor1ID"] = vendor1_id
        if vendor1_contact is not None:
            body["Vendor1Contact"] = vendor1_contact
        if vendor2_id is not None:
            body["Vendor2ID"] = vendor2_id
        if vendor2_contact is not None:
            body["Vendor2Contact"] = vendor2_contact
        if acquisition_date is not None:
            body["AcquisitionDate"] = acquisition_date
        if delivery_date is not None:
            body["DeliveryDate"] = delivery_date
        if replacement_date is not None:
            body["ReplacementDate"] = replacement_date
        if lease_cost is not None:
            body["LeaseCost"] = lease_cost
        if lease_expires is not None:
            body["LeaseExpires"] = lease_expires
        if retire_date is not None:
            body["RetireDate"] = retire_date
        if after_paint_date is not None:
            body["AfterPaintDate"] = after_paint_date
        if inspection_date is not None:
            body["InspectionDate"] = inspection_date
        if rental_start_date is not None:
            body["RentalStartDate"] = rental_start_date
        if rental_expire_date is not None:
            body["RentalExpireDate"] = rental_expire_date
        if appraisal_value is not None:
            body["AppraisalValue"] = appraisal_value
        if book_value is not None:
            body["BookValue"] = book_value
        if disposal_value is not None:
            body["DisposalValue"] = disposal_value
        if sold_fee is not None:
            body["SoldFee"] = sold_fee
        if sold_to is not None:
            body["SoldTo"] = sold_to
        if airport_license is not None:
            body["AirportLicense"] = airport_license
        if airport_lic_expire is not None:
            body["AirportLicExpire"] = airport_lic_expire
        if city_lic_expire is not None:
            body["CityLicExpire"] = city_lic_expire
        if state_lic_expire is not None:
            body["StateLicExpire"] = state_lic_expire
        if county_lic_expire is not None:
            body["CountyLicExpire"] = county_lic_expire
        if country_lic_expire is not None:
            body["CountryLicExpire"] = country_lic_expire
        if fuel_capacity is not None:
            body["FuelCapacity"] = fuel_capacity
        if obj_length is not None:
            body["ObjLength"] = obj_length
        if obj_width is not None:
            body["ObjWidth"] = obj_width
        if obj_height is not None:
            body["ObjHeight"] = obj_height
        if obj_gross_weight is not None:
            body["ObjGrossWeight"] = obj_gross_weight
        if obj_empty_weight is not None:
            body["ObjEmptyWeight"] = obj_empty_weight
        if obj_total_weight is not None:
            body["ObjTotalWeight"] = obj_total_weight
        if freon_amount is not None:
            body["FreonAmount"] = freon_amount
        if freon_type is not None:
            body["FreonType"] = freon_type
        if size_dimension is not None:
            body["SizeDimension"] = size_dimension
        if sort_field is not None:
            body["SortField"] = sort_field
        if env_no is not None:
            body["EnvNo"] = env_no
        if shea_no is not None:
            body["SheaNo"] = shea_no
        if usage_indictator is not None:
            body["UsageIndictator"] = usage_indictator
        if gse_eq_count is not None:
            body["GseEqCount"] = gse_eq_count
        if construct_month is not None:
            body["ConstructMonth"] = construct_month
        if prior_asset_no is not None:
            body["PriorAssetNo"] = prior_asset_no
        if prior_owner is not None:
            body["PriorOwner"] = prior_owner
        if asset_mgm_no is not None:
            body["AssetMgmNo"] = asset_mgm_no
        if chassis_no is not None:
            body["ChassisNo"] = chassis_no
        if eq_part_category is not None:
            body["EqPartCategory"] = eq_part_category
        if plant_section is not None:
            body["PlantSection"] = plant_section
        if county_reg is not None:
            body["CountyReg"] = county_reg
        if state_reg is not None:
            body["StateReg"] = state_reg
        if country_reg is not None:
            body["CountryReg"] = country_reg
        if country_manuf is not None:
            body["CountryManuf"] = country_manuf
        if planner_group is not None:
            body["PlannerGroup"] = planner_group
        if planning_plant is not None:
            body["PlanningPlant"] = planning_plant
        if identification is not None:
            body["Identification"] = identification
        if aerial_make1_id is not None:
            body["AerialMake1ID"] = aerial_make1_id
        if aerial_model1_id is not None:
            body["AerialModel1ID"] = aerial_model1_id
        if aerial_serial is not None:
            body["AerialSerial"] = aerial_serial
        if aerial_year_built is not None:
            body["AerialYearBuilt"] = aerial_year_built
        if product_filter_type_id is not None:
            body["ProductFilterTypeID"] = product_filter_type_id
        if at_risk_id is not None:
            body["AtRiskID"] = at_risk_id
        if abe_indicator_id is not None:
            body["AbeIndicatorID"] = abe_indicator_id
        if fleet_object_id is not None:
            body["FleetObjectID"] = fleet_object_id
        if leassor_id is not None:
            body["LeassorID"] = leassor_id
        if pmi_type_id is not None:
            body["PmiTypeID"] = pmi_type_id
        if step_config_id is not None:
            body["StepConfigID"] = step_config_id
        if system_status_id is not None:
            body["SystemStatusID"] = system_status_id
        if work_class_id is not None:
            body["WorkClassID"] = work_class_id
        if poi_type_id is not None:
            body["PoiTypeID"] = poi_type_id
        if transmission_serial is not None:
            body["TransmissionSerial"] = transmission_serial
        if front_axel_serial is not None:
            body["FrontAxelSerial"] = front_axel_serial
        if rear_axel_serial is not None:
            body["RearAxelSerial"] = rear_axel_serial
        if front_torque is not None:
            body["FrontTorque"] = front_torque
        if rear_torque is not None:
            body["RearTorque"] = rear_torque
        if city_no_insert_type_id is not None:
            body["CityNoInsertTypeID"] = city_no_insert_type_id
        if city_no_insert_prefix is not None:
            body["CityNoInsertPrefix"] = city_no_insert_prefix
        if belt_type is not None:
            body["BeltType"] = belt_type
        if belt_width_between is not None:
            body["BeltWidthBetween"] = belt_width_between
        if belt_length is not None:
            body["BeltLength"] = belt_length
        if drive_belt_no is not None:
            body["DriveBeltNo"] = drive_belt_no
        if clutch_brake_no is not None:
            body["ClutchBrakeNo"] = clutch_brake_no
        if controller_type is not None:
            body["ControllerType"] = controller_type
        if bed_length is not None:
            body["BedLength"] = bed_length
        if incline_angle is not None:
            body["InclineAngle"] = incline_angle
        if degree_of_turn is not None:
            body["DegreeOfTurn"] = degree_of_turn
        if inside_radius is not None:
            body["InsideRadius"] = inside_radius
        if mfr_motor_framecode is not None:
            body["MfrMotorFramecode"] = mfr_motor_framecode
        if mfr_no is not None:
            body["MfrNo"] = mfr_no
        if master_control_no is not None:
            body["MasterControlNo"] = master_control_no
        if motor_hp is not None:
            body["MotorHp"] = motor_hp
        if oem is not None:
            body["Oem"] = oem
        if reducer_no is not None:
            body["ReducerNo"] = reducer_no
        if is_scale is not None:
            body["IsScale"] = is_scale
        if scale_capacity is not None:
            body["ScaleCapacity"] = scale_capacity
        if scale_length is not None:
            body["ScaleLength"] = scale_length
        if scale_revenue is not None:
            body["ScaleRevenue"] = scale_revenue
        if scale_width is not None:
            body["ScaleWidth"] = scale_width
        if scale_height is not None:
            body["ScaleHeight"] = scale_height
        if motor_no is not None:
            body["MotorNo"] = motor_no
        if motor_mfr is not None:
            body["MotorMfr"] = motor_mfr
        if reducer_mfr is not None:
            body["ReducerMfr"] = reducer_mfr
        if reducer_ratio is not None:
            body["ReducerRatio"] = reducer_ratio
        if workstation1 is not None:
            body["Workstation1"] = workstation1
        if workstation2 is not None:
            body["Workstation2"] = workstation2
        if change_to_city_no is not None:
            body["ChangeToCityNo"] = change_to_city_no
        if change_to_equip_type_id is not None:
            body["ChangeToEquipTypeID"] = change_to_equip_type_id
        if transfer_to_city_id is not None:
            body["TransferToCityID"] = transfer_to_city_id
        if transfer_to_work_center_id is not None:
            body["TransferToWorkCenterID"] = transfer_to_work_center_id
        if transfer_to_cost_center_id is not None:
            body["TransferToCostCenterID"] = transfer_to_cost_center_id
        if transfer_date is not None:
            body["TransferDate"] = transfer_date
        if transfer_notes is not None:
            body["TransferNotes"] = transfer_notes
        if transfer_inactivate is not None:
            body["TransferInactivate"] = transfer_inactivate
        if transfer_activate is not None:
            body["TransferActivate"] = transfer_activate
        if transfer_move_open_wos is not None:
            body["TransferMoveOpenWos"] = transfer_move_open_wos
        if transfer_void_open_wos is not None:
            body["TransferVoidOpenWos"] = transfer_void_open_wos
        if power_change_to_power_id is not None:
            body["PowerChangeToPowerID"] = power_change_to_power_id
        if power_change_to_engine_id is not None:
            body["PowerChangeToEngineID"] = power_change_to_engine_id
        if power_change_to_transmission_id is not None:
            body["PowerChangeToTransmissionID"] = power_change_to_transmission_id
        if power_change_notes is not None:
            body["PowerChangeNotes"] = power_change_notes
        if power_change_engine1_serial is not None:
            body["PowerChangeEngine1Serial"] = power_change_engine1_serial
        if power_change_engine1_spec_no is not None:
            body["PowerChangeEngine1SpecNo"] = power_change_engine1_spec_no
        if power_change_engine1_family_code is not None:
            body["PowerChangeEngine1FamilyCode"] = power_change_engine1_family_code
        if power_change_engine1_rpm is not None:
            body["PowerChangeEngine1Rpm"] = power_change_engine1_rpm
        if power_change_engine1_hp is not None:
            body["PowerChangeEngine1HP"] = power_change_engine1_hp
        if power_change_engine1_capacity is not None:
            body["PowerChangeEngine1Capacity"] = power_change_engine1_capacity
        if power_change_engine1_num_cyl is not None:
            body["PowerChangeEngine1NumCyl"] = power_change_engine1_num_cyl
        if power_change_engine1_model_year is not None:
            body["PowerChangeEngine1ModelYear"] = power_change_engine1_model_year
        if engine_id is not None:
            body["EngineID"] = engine_id
        if make_id is not None:
            body["MakeID"] = make_id
        if model_id is not None:
            body["ModelID"] = model_id
        if power_id is not None:
            body["PowerID"] = power_id
        if telemetry_profile_id is not None:
            body["TelemetryProfileID"] = telemetry_profile_id
        if transmission_id is not None:
            body["TransmissionID"] = transmission_id
        if vendor_id is not None:
            body["VendorID"] = vendor_id
        if user_validate_temp_token is not None:
            body["UserValidateTempToken"] = user_validate_temp_token

        return self.post("equipment/addupdate", body)
