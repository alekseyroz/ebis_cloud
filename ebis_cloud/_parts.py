"""Master part listing API methods."""

from typing import Any


class PartsMixin:
    def get_masterpart_listing_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying the master part list.

        Available list names: PartComponentID, PartTypeID, SupplierID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("masterpart/listing/lists", params=params)

    def get_masterpart_listing(
        self,
        core_is: str | None = None,
        description_like: str | None = None,
        expiring_shelf_life: int | None = None,
        family_name: str | None = None,
        general_cost_range: list[int | float] | None = None,
        general_location_range: list[str] | None = None,
        has_alternate: str | None = None,
        has_general_cost: str | None = None,
        has_general_location: bool = False,
        has_media: str | None = None,
        has_superseded: str | None = None,
        has_unspsc: str | None = None,
        has_warranty_days: str | None = None,
        hazard_is: str | None = None,
        is_serial: str | None = None,
        line_code: str | None = None,
        no_inv_movement: bool = False,
        no_inv_movement_days: int | None = None,
        part_component_ids: list[int | str] | None = None,
        part_number_like: str | None = None,
        part_number_range: list[str] | None = None,
        part_type_ids: list[int | str] | None = None,
        specific_location_range: list[str] | None = None,
        supplier_ids: list[int | str] | None = None,
        unspsc: str | None = None,
        id_accessible: bool = False,
    ) -> dict:
        """
        Retrieve general master part list information.

        Use get_masterpart_listing_lists() to discover valid ID/name values.

        Args:
            core_is: Filter by core part status — "yes", "no", or "all".
            description_like: Fragment search on part description.
            expiring_shelf_life: Return parts whose shelf life expires within N days.
            family_name: Fragment search on part family name.
            general_cost_range: Filter by general cost range as [min, max].
            general_location_range: Filter by general location range as [start, end].
            has_alternate: Filter by alternate part presence — "yes", "no", or "all".
            has_general_cost: Filter by general cost presence — "yes", "no", or "all".
            has_general_location: If True, return only parts that have a general location.
            has_media: Filter by media attachment presence — "yes", "no", or "all".
            has_superseded: Filter by superseded part presence — "yes", "no", or "all".
            has_unspsc: Filter by UNSPSC code presence — "yes", "no", or "all".
            has_warranty_days: Filter by warranty days presence — "yes", "no", or "all".
            hazard_is: Filter by hazardous material status — "yes", "no", or "all".
            is_serial: Filter by serialised part status — "yes", "no", or "all".
            line_code: Fragment search on part line code.
            no_inv_movement: If True, return only parts with no inventory movement.
            no_inv_movement_days: Return parts with no inventory movement in the last N days.
            part_component_ids: Filter by part component IDs or names.
            part_number_like: Fragment search on part number.
            part_number_range: Filter by part number range as [start, end].
            part_type_ids: Filter by part type IDs or names.
            specific_location_range: Filter by specific location range as [start, end].
            supplier_ids: Filter by supplier IDs or names.
            unspsc: Search on UNSPSC code.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.

        Returns:
            Master part list records matching the requested filters.
        """
        body: dict[str, Any] = {}

        if core_is is not None:
            body["CoreIs"] = core_is
        if description_like is not None:
            body["DescriptionLike"] = description_like
        if expiring_shelf_life is not None:
            body["ExpiringShelfLife"] = expiring_shelf_life
        if family_name is not None:
            body["FamilyName"] = family_name
        if general_cost_range is not None:
            body["GeneralCostRange"] = general_cost_range
        if general_location_range is not None:
            body["GeneralLocationRange"] = general_location_range
        if has_alternate is not None:
            body["HasAlternate"] = has_alternate
        if has_general_cost is not None:
            body["HasGeneralCost"] = has_general_cost
        if has_general_location:
            body["HasGeneralLocation"] = True
        if has_media is not None:
            body["HasMedia"] = has_media
        if has_superseded is not None:
            body["HasSuperseded"] = has_superseded
        if has_unspsc is not None:
            body["HasUnspsc"] = has_unspsc
        if has_warranty_days is not None:
            body["HasWarrantyDays"] = has_warranty_days
        if hazard_is is not None:
            body["HazardIs"] = hazard_is
        if is_serial is not None:
            body["IsSerial"] = is_serial
        if line_code is not None:
            body["LineCode"] = line_code
        if no_inv_movement:
            body["NoInvMovement"] = True
        if no_inv_movement_days is not None:
            body["NoInvMovementDays"] = no_inv_movement_days
        if part_component_ids is not None:
            body["PartComponentID"] = part_component_ids
        if part_number_like is not None:
            body["PartNumberLike"] = part_number_like
        if part_number_range is not None:
            body["PartNumberRange"] = part_number_range
        if part_type_ids is not None:
            body["PartTypeID"] = part_type_ids
        if specific_location_range is not None:
            body["SpecificLocationRange"] = specific_location_range
        if supplier_ids is not None:
            body["SupplierID"] = supplier_ids
        if unspsc is not None:
            body["Unspsc"] = unspsc
        if id_accessible:
            body["IDAccessible"] = True

        return self.post("masterpart/listing", body)
