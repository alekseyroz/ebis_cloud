"""Stock quantity API methods."""

from typing import Any


class InventoryMixin:
    def get_stock_quantity_detail_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying stock quantity detail.

        Available list names: PartComponentID, PartTypeID, StockRoomID, SupplierID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("masterpart/quantity/detail/lists", params=params)

    def get_stock_quantity_detail(
        self,
        core_is: str | None = None,
        description_like: str | None = None,
        family_name: str | None = None,
        general_location_range: list[str] | None = None,
        has_alternate: str | None = None,
        has_media: str | None = None,
        has_superseded: str | None = None,
        has_warranty_days: str | None = None,
        hazard_is: str | None = None,
        is_serial: str | None = None,
        line_code: str | None = None,
        part_component_ids: list[int | str] | None = None,
        part_number_like: str | None = None,
        part_number_range: list[str] | None = None,
        part_type_ids: list[int | str] | None = None,
        qty_customer: int | None = None,
        qty_location_range: list[str] | None = None,
        qty_po_number: str | None = None,
        qty_serial: str | None = None,
        qty_vendor: str | None = None,
        shelf_life_expires_days: int | None = None,
        stock_qty: int | None = None,
        stock_room_ids: list[int | str] | None = None,
        supplier_ids: list[int | str] | None = None,
        id_accessible: bool = False,
    ) -> dict:
        """
        Retrieve basic part information and detailed stock quantity data.

        Use get_stock_quantity_detail_lists() to discover valid ID/name values.

        Args:
            core_is: Filter by core part status — "yes", "no", or "all".
            description_like: Fragment search on part description.
            family_name: Fragment search on part family name.
            general_location_range: Filter by general location range as [start, end].
            has_alternate: Filter by alternate part presence — "yes", "no", or "all".
            has_media: Filter by media attachment presence — "yes", "no", or "all".
            has_superseded: Filter by superseded part presence — "yes", "no", or "all".
            has_warranty_days: Filter by warranty days presence — "yes", "no", or "all".
            hazard_is: Filter by hazardous material status — "yes", "no", or "all".
            is_serial: Filter by serialised part status — "yes", "no", or "all".
            line_code: Fragment search on part line code.
            part_component_ids: Filter by part component IDs or names.
            part_number_like: Fragment search on part number.
            part_number_range: Filter by part number range as [start, end].
            part_type_ids: Filter by part type IDs or names.
            qty_customer: Filter by stock quantity customer ID.
            qty_location_range: Filter stock rows by location range as [start, end].
            qty_po_number: Fragment search on the PO number associated with stock quantity rows.
            qty_serial: Fragment search on serial number within stock quantity rows.
            qty_vendor: Fragment search on vendor within stock quantity rows.
            shelf_life_expires_days: Return parts whose shelf life expires within N days.
            stock_qty: Filter by a specific stock quantity value.
            stock_room_ids: Filter by stock room IDs or names.
            supplier_ids: Filter by supplier IDs or names.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.

        Returns:
            Stock quantity detail records matching the requested filters.
        """
        body: dict[str, Any] = {}

        if core_is is not None:
            body["CoreIs"] = core_is
        if description_like is not None:
            body["DescriptionLike"] = description_like
        if family_name is not None:
            body["FamilyName"] = family_name
        if general_location_range is not None:
            body["GeneralLocationRange"] = general_location_range
        if has_alternate is not None:
            body["HasAlternate"] = has_alternate
        if has_media is not None:
            body["HasMedia"] = has_media
        if has_superseded is not None:
            body["HasSuperseded"] = has_superseded
        if has_warranty_days is not None:
            body["HasWarrantyDays"] = has_warranty_days
        if hazard_is is not None:
            body["HazardIs"] = hazard_is
        if is_serial is not None:
            body["IsSerial"] = is_serial
        if line_code is not None:
            body["LineCode"] = line_code
        if part_component_ids is not None:
            body["PartComponentID"] = part_component_ids
        if part_number_like is not None:
            body["PartNumberLike"] = part_number_like
        if part_number_range is not None:
            body["PartNumberRange"] = part_number_range
        if part_type_ids is not None:
            body["PartTypeID"] = part_type_ids
        if qty_customer is not None:
            body["QtyCustomer"] = qty_customer
        if qty_location_range is not None:
            body["QtyLocationRange"] = qty_location_range
        if qty_po_number is not None:
            body["QtyPoNumber"] = qty_po_number
        if qty_serial is not None:
            body["QtySerial"] = qty_serial
        if qty_vendor is not None:
            body["QtyVendor"] = qty_vendor
        if shelf_life_expires_days is not None:
            body["ShelfLifeExpiresDays"] = shelf_life_expires_days
        if stock_qty is not None:
            body["StockQty"] = stock_qty
        if stock_room_ids is not None:
            body["StockRoomID"] = stock_room_ids
        if supplier_ids is not None:
            body["SupplierID"] = supplier_ids
        if id_accessible:
            body["IDAccessible"] = True

        return self.post("masterpart/quantity/detail", body)

    def get_stock_quantity_log_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying the stock quantity log.

        Available list names: StockRoomID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("masterpart/quantity/log/lists", params=params)

    def get_stock_quantity_log(
        self,
        dates: list[str],
        description_like: str | None = None,
        part_number_like: str | None = None,
        stock_room_ids: list[int | str] | None = None,
        user: str | None = None,
        id_accessible: bool = False,
        debug_sql: bool = False,
    ) -> dict:
        """
        Retrieve detailed information about inventory quantity and cost changes.

        Use get_stock_quantity_log_lists() to discover valid StockRoomID values.

        Args:
            dates: (Required) Date range to retrieve log entries within,
                   e.g. ["2024-01-01", "2024-01-31"].
            description_like: Fragment search on part description.
            part_number_like: Fragment search on part number.
            stock_room_ids: Filter by stock room IDs or names.
            user: Fragment search on the username that made the inventory change.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            debug_sql: Enable SQL debug output (dev/testing use).

        Returns:
            Stock quantity log records showing inventory quantity and cost changes.
        """
        body: dict[str, Any] = {
            "Date": dates,
        }

        if description_like is not None:
            body["DescriptionLike"] = description_like
        if part_number_like is not None:
            body["PartNumberLike"] = part_number_like
        if stock_room_ids is not None:
            body["StockRoomID"] = stock_room_ids
        if user is not None:
            body["User"] = user
        if id_accessible:
            body["IDAccessible"] = True
        if debug_sql:
            body["DebugSql"] = True

        return self.post("masterpart/quantity/log", body)
