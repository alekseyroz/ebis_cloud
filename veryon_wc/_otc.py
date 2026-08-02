"""Over-the-counter (OTC) API methods."""

from typing import Any


class OtcMixin:
    def get_otc_listing_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying OTC listings.

        Available list names: EBisMainTypeID, CityID, StatusID, CustomerID, TypeID, DepartmentID.
        EBisMainTypeID values: 1=Quote, 2=Invoice, 3=CoreInvoice.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("otc/listing/lists", params=params)

    def get_otc_listing(
        self,
        ebis_main_type_ids: list[int | str] | None = None,
        back_order_is: str | None = None,
        return_is: str | None = None,
        original_quote_number: str | None = None,
        reminder_due_next_days: int | None = None,
        filter_text: str | None = None,
        include_parts: bool = False,
        include_misc_charges: bool = False,
        otc_id: int | None = None,
        city_ids: list[int | str] | None = None,
        status_ids: list[int | str] | None = None,
        customer_ids: list[int | str] | None = None,
        type_ids: list[int | str] | None = None,
        department_ids: list[int | str] | None = None,
        show_mine_only: bool = False,
        accounting_invoice_num: str | None = None,
        buyer_contact: str | None = None,
        buyer_purchase_order: str | None = None,
        created_dates: list[str] | None = None,
        display_dates: list[str] | None = None,
        est_ship_dates: list[str] | None = None,
        has_media: str | None = None,
        has_misc_charges: str | None = None,
        misc_charge: str | None = None,
        notes: str | None = None,
        part_description: str | None = None,
        part_number: str | None = None,
        part_serial_no: str | None = None,
        payment_due_dates: list[str] | None = None,
        processed_dates: list[str] | None = None,
        shipped_dates: list[str] | None = None,
        tracking_number: str | None = None,
        rpt_sort: str | None = None,
        hierarchy: str = "nested",
        id_accessible: bool = False,
        language: str | None = None,
        debug_sql: bool = False,
    ) -> dict:
        """
        Retrieve items and totals for over-the-counter (OTC) transactions.

        OTC records include Quotes, Invoices, and Core Invoices.
        Use get_otc_listing_lists() to discover valid ID/name values.

        Args:
            ebis_main_type_ids: Filter by transaction type IDs or names (1=Quote, 2=Invoice, 3=CoreInvoice).
            back_order_is: Filter by back order status — "yes", "no", or "all".
            return_is: Filter by return status — "yes", "no", or "all".
            original_quote_number: Fragment search — find an invoice by its originating quote number.
            reminder_due_next_days: Return records with a reminder date within the next N days.
            filter_text: General text filter applied across the listing.
            include_parts: If True, include parts line items in the response.
            include_misc_charges: If True, include miscellaneous charges in the response.
            otc_id: Return a single OTC record by its eBis ID.
            city_ids: Filter by city IDs or names.
            status_ids: Filter by OTC status IDs or names.
            customer_ids: Filter by customer IDs or names.
            type_ids: Filter by OTC type IDs or names.
            department_ids: Filter by department IDs or names.
            show_mine_only: If True, return only records created by the authenticated user.
            accounting_invoice_num: Fragment search on accounting invoice number.
            buyer_contact: Fragment search on buyer contact name.
            buyer_purchase_order: Fragment search on buyer purchase order number.
            created_dates: Filter by creation date(s).
            display_dates: Filter by display date(s).
            est_ship_dates: Filter by estimated ship date(s).
            has_media: Filter by media presence — "yes", "no", or "all".
            has_misc_charges: Filter by misc charge presence — "yes", "no", or "all".
            misc_charge: Fragment search on miscellaneous charge description.
            notes: Fragment search on notes text.
            part_description: Fragment search on part description.
            part_number: Fragment search on part number.
            part_serial_no: Fragment search on part serial number.
            payment_due_dates: Filter by payment due date(s).
            processed_dates: Filter by processed date(s).
            shipped_dates: Filter by shipped date(s).
            tracking_number: Fragment search on shipping tracking number.
            rpt_sort: Sort order for the report output.
            hierarchy: Response structure — "nested" (default) or "flat".
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            language: Language for generic list parameter lookups (default: "English").
            debug_sql: Enable SQL debug output (dev/testing use).

        Returns:
            OTC listing records matching the requested filters.
        """
        body: dict[str, Any] = {}

        if ebis_main_type_ids is not None:
            body["EBisMainTypeID"] = ebis_main_type_ids
        if back_order_is is not None:
            body["BackOrderIs"] = back_order_is
        if return_is is not None:
            body["ReturnIs"] = return_is
        if original_quote_number is not None:
            body["OriginalQuoteNumber"] = original_quote_number
        if reminder_due_next_days is not None:
            body["ReminderDueNextDays"] = reminder_due_next_days
        if filter_text is not None:
            body["FilterText"] = filter_text
        if include_parts:
            body["IncludeParts"] = True
        if include_misc_charges:
            body["IncludeMiscCharges"] = True
        if otc_id is not None:
            body["OtcID"] = otc_id
        if city_ids is not None:
            body["CityID"] = city_ids
        if status_ids is not None:
            body["StatusID"] = status_ids
        if customer_ids is not None:
            body["CustomerID"] = customer_ids
        if type_ids is not None:
            body["TypeID"] = type_ids
        if department_ids is not None:
            body["DepartmentID"] = department_ids
        if show_mine_only:
            body["ShowMineOnly"] = True
        if accounting_invoice_num is not None:
            body["AccountingInvoiceNum"] = accounting_invoice_num
        if buyer_contact is not None:
            body["BuyerContact"] = buyer_contact
        if buyer_purchase_order is not None:
            body["BuyerPurchaseOrder"] = buyer_purchase_order
        if created_dates is not None:
            body["CreatedDate"] = created_dates
        if display_dates is not None:
            body["DisplayDate"] = display_dates
        if est_ship_dates is not None:
            body["EstShipDate"] = est_ship_dates
        if has_media is not None:
            body["HasMedia"] = has_media
        if has_misc_charges is not None:
            body["HasMiscCharges"] = has_misc_charges
        if misc_charge is not None:
            body["MiscCharge"] = misc_charge
        if notes is not None:
            body["Notes"] = notes
        if part_description is not None:
            body["PartDescription"] = part_description
        if part_number is not None:
            body["PartNumber"] = part_number
        if part_serial_no is not None:
            body["PartSerialNo"] = part_serial_no
        if payment_due_dates is not None:
            body["PaymentDueDate"] = payment_due_dates
        if processed_dates is not None:
            body["ProcessedDate"] = processed_dates
        if shipped_dates is not None:
            body["ShippedDate"] = shipped_dates
        if tracking_number is not None:
            body["TrackingNumber"] = tracking_number
        if rpt_sort is not None:
            body["RptSort"] = rpt_sort
        if hierarchy != "nested":
            body["Hierarchy"] = hierarchy
        if id_accessible:
            body["IDAccessible"] = True
        if language is not None:
            body["Language"] = language
        if debug_sql:
            body["DebugSql"] = True

        return self.post("otc/listing", body)
