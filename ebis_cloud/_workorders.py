"""Work order API methods."""

from typing import Any


class WorkordersMixin:
    def get_workorder_lists(self, list_name: str | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when filtering work order exports.

        Args:
            list_name: Optional. Name of a specific list to return (e.g. 'CityID').
                       If omitted, all available lists are returned.

        Returns:
            Dict containing reference lists such as CityID with their IDs and Names.
        """
        params = {}
        if list_name:
            params["name"] = list_name
        return self.get("workorder/lists", params=params)

    def export_workorders(
        self,
        city_ids: list[int | str] | None = None,
        completed_dates: list[str] | None = None,
        created_dates: list[str] | None = None,
        include_billing_option: bool = False,
        include_invoice_media: bool = False,
        include_invoice_totals: bool = False,
        include_meter_reading: bool = False,
        include_outside_repair: bool = False,
        include_parts: bool = False,
        include_service: bool = False,
        include_service_logs: bool = False,
        include_signoffs: bool = False,
        include_wo_item_media: bool = False,
        include_wo_media: bool = False,
        hierarchy: str = "flat",
        id_accessible: bool = False,
    ) -> dict:
        """
        Export detailed work order information from eBis Cloud.

        Includes optional sections: Outside Repair, Signoffs, Service, Media, Parts, Invoices.

        Args:
            city_ids: Filter by city IDs or names, e.g. [1013, 1014, "Denver"].
                      Use get_workorder_lists(list_name='CityID') to find valid values.
            completed_dates: Filter by completion date(s), e.g. ["2024-01-25", "2024-01-26"].
            created_dates: Filter by creation date(s), e.g. ["2024-01-25", "2024-01-26"].
            include_billing_option: Include billing option data.
            include_invoice_media: Include invoice media attachments.
            include_invoice_totals: Include invoice totals.
            include_meter_reading: Include meter reading data.
            include_outside_repair: Include outside repair records.
            include_parts: Include parts records.
            include_service: Include service records.
            include_service_logs: Include service log records (includes technician names).
            include_signoffs: Include PM, QC, SafetyCheck, and SB signoffs.
            include_wo_item_media: Include media attached to individual work order items.
            include_wo_media: Include media attached to the work order.
            hierarchy: Response structure — "flat" (default) or "nested".
            id_accessible: If True, child lists are returned as object trees keyed by ID.

        Returns:
            Work order export data matching the requested filters and include options.
        """
        body: dict[str, Any] = {}

        if city_ids is not None:
            body["CityID"] = city_ids
        if completed_dates is not None:
            body["CompletedDate"] = completed_dates
        if created_dates is not None:
            body["CreatedDate"] = created_dates
        if include_billing_option:
            body["IncludeBillingOption"] = True
        if include_invoice_media:
            body["IncludeInvoiceMedia"] = True
        if include_invoice_totals:
            body["IncludeInvoiceTotals"] = True
        if include_meter_reading:
            body["IncludeMeterReading"] = True
        if include_outside_repair:
            body["IncludeOutsideRepair"] = True
        if include_parts:
            body["IncludeParts"] = True
        if include_service:
            body["IncludeService"] = True
        if include_service_logs:
            body["IncludeServiceLogs"] = True
        if include_signoffs:
            body["IncludeSignoffs"] = True
        if include_wo_item_media:
            body["IncludeWoItemMedia"] = True
        if include_wo_media:
            body["IncludeWoMedia"] = True
        if hierarchy != "flat":
            body["Hierarchy"] = hierarchy
        if id_accessible:
            body["IDAccessible"] = True

        return self.post("workorder", body)

    def get_workorder_addupdate_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when creating or updating a work order.

        Available list names: CityID, CustomerID, AircraftID, BillingProfileID, MeterProfileID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("workorder/addupdate/lists", params=params)

    def create_update_workorder(
        self,
        city_id: int | None = None,
        city_abbr: str | None = None,
        create_city_if_not_exists: bool = False,
        default_to_aircraft_city: bool = True,
        customer_id: int | None = None,
        customer_name: str | None = None,
        create_customer_if_not_exists: bool = False,
        default_to_aircraft_primary_customer: bool = True,
        aircraft_id: int | None = None,
        reg_num: str | None = None,
        create_aircraft_if_not_exists: bool = False,
        add_customer_to_aircraft_if_not_attached: bool = False,
        billing_profile_id: int | None = None,
        billing_profile_name: str | None = None,
        use_any_billing_profile: bool = True,
        meter_profile_id: int | None = None,
        meter_profile_name: str | None = None,
        use_any_meter_profile: bool = True,
        items: list[dict] | None = None,
        priority_id: int | None = None,
    ) -> dict:
        """
        Create or update a work order in eBis Cloud.

        eBis resolves city, customer, billing profile, and aircraft in order before
        creating the work order. Use get_workorder_addupdate_lists() to find valid IDs.

        Args:
            city_id: eBis ID for the intended city. Takes priority over city_abbr.
            city_abbr: Identify the city by name/abbreviation.
            create_city_if_not_exists: If True and city is not found, create it and continue.
            default_to_aircraft_city: If no city provided, use the aircraft's associated city.
            customer_id: eBis ID for the intended customer.
            customer_name: Identify the customer by name.
            create_customer_if_not_exists: If True and customer is not found, create it.
            default_to_aircraft_primary_customer: If no customer provided, use aircraft's primary customer.
            aircraft_id: eBis ID for the intended aircraft.
            reg_num: Identify the aircraft by registration/tail number.
            create_aircraft_if_not_exists: If True and aircraft is not found, create it.
            add_customer_to_aircraft_if_not_attached: If True and customer not linked, associate them.
            billing_profile_id: eBis ID for the intended billing profile.
            billing_profile_name: Identify the billing profile by name.
            use_any_billing_profile: If no billing profile provided, find and attach any available one.
            meter_profile_id: eBis ID for the meter profile (new aircraft only).
            meter_profile_name: Identify the meter profile by name (new aircraft only).
            use_any_meter_profile: If no meter profile provided for a new aircraft, find and attach any.
            items: List of work order line items. Each item is a dict with Discrepancy (required)
                   and optional LineNumber, Notes.
            priority_id: eBis ID for the work order priority.

        Returns:
            Dict with Data containing MessageID, ID, EBisWoLink, and resolution details.
        """
        payload: dict[str, Any] = {}

        if city_id is not None:
            payload["CityID"] = city_id
        if city_abbr is not None:
            payload["CityAbbr"] = city_abbr
        if create_city_if_not_exists:
            payload["CreateCityIfNotExists"] = True
        if not default_to_aircraft_city:
            payload["DefaultToAircraftCity"] = False

        if customer_id is not None:
            payload["CustomerID"] = customer_id
        if customer_name is not None:
            payload["CustomerName"] = customer_name
        if create_customer_if_not_exists:
            payload["CreateCustomerIfNotExists"] = True
        if not default_to_aircraft_primary_customer:
            payload["DefaultToAircraftPrimaryCustomer"] = False

        if aircraft_id is not None:
            payload["AircraftID"] = aircraft_id
        if reg_num is not None:
            payload["RegNum"] = reg_num
        if create_aircraft_if_not_exists:
            payload["CreateAircraftIfNotExists"] = True
        if add_customer_to_aircraft_if_not_attached:
            payload["AddCustomerToAircraftIfNotAttached"] = True

        if billing_profile_id is not None:
            payload["BillingProfileID"] = billing_profile_id
        if billing_profile_name is not None:
            payload["BillingProfileName"] = billing_profile_name
        if not use_any_billing_profile:
            payload["UseAnyBillingProfile"] = False

        if meter_profile_id is not None:
            payload["MeterProfileID"] = meter_profile_id
        if meter_profile_name is not None:
            payload["MeterProfileName"] = meter_profile_name
        if not use_any_meter_profile:
            payload["UseAnyMeterProfile"] = False

        if items:
            payload["Items"] = items
        if priority_id is not None:
            payload["PriorityID"] = priority_id

        return self.post("workorder/addupdate", payload)

    def get_workorder_totals_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when filtering work order totals.

        Available list names: CityID, CurrencyID, CustomerID, DepartmentID, FleetObjectID,
        MaintainedByID, MakeID, ModelID, RegionID, VehicleTypeID, WoCat1ID, WoCat2ID,
        WoCat3ID, WoDepartmentID, WorkCenterID, WoStatusID, WoTypeID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("workorder/totals/lists", params=params)

    def get_workorder_totals(
        self,
        completed_dates: list[str] | None = None,
        created_dates: list[str] | None = None,
        ac_reg_num: str | None = None,
        ac_serial_no: str | None = None,
        city_ids: list[int | str] | None = None,
        city_nos: list[str] | None = None,
        created_by_username_like: str | None = None,
        currency_ids: list[int | str] | None = None,
        customer_ids: list[int | str] | None = None,
        department_ids: list[int | str] | None = None,
        ebis_ids: list[int] | None = None,
        every_item: bool = False,
        fleet_object_ids: list[int | str] | None = None,
        group_by_invoice: bool = False,
        include_open_wos: bool = False,
        maintained_by_ids: list[int | str] | None = None,
        make_ids: list[int | str] | None = None,
        model_ids: list[int | str] | None = None,
        region_ids: list[int | str] | None = None,
        vehicle_type_ids: list[int | str] | None = None,
        void_work_orders: bool = False,
        wo_cat1_ids: list[int | str] | None = None,
        wo_cat2_ids: list[int | str] | None = None,
        wo_cat3_ids: list[int | str] | None = None,
        wo_corr_action: str | None = None,
        wo_department_ids: list[int | str] | None = None,
        wo_discrep: str | None = None,
        work_center_ids: list[int | str] | None = None,
        work_orders: list[str] | None = None,
        wo_status_ids: list[int | str] | None = None,
        wo_type_ids: list[int | str] | None = None,
        hierarchy: str = "flat",
        id_accessible: bool = False,
        full_debug: bool = False,
        unit_test: bool = False,
    ) -> dict:
        """
        Retrieve work order totals based on custom criteria.

        Use get_workorder_totals_lists() to discover valid ID/name values.

        Args:
            completed_dates: Limit to work orders completed within these dates.
            created_dates: Limit to work orders created on these dates.
            ac_reg_num: Filter by aircraft registration/tail number (exact match).
            ac_serial_no: Filter by aircraft serial number (exact match).
            city_ids: Filter by city IDs or names.
            city_nos: Filter by city number strings.
            created_by_username_like: Fragment search on the username that created the WO.
            currency_ids: Filter by currency IDs or names.
            customer_ids: Filter by customer IDs or names.
            department_ids: Filter by department IDs or names.
            ebis_ids: Filter by specific eBis internal work order IDs.
            every_item: If True, return a row per line item rather than per work order.
            fleet_object_ids: Filter by fleet object IDs or names.
            group_by_invoice: If True, group totals by invoice.
            include_open_wos: If True, include open (non-completed) work orders.
            maintained_by_ids: Filter by maintained-by organisation IDs or names.
            make_ids: Filter by aircraft make IDs or names.
            model_ids: Filter by aircraft model IDs or names.
            region_ids: Filter by region IDs or names.
            vehicle_type_ids: Filter by vehicle type IDs or names.
            void_work_orders: If True, include voided work orders.
            wo_cat1_ids: Filter by WO Category 1 IDs or names.
            wo_cat2_ids: Filter by WO Category 2 IDs or names.
            wo_cat3_ids: Filter by WO Category 3 IDs or names.
            wo_corr_action: Fragment search on corrective action text.
            wo_discrep: Fragment search on discrepancy text.
            work_center_ids: Filter by work center IDs or names.
            work_orders: Filter by work order number strings.
            wo_status_ids: Filter by work order status IDs or names.
            wo_type_ids: Filter by work order type IDs or names.
            hierarchy: Response structure — "flat" (default) or "nested".
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            full_debug: Enable full debug output (dev/testing use).
            unit_test: Enable unit test mode (dev/testing use).

        Returns:
            Work order totals matching the requested filters.
        """
        body: dict[str, Any] = {}

        if completed_dates is not None:
            body["CompletedDate"] = completed_dates
        if created_dates is not None:
            body["CreatedDate"] = created_dates
        if ac_reg_num is not None:
            body["AcRegNum"] = ac_reg_num
        if ac_serial_no is not None:
            body["AcSerialNo"] = ac_serial_no
        if city_ids is not None:
            body["CityID"] = city_ids
        if city_nos is not None:
            body["CityNo"] = city_nos
        if created_by_username_like is not None:
            body["CreatedByUsernameLike"] = created_by_username_like
        if currency_ids is not None:
            body["CurrencyID"] = currency_ids
        if customer_ids is not None:
            body["CustomerID"] = customer_ids
        if department_ids is not None:
            body["DepartmentID"] = department_ids
        if ebis_ids is not None:
            body["EBisID"] = ebis_ids
        if every_item:
            body["EveryItem"] = True
        if fleet_object_ids is not None:
            body["FleetObjectID"] = fleet_object_ids
        if group_by_invoice:
            body["GroupByInvoice"] = True
        if include_open_wos:
            body["IncludeOpenWos"] = True
        if maintained_by_ids is not None:
            body["MaintainedByID"] = maintained_by_ids
        if make_ids is not None:
            body["MakeID"] = make_ids
        if model_ids is not None:
            body["ModelID"] = model_ids
        if region_ids is not None:
            body["RegionID"] = region_ids
        if vehicle_type_ids is not None:
            body["VehicleTypeID"] = vehicle_type_ids
        if void_work_orders:
            body["VoidWorkOrders"] = True
        if wo_cat1_ids is not None:
            body["WoCat1ID"] = wo_cat1_ids
        if wo_cat2_ids is not None:
            body["WoCat2ID"] = wo_cat2_ids
        if wo_cat3_ids is not None:
            body["WoCat3ID"] = wo_cat3_ids
        if wo_corr_action is not None:
            body["WoCorrAction"] = wo_corr_action
        if wo_department_ids is not None:
            body["WoDepartmentID"] = wo_department_ids
        if wo_discrep is not None:
            body["WoDiscrep"] = wo_discrep
        if work_center_ids is not None:
            body["WorkCenterID"] = work_center_ids
        if work_orders is not None:
            body["WorkOrder"] = work_orders
        if wo_status_ids is not None:
            body["WoStatusID"] = wo_status_ids
        if wo_type_ids is not None:
            body["WoTypeID"] = wo_type_ids
        if hierarchy != "flat":
            body["Hierarchy"] = hierarchy
        if id_accessible:
            body["IDAccessible"] = True
        if full_debug:
            body["FullDebug"] = True
        if unit_test:
            body["UnitTest"] = True

        return self.post("workorder/totals", body)

    def get_outside_repair_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when filtering outside repair searches.

        Available list names: CityID, CostCenterID, CustomerID, DepartmentID, EngineID,
        IbsID, MakeID, ModelID, RegionID, StatusTypeID, UserStatusID, VehicleTypeID,
        WoActionCategoryID, WoCategoryID, WorkCenterID, WoStatusID, WoSubCategoryID, WoTypeID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("workorder/outsiderepair/lists", params=params)

    def search_outside_repair(
        self,
        completed_dates: list[str] | None = None,
        date_added: list[str] | None = None,
        added_by_user_like: str | None = None,
        all_accessible_cities: bool = False,
        city_ids: list[int | str] | None = None,
        city_no_like: str | None = None,
        cost_center_ids: list[int | str] | None = None,
        customer_ids: list[int | str] | None = None,
        department_ids: list[int | str] | None = None,
        engine1_serial: str | None = None,
        engine_ids: list[int | str] | None = None,
        ibs_ids: list[int | str] | None = None,
        make_ids: list[int | str] | None = None,
        model_ids: list[int | str] | None = None,
        output_only_detail: bool = False,
        part_description: str | None = None,
        part_number: str | None = None,
        region_ids: list[int | str] | None = None,
        reg_nums: list[str] | None = None,
        serial_no: str | None = None,
        show_deleted_only: bool = False,
        status_type_id: int | str | None = None,
        user_status_ids: list[int | str] | None = None,
        vehicle_type_abbrs: list[str] | None = None,
        vehicle_type_ids: list[int | str] | None = None,
        vendor_name: str | None = None,
        vin: str | None = None,
        wo_action_category_ids: list[int | str] | None = None,
        wo_category_ids: list[int | str] | None = None,
        work_center_ids: list[int | str] | None = None,
        work_order_like: str | None = None,
        wo_status_ids: list[int | str] | None = None,
        wo_sub_category_ids: list[int | str] | None = None,
        wo_type_ids: list[int | str] | None = None,
        year_built: list[int] | None = None,
        hierarchy: str = "flat",
        id_accessible: bool = False,
        language: str | None = None,
    ) -> dict:
        """
        Search outside repair items based on custom criteria.

        Use get_outside_repair_lists() to discover valid ID/name values.

        Args:
            completed_dates: Limit to work orders completed within these dates.
            date_added: Filter by the date the outside repair was added.
            added_by_user_like: Fragment search on the username that added the outside repair.
            all_accessible_cities: If True, include all cities accessible to the user.
            city_ids: Filter by city IDs or names.
            city_no_like: Fragment search on city number.
            cost_center_ids: Filter by cost center IDs or names.
            customer_ids: Filter by customer IDs or names.
            department_ids: Filter by department IDs or names.
            engine1_serial: Fragment search on engine 1 serial number.
            engine_ids: Filter by engine IDs or names.
            ibs_ids: Filter by IBS IDs or names.
            make_ids: Filter by aircraft make IDs or names.
            model_ids: Filter by aircraft model IDs or names.
            output_only_detail: If True, output only detail-level records.
            part_description: Fragment search on part description.
            part_number: Fragment search on part number.
            region_ids: Filter by region IDs or names.
            reg_nums: Filter by aircraft registration/tail numbers.
            serial_no: Fragment search on aircraft serial number.
            show_deleted_only: If True, return only deleted outside repair records.
            status_type_id: Filter by a single status type ID or name.
            user_status_ids: Filter by user status IDs or names.
            vehicle_type_abbrs: Filter by vehicle type abbreviations.
            vehicle_type_ids: Filter by vehicle type IDs or names.
            vendor_name: Fragment search on vendor name.
            vin: Fragment search on VIN.
            wo_action_category_ids: Filter by WO action category IDs or names.
            wo_category_ids: Filter by WO category IDs or names.
            work_center_ids: Filter by work center IDs or names.
            work_order_like: Fragment search on work order number.
            wo_status_ids: Filter by work order status IDs or names.
            wo_sub_category_ids: Filter by WO sub-category IDs or names.
            wo_type_ids: Filter by work order type IDs or names.
            year_built: Filter by aircraft year(s) built.
            hierarchy: Response structure — "flat" (default) or "nested".
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            language: Language for generic list parameter lookups (default: "English").

        Returns:
            Outside repair records matching the requested filters.
        """
        body: dict[str, Any] = {}

        if completed_dates is not None:
            body["CompletedDate"] = completed_dates
        if date_added is not None:
            body["DateAdded"] = date_added
        if added_by_user_like is not None:
            body["AddedByUserLike"] = added_by_user_like
        if all_accessible_cities:
            body["AllAccessibleCities"] = True
        if city_ids is not None:
            body["CityID"] = city_ids
        if city_no_like is not None:
            body["CityNoLike"] = city_no_like
        if cost_center_ids is not None:
            body["CostCenterID"] = cost_center_ids
        if customer_ids is not None:
            body["CustomerID"] = customer_ids
        if department_ids is not None:
            body["DepartmentID"] = department_ids
        if engine1_serial is not None:
            body["Engine1Serial"] = engine1_serial
        if engine_ids is not None:
            body["EngineID"] = engine_ids
        if ibs_ids is not None:
            body["IbsID"] = ibs_ids
        if make_ids is not None:
            body["MakeID"] = make_ids
        if model_ids is not None:
            body["ModelID"] = model_ids
        if output_only_detail:
            body["OutputOnlyDetail"] = True
        if part_description is not None:
            body["PartDescription"] = part_description
        if part_number is not None:
            body["PartNumber"] = part_number
        if region_ids is not None:
            body["RegionID"] = region_ids
        if reg_nums is not None:
            body["RegNum"] = reg_nums
        if serial_no is not None:
            body["SerialNo"] = serial_no
        if show_deleted_only:
            body["ShowDeletedOnly"] = True
        if status_type_id is not None:
            body["StatusTypeID"] = status_type_id
        if user_status_ids is not None:
            body["UserStatusID"] = user_status_ids
        if vehicle_type_abbrs is not None:
            body["VehicleTypeAbbr"] = vehicle_type_abbrs
        if vehicle_type_ids is not None:
            body["VehicleTypeID"] = vehicle_type_ids
        if vendor_name is not None:
            body["VendorName"] = vendor_name
        if vin is not None:
            body["Vin"] = vin
        if wo_action_category_ids is not None:
            body["WoActionCategoryID"] = wo_action_category_ids
        if wo_category_ids is not None:
            body["WoCategoryID"] = wo_category_ids
        if work_center_ids is not None:
            body["WorkCenterID"] = work_center_ids
        if work_order_like is not None:
            body["WorkOrderLike"] = work_order_like
        if wo_status_ids is not None:
            body["WoStatusID"] = wo_status_ids
        if wo_sub_category_ids is not None:
            body["WoSubCategoryID"] = wo_sub_category_ids
        if wo_type_ids is not None:
            body["WoTypeID"] = wo_type_ids
        if year_built is not None:
            body["YearBuilt"] = year_built
        if hierarchy != "flat":
            body["Hierarchy"] = hierarchy
        if id_accessible:
            body["IDAccessible"] = True
        if language is not None:
            body["Language"] = language

        return self.post("workorder/outsiderepair", body)

    def get_workorder_listing_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying work order listings.

        Available list names: CityGroupID, CityID, CustomerID, EngineID, MaintainedByID,
        MakeID, ModelID, PmDocID, RegionID, SortByID, VehicleTypeID, WoActionCategoryID,
        WoCategoryID, WorkCenterID, WoStatusID, WoSubCategoryID, WoTypeID, ZoneID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("workorder/listing/lists", params=params)

    def get_workorder_listing(
        self,
        wo_status_id: int | str,
        wo_type_id: int | str,
        city_group_ids: list[int | str] | None = None,
        city_ids: list[int | str] | None = None,
        city_no: str | None = None,
        completed_dates: list[str] | None = None,
        created_dates: list[str] | None = None,
        customer_ids: list[int | str] | None = None,
        detailed_export: bool = False,
        due_dates: list[str] | None = None,
        engine_ids: list[int | str] | None = None,
        export_all_items: bool = False,
        export_invoice_totals: bool = False,
        has_customer_po: str | None = None,
        maintained_by_ids: list[int | str] | None = None,
        make_ids: list[int | str] | None = None,
        model_ids: list[int | str] | None = None,
        pm_doc_ids: list[int | str] | None = None,
        region_ids: list[int | str] | None = None,
        sort_by_id: int | str | None = None,
        vehicle_type_ids: list[int | str] | None = None,
        wo_action_category_ids: list[int | str] | None = None,
        wo_category_ids: list[int | str] | None = None,
        work_center_ids: list[int | str] | None = None,
        wo_sub_category_ids: list[int | str] | None = None,
        zone_ids: list[int | str] | None = None,
        hierarchy: str = "flat",
        id_accessible: bool = False,
        language: str | None = None,
    ) -> dict:
        """
        Retrieve work order listing information based on custom criteria.

        Use get_workorder_listing_lists() to discover valid ID/name values.

        Args:
            wo_status_id: (Required) Work order status ID or name.
            wo_type_id: (Required) Work order type ID or name.
            city_group_ids: Filter by city group IDs or names.
            city_ids: Filter by city IDs or names.
            city_no: Fragment search on city number.
            completed_dates: Filter by completion date(s).
            created_dates: Filter by creation date(s).
            customer_ids: Filter by customer IDs or names.
            detailed_export: If True, include detailed line-item data.
            due_dates: Filter by due date(s).
            engine_ids: Filter by engine IDs or names.
            export_all_items: If True, export all work order items.
            export_invoice_totals: If True, include invoice totals.
            has_customer_po: Filter by customer PO presence — "yes", "no", or "all".
            maintained_by_ids: Filter by maintained-by organisation IDs or names.
            make_ids: Filter by aircraft make IDs or names.
            model_ids: Filter by aircraft model IDs or names.
            pm_doc_ids: Filter by PM document IDs or names.
            region_ids: Filter by region IDs or names.
            sort_by_id: Sort results by this field ID or name.
            vehicle_type_ids: Filter by vehicle type IDs or names.
            wo_action_category_ids: Filter by WO action category IDs or names.
            wo_category_ids: Filter by WO category IDs or names.
            work_center_ids: Filter by work center IDs or names.
            wo_sub_category_ids: Filter by WO sub-category IDs or names.
            zone_ids: Filter by zone IDs or names.
            hierarchy: Response structure — only "flat" is supported.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            language: Language for generic list parameter lookups (default: "English").

        Returns:
            Work order listing records matching the requested filters.
        """
        body: dict[str, Any] = {
            "WoStatusID": wo_status_id,
            "WoTypeID": wo_type_id,
        }

        if city_group_ids is not None:
            body["CityGroupID"] = city_group_ids
        if city_ids is not None:
            body["CityID"] = city_ids
        if city_no is not None:
            body["CityNo"] = city_no
        if completed_dates is not None:
            body["CompletedDate"] = completed_dates
        if created_dates is not None:
            body["CreatedDate"] = created_dates
        if customer_ids is not None:
            body["CustomerID"] = customer_ids
        if detailed_export:
            body["DetailedExport"] = True
        if due_dates is not None:
            body["DueDate"] = due_dates
        if engine_ids is not None:
            body["EngineID"] = engine_ids
        if export_all_items:
            body["ExportAllItems"] = True
        if export_invoice_totals:
            body["ExportInvoiceTotals"] = True
        if has_customer_po is not None:
            body["HasCustomerPo"] = has_customer_po
        if maintained_by_ids is not None:
            body["MaintainedByID"] = maintained_by_ids
        if make_ids is not None:
            body["MakeID"] = make_ids
        if model_ids is not None:
            body["ModelID"] = model_ids
        if pm_doc_ids is not None:
            body["PmDocID"] = pm_doc_ids
        if region_ids is not None:
            body["RegionID"] = region_ids
        if sort_by_id is not None:
            body["SortByID"] = sort_by_id
        if vehicle_type_ids is not None:
            body["VehicleTypeID"] = vehicle_type_ids
        if wo_action_category_ids is not None:
            body["WoActionCategoryID"] = wo_action_category_ids
        if wo_category_ids is not None:
            body["WoCategoryID"] = wo_category_ids
        if work_center_ids is not None:
            body["WorkCenterID"] = work_center_ids
        if wo_sub_category_ids is not None:
            body["WoSubCategoryID"] = wo_sub_category_ids
        if zone_ids is not None:
            body["ZoneID"] = zone_ids
        if hierarchy != "flat":
            body["Hierarchy"] = hierarchy
        if id_accessible:
            body["IDAccessible"] = True
        if language is not None:
            body["Language"] = language

        return self.post("workorder/listing", body)

    def get_workorder_compliance_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying work order compliance.

        Available list names: CityID, CustomerID, MaintainedByID, RegionID,
        SummaryGroupByID, WorkCenterID, ZoneID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("workorder/compliance/lists", params=params)

    def get_workorder_compliance(
        self,
        summary_group_by_id: int | str,
        city_ids: list[int | str] | None = None,
        completed_dates: list[str] | None = None,
        customer_ids: list[int | str] | None = None,
        due_dates: list[str] | None = None,
        maintained_by_ids: list[int | str] | None = None,
        region_ids: list[int | str] | None = None,
        show_unassigned_workcenter: bool = False,
        work_center_ids: list[int | str] | None = None,
        zone_ids: list[int | str] | None = None,
        id_accessible: bool = False,
        language: str | None = None,
    ) -> dict:
        """
        Retrieve compliance information about whether work orders are created on time.

        Use get_workorder_compliance_lists() to discover valid ID/name values.

        Args:
            summary_group_by_id: (Required) Field to group the compliance summary by.
            city_ids: Filter by city IDs or names.
            completed_dates: Filter by work order completion date(s).
            customer_ids: Filter by customer IDs or names.
            due_dates: Filter by work order due date(s).
            maintained_by_ids: Filter by maintained-by organisation IDs or names.
            region_ids: Filter by region IDs or names.
            show_unassigned_workcenter: If True, include work orders with no assigned work center.
            work_center_ids: Filter by work center IDs or names.
            zone_ids: Filter by zone IDs or names.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            language: Language for generic list parameter lookups (default: "English").

        Returns:
            Compliance records indicating whether work orders were created on time.
        """
        body: dict[str, Any] = {
            "SummaryGroupByID": summary_group_by_id,
        }

        if city_ids is not None:
            body["CityID"] = city_ids
        if completed_dates is not None:
            body["CompletedDate"] = completed_dates
        if customer_ids is not None:
            body["CustomerID"] = customer_ids
        if due_dates is not None:
            body["DueDate"] = due_dates
        if maintained_by_ids is not None:
            body["MaintainedByID"] = maintained_by_ids
        if region_ids is not None:
            body["RegionID"] = region_ids
        if show_unassigned_workcenter:
            body["ShowUnassignedWorkcenter"] = True
        if work_center_ids is not None:
            body["WorkCenterID"] = work_center_ids
        if zone_ids is not None:
            body["ZoneID"] = zone_ids
        if id_accessible:
            body["IDAccessible"] = True
        if language is not None:
            body["Language"] = language

        return self.post("workorder/compliance", body)

    def get_part_history_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying work order part history.

        Available list names: CityID, CostCenterID, CustomerID, DepartmentID, Engine1ID,
        IbsID, Make1ID, Model1ID, PartComponentID, PartTypeID, RegionID, StatusTypeID,
        UserStatusID, VehicleTypeID, WoActionCategoryID, WoCategoryID, WoEbisMainTypeID,
        WorkCenterID, WoStatusID, WoSubCategoryID, WoTypeID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("workorder/parthistory/lists", params=params)

    def get_part_history(
        self,
        added_by_user_like: str | None = None,
        all_accessible_cities: bool = False,
        city_ids: list[int | str] | None = None,
        city_no_like: str | None = None,
        completed_dates: list[str] | None = None,
        cost_center_ids: list[int | str] | None = None,
        customer_ids: list[int | str] | None = None,
        date_added: list[str] | None = None,
        date_used: list[str] | None = None,
        department_ids: list[int | str] | None = None,
        engine1_ids: list[int | str] | None = None,
        engine1_serial: str | None = None,
        ibs_ids: list[int | str] | None = None,
        line_code: str | None = None,
        make1_ids: list[int | str] | None = None,
        model1_ids: list[int | str] | None = None,
        part_component_ids: list[int | str] | None = None,
        part_description: str | None = None,
        part_number: str | None = None,
        parts_not_in_master_parts: bool = False,
        parts_with_serial_numbers: bool = False,
        part_type_ids: list[int | str] | None = None,
        region_ids: list[int | str] | None = None,
        reg_nums: list[str] | None = None,
        serial_no: str | None = None,
        show_deleted_only: bool = False,
        status_type_id: int | str | None = None,
        user_status_ids: list[int | str] | None = None,
        vehicle_type_abbrs: list[str] | None = None,
        vehicle_type_ids: list[int | str] | None = None,
        vin: str | None = None,
        wo_action_category_ids: list[int | str] | None = None,
        wo_category_ids: list[int | str] | None = None,
        wo_date_created: list[str] | None = None,
        wo_ebis_main_type_ids: list[int | str] | None = None,
        work_center_ids: list[int | str] | None = None,
        work_order_like: str | None = None,
        wo_status_ids: list[int | str] | None = None,
        wo_sub_category_ids: list[int | str] | None = None,
        wo_type_ids: list[int | str] | None = None,
        year_built: list[int] | None = None,
        id_accessible: bool = False,
        language: str | None = None,
    ) -> dict:
        """
        Retrieve work order part usage history based on custom criteria.

        Use get_part_history_lists() to discover valid ID/name values.

        Args:
            added_by_user_like: Fragment search on the username that added the part record.
            all_accessible_cities: If True, include all cities accessible to the user.
            city_ids: Filter by city IDs or names.
            city_no_like: Fragment search on city number.
            completed_dates: Filter by work order completion date(s).
            cost_center_ids: Filter by cost center IDs or names.
            customer_ids: Filter by customer IDs or names.
            date_added: Filter by the date the part was added.
            date_used: Filter by the date the part was used.
            department_ids: Filter by department IDs or names.
            engine1_ids: Filter by primary engine IDs or names.
            engine1_serial: Fragment search on primary engine serial number.
            ibs_ids: Filter by IBS IDs or names.
            line_code: Fragment search on part line code.
            make1_ids: Filter by aircraft make IDs or names.
            model1_ids: Filter by aircraft model IDs or names.
            part_component_ids: Filter by part component IDs or names.
            part_description: Fragment search on part description.
            part_number: Fragment search on part number.
            parts_not_in_master_parts: If True, return only parts not found in master parts list.
            parts_with_serial_numbers: If True, return only parts that have serial numbers.
            part_type_ids: Filter by part type IDs or names.
            region_ids: Filter by region IDs or names.
            reg_nums: Filter by aircraft registration/tail numbers.
            serial_no: Fragment search on aircraft serial number.
            show_deleted_only: If True, return only deleted part history records.
            status_type_id: Filter by a single status type ID or name.
            user_status_ids: Filter by user status IDs or names.
            vehicle_type_abbrs: Filter by vehicle type abbreviations.
            vehicle_type_ids: Filter by vehicle type IDs or names.
            vin: Fragment search on VIN.
            wo_action_category_ids: Filter by WO action category IDs or names.
            wo_category_ids: Filter by WO category IDs or names.
            wo_date_created: Filter by work order creation date(s).
            wo_ebis_main_type_ids: Filter by eBis main type IDs or names.
            work_center_ids: Filter by work center IDs or names.
            work_order_like: Fragment search on work order number.
            wo_status_ids: Filter by work order status IDs or names.
            wo_sub_category_ids: Filter by WO sub-category IDs or names.
            wo_type_ids: Filter by work order type IDs or names.
            year_built: Filter by aircraft year(s) built.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            language: Language for generic list parameter lookups (default: "English").

        Returns:
            Part history records matching the requested filters.
        """
        body: dict[str, Any] = {}

        if added_by_user_like is not None:
            body["AddedByUserLike"] = added_by_user_like
        if all_accessible_cities:
            body["AllAccessibleCities"] = True
        if city_ids is not None:
            body["CityID"] = city_ids
        if city_no_like is not None:
            body["CityNoLike"] = city_no_like
        if completed_dates is not None:
            body["CompletedDate"] = completed_dates
        if cost_center_ids is not None:
            body["CostCenterID"] = cost_center_ids
        if customer_ids is not None:
            body["CustomerID"] = customer_ids
        if date_added is not None:
            body["DateAdded"] = date_added
        if date_used is not None:
            body["DateUsed"] = date_used
        if department_ids is not None:
            body["DepartmentID"] = department_ids
        if engine1_ids is not None:
            body["Engine1ID"] = engine1_ids
        if engine1_serial is not None:
            body["Engine1Serial"] = engine1_serial
        if ibs_ids is not None:
            body["IbsID"] = ibs_ids
        if line_code is not None:
            body["LineCode"] = line_code
        if make1_ids is not None:
            body["Make1ID"] = make1_ids
        if model1_ids is not None:
            body["Model1ID"] = model1_ids
        if part_component_ids is not None:
            body["PartComponentID"] = part_component_ids
        if part_description is not None:
            body["PartDescription"] = part_description
        if part_number is not None:
            body["PartNumber"] = part_number
        if parts_not_in_master_parts:
            body["PartsNotInMasterParts"] = True
        if parts_with_serial_numbers:
            body["PartsWithSerialNumbers"] = True
        if part_type_ids is not None:
            body["PartTypeID"] = part_type_ids
        if region_ids is not None:
            body["RegionID"] = region_ids
        if reg_nums is not None:
            body["RegNum"] = reg_nums
        if serial_no is not None:
            body["SerialNo"] = serial_no
        if show_deleted_only:
            body["ShowDeletedOnly"] = True
        if status_type_id is not None:
            body["StatusTypeID"] = status_type_id
        if user_status_ids is not None:
            body["UserStatusID"] = user_status_ids
        if vehicle_type_abbrs is not None:
            body["VehicleTypeAbbr"] = vehicle_type_abbrs
        if vehicle_type_ids is not None:
            body["VehicleTypeID"] = vehicle_type_ids
        if vin is not None:
            body["Vin"] = vin
        if wo_action_category_ids is not None:
            body["WoActionCategoryID"] = wo_action_category_ids
        if wo_category_ids is not None:
            body["WoCategoryID"] = wo_category_ids
        if wo_date_created is not None:
            body["WoDateCreated"] = wo_date_created
        if wo_ebis_main_type_ids is not None:
            body["WoEbisMainTypeID"] = wo_ebis_main_type_ids
        if work_center_ids is not None:
            body["WorkCenterID"] = work_center_ids
        if work_order_like is not None:
            body["WorkOrderLike"] = work_order_like
        if wo_status_ids is not None:
            body["WoStatusID"] = wo_status_ids
        if wo_sub_category_ids is not None:
            body["WoSubCategoryID"] = wo_sub_category_ids
        if wo_type_ids is not None:
            body["WoTypeID"] = wo_type_ids
        if year_built is not None:
            body["YearBuilt"] = year_built
        if id_accessible:
            body["IDAccessible"] = True
        if language is not None:
            body["Language"] = language

        return self.post("workorder/parthistory", body)

    def get_tech_activity_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying technician activity.

        Available list names: TechGroupID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("workorder/techactivity/lists", params=params)

    def get_tech_activity(
        self,
        dates: list[str],
        city_ids: list[int | str] | None = None,
        tech_group_ids: list[int | str] | None = None,
        technician_ids: list[int | str] | None = None,
        id_accessible: bool = False,
        full_debug: bool = False,
    ) -> dict:
        """
        Retrieve detailed logs of technician activity on work orders.

        Use get_tech_activity_lists() to discover valid TechGroupID values.

        Args:
            dates: (Required) One or more dates to query activity for, e.g. ["2024-01-25"].
            city_ids: Filter by city IDs or names. Submit [-1] to include all accessible cities.
            tech_group_ids: Filter by technician group IDs or names.
            technician_ids: Filter by individual technician IDs or names.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            full_debug: Enable full debug output (dev/testing use).

        Returns:
            Technician activity log records for the requested dates and filters.
        """
        body: dict[str, Any] = {
            "Date": dates,
        }

        if city_ids is not None:
            body["CityID"] = city_ids
        if tech_group_ids is not None:
            body["TechGroupID"] = tech_group_ids
        if technician_ids is not None:
            body["TechnicianID"] = technician_ids
        if id_accessible:
            body["IDAccessible"] = True
        if full_debug:
            body["FullDebug"] = True

        return self.post("workorder/techactivity", body)

    def resync_billing_and_tax(
        self,
        wo_id_list: list[int],
        full_debug: bool = False,
    ) -> dict:
        """
        Resynchronize billing, tax, and invoice information for one or more work orders.

        Args:
            wo_id_list: (Required) List of work order IDs to resync, e.g. [111, 234, 399].
            full_debug: Enable full debug output (dev/testing use).

        Returns:
            Result of the billing/tax resync operation for the specified work orders.
        """
        body: dict[str, Any] = {
            "WoIDList": wo_id_list,
        }

        if full_debug:
            body["FullDebug"] = True

        return self.post("workorder/billingresync", body)
