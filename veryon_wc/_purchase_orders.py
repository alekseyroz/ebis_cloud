"""Purchase order API methods."""

from typing import Any


class PurchaseOrdersMixin:
    def get_purchase_order_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying purchase orders.

        Available list names: CityID, IbsID, RegionID, StatusID, VendorID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("purchaseorder/lists", params=params)

    def export_purchase_orders(
        self,
        city_ids: list[int | str] | None = None,
        completed_dates: list[str] | None = None,
        created_by_user: str | None = None,
        ibs_ids: list[int | str] | None = None,
        include_item_destination_detail: bool = False,
        include_item_detail: bool = False,
        include_receiving_info: bool = False,
        inspect_dates: list[str] | None = None,
        ordered_dates: list[str] | None = None,
        part_number: str | None = None,
        received_dates: list[str] | None = None,
        region_ids: list[int | str] | None = None,
        rma_number: str | None = None,
        status_ids: list[int | str] | None = None,
        vendor_ids: list[int | str] | None = None,
        hierarchy: str = "flat",
        id_accessible: bool = False,
    ) -> dict:
        """
        Export purchase order listings including parts and destinations.

        Use get_purchase_order_lists() to discover valid ID/name values.

        Args:
            city_ids: Filter by city IDs or names.
            completed_dates: Filter by PO completion date(s).
            created_by_user: Fragment search on the username that created the PO.
            ibs_ids: Filter by IBS IDs or names.
            include_item_destination_detail: If True, include destination detail for each PO item.
            include_item_detail: If True, include line item detail for each PO.
            include_receiving_info: If True, include receiving information for each PO.
            inspect_dates: Filter by inspection date(s).
            ordered_dates: Filter by order date(s).
            part_number: Fragment search on part number.
            received_dates: Filter by received date(s).
            region_ids: Filter by region IDs or names.
            rma_number: Fragment search on RMA number.
            status_ids: Filter by PO status IDs or names.
            vendor_ids: Filter by vendor IDs or names.
            hierarchy: Response structure — "flat" (default) or "nested".
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.

        Returns:
            Purchase order records matching the requested filters.
        """
        body: dict[str, Any] = {}

        if city_ids is not None:
            body["CityID"] = city_ids
        if completed_dates is not None:
            body["CompletedDate"] = completed_dates
        if created_by_user is not None:
            body["CreatedByUser"] = created_by_user
        if ibs_ids is not None:
            body["IbsID"] = ibs_ids
        if include_item_destination_detail:
            body["IncludeItemDestinationDetail"] = True
        if include_item_detail:
            body["IncludeItemDetail"] = True
        if include_receiving_info:
            body["IncludeReceivingInfo"] = True
        if inspect_dates is not None:
            body["InspectDate"] = inspect_dates
        if ordered_dates is not None:
            body["OrderedDate"] = ordered_dates
        if part_number is not None:
            body["PartNumber"] = part_number
        if received_dates is not None:
            body["ReceivedDate"] = received_dates
        if region_ids is not None:
            body["RegionID"] = region_ids
        if rma_number is not None:
            body["RmaNumber"] = rma_number
        if status_ids is not None:
            body["StatusID"] = status_ids
        if vendor_ids is not None:
            body["VendorID"] = vendor_ids
        if hierarchy != "flat":
            body["Hierarchy"] = hierarchy
        if id_accessible:
            body["IDAccessible"] = True

        return self.post("purchaseorder", body)
