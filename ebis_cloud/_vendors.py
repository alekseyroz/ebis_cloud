"""Vendor API methods."""

from typing import Any


class VendorsMixin:
    def get_vendor_listing_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying vendors.

        Available list names: LimitToCityID, ShipMethodID, TermsID, VendorClassID.

        Args:
            list_names: Optional list of specific list names to return,
                        e.g. ["ShipMethodID", "VendorClassID"]. If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("vendor/listing/lists", params=params)

    def get_vendor_listing(
        self,
        include_inactive: bool = False,
        account: str | None = None,
        address: str | None = None,
        address2: str | None = None,
        approval_expiring: int | None = None,
        approved: int | str | None = None,
        cities: list[str] | None = None,
        city: str | None = None,
        contact: str | None = None,
        countries: list[str] | None = None,
        country: str | None = None,
        do_not_create_po: str | None = None,
        email: str | None = None,
        gl_account_number: str | None = None,
        has_media: bool = False,
        has_warranty_claims: str | None = None,
        inactive: str | None = None,
        is_osr: str | None = None,
        is_supplier: str | None = None,
        is_tools: str | None = None,
        limit_to_city_id: int | str | None = None,
        phone: str | None = None,
        ship_method_ids: list[int | str] | None = None,
        state: str | None = None,
        states: list[str] | None = None,
        terms_ids: list[int | str] | None = None,
        url: str | None = None,
        vendor_class_ids: list[int | str] | None = None,
        vendor_name: str | None = None,
        zip: str | None = None,
        zips: list[str] | None = None,
        id_accessible: bool = False,
    ) -> dict:
        """
        Retrieve a comprehensive list of vendors.

        Use get_vendor_listing_lists() to discover valid ID/name values for
        any of the ID filter parameters.

        Args:
            include_inactive: If True, include inactive vendors in the results.
            account: Fragment search on vendor account number.
            address: Fragment search on address line 1.
            address2: Fragment search on address line 2.
            approval_expiring: Return vendors whose approval expires within N days.
            approved: Filter by approval status ID or name.
            cities: Filter by multiple exact city names, e.g. ["Dallas", "Charlotte"].
            city: Fragment search on vendor city.
            contact: Fragment search on vendor contact name.
            countries: Filter by multiple exact country names.
            country: Fragment search on vendor country.
            do_not_create_po: Filter by PO restriction — "yes", "no", or "all".
            email: Fragment search on vendor email address.
            gl_account_number: Fragment search on GL account number.
            has_media: If True, return only vendors with media attachments.
            has_warranty_claims: Filter by warranty claim presence — "yes", "no", or "all".
            inactive: Filter by inactive status — "yes", "no", or "all".
            is_osr: Filter by outside repair vendor status — "yes", "no", or "all".
            is_supplier: Filter by supplier status — "yes", "no", or "all".
            is_tools: Filter by tools vendor status — "yes", "no", or "all".
            limit_to_city_id: Limit results to vendors accessible to this city ID or name.
            phone: Fragment search on vendor phone number.
            ship_method_ids: Filter by shipping method IDs or names.
            state: Fragment search on vendor state.
            states: Filter by multiple exact state values.
            terms_ids: Filter by payment terms IDs or names.
            url: Fragment search on vendor website URL.
            vendor_class_ids: Filter by vendor class IDs or names.
            vendor_name: Fragment search on vendor name.
            zip: Fragment search on vendor ZIP/postal code.
            zips: Filter by multiple exact ZIP/postal codes.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.

        Returns:
            Vendor records matching the requested filters.
        """
        body: dict[str, Any] = {}

        if include_inactive:
            body["IncludeInactive"] = True
        if account is not None:
            body["Account"] = account
        if address is not None:
            body["Address"] = address
        if address2 is not None:
            body["Address2"] = address2
        if approval_expiring is not None:
            body["ApprovalExpiring"] = approval_expiring
        if approved is not None:
            body["Approved"] = approved
        if cities is not None:
            body["Cities"] = cities
        if city is not None:
            body["City"] = city
        if contact is not None:
            body["Contact"] = contact
        if countries is not None:
            body["Countries"] = countries
        if country is not None:
            body["Country"] = country
        if do_not_create_po is not None:
            body["DoNotCreatePO"] = do_not_create_po
        if email is not None:
            body["Email"] = email
        if gl_account_number is not None:
            body["GLAccountNumber"] = gl_account_number
        if has_media:
            body["HasMedia"] = True
        if has_warranty_claims is not None:
            body["HasWarrantyClaims"] = has_warranty_claims
        if inactive is not None:
            body["Inactive"] = inactive
        if is_osr is not None:
            body["IsOsr"] = is_osr
        if is_supplier is not None:
            body["IsSupplier"] = is_supplier
        if is_tools is not None:
            body["IsTools"] = is_tools
        if limit_to_city_id is not None:
            body["LimitToCityID"] = limit_to_city_id
        if phone is not None:
            body["Phone"] = phone
        if ship_method_ids is not None:
            body["ShipMethodID"] = ship_method_ids
        if state is not None:
            body["State"] = state
        if states is not None:
            body["States"] = states
        if terms_ids is not None:
            body["TermsID"] = terms_ids
        if url is not None:
            body["Url"] = url
        if vendor_class_ids is not None:
            body["VendorClassID"] = vendor_class_ids
        if vendor_name is not None:
            body["VendorName"] = vendor_name
        if zip is not None:
            body["Zip"] = zip
        if zips is not None:
            body["Zips"] = zips
        if id_accessible:
            body["IDAccessible"] = True

        return self.post("vendor/listing", body)

    def get_vendor_addupdate_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when adding or updating vendors.

        Available list names: Phone1TypeID, Phone2TypeID, Phone3TypeID, Phone4TypeID,
        TermsID, VendorClassID, CurrencyID, ShipMethodID, ApproveTypeID, WarrantyMakeID,
        LimitToCityID, TaxID.

        Args:
            list_names: Optional list of specific list names to return,
                        e.g. ["TermsID", "ShipMethodID"]. If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("vendor/addupdate/lists", params=params)

    def add_update_vendors(
        self,
        # Batch mode
        vendor_batch: list[dict] | None = None,
        # Single-record mode
        mode: str | None = None,
        id: int | None = None,
        vendor_name: str | None = None,
        user_validate_temp_token: str | None = None,
        change_to_name: str | None = None,
        # Contact / address
        contact: str | None = None,
        address: str | None = None,
        address2: str | None = None,
        city: str | None = None,
        state: str | None = None,
        zip: str | None = None,
        country: str | None = None,
        country_use: bool | None = None,
        # Shipping address
        ship_address: str | None = None,
        ship_address2: str | None = None,
        ship_city: str | None = None,
        ship_state: str | None = None,
        ship_zip: str | None = None,
        ship_country: str | None = None,
        ship_country_use: bool | None = None,
        # Phone numbers
        phone1: str | None = None,
        phone2: str | None = None,
        phone3: str | None = None,
        phone4: str | None = None,
        phone1_type_id: int | None = None,
        phone2_type_id: int | None = None,
        phone3_type_id: int | None = None,
        phone4_type_id: int | None = None,
        # Online / account
        email: str | None = None,
        url: str | None = None,
        account: str | None = None,
        customer_code: str | None = None,
        notes: str | None = None,
        gl_account_number: str | None = None,
        supplier_site_name: str | None = None,
        # Classifications
        terms_id: int | None = None,
        vendor_class_id: int | None = None,
        currency_id: int | None = None,
        ship_method_id: int | None = None,
        tax_id: str | None = None,
        is_supplier: bool | None = None,
        is_osr: bool | None = None,
        is_tools: bool | None = None,
        do_not_create_po: bool | None = None,
        limit_to_city_id: int | None = None,
        # Approval / warranty
        approve_type_id: int | None = None,
        approve_expires: str | None = None,
        has_warranty_claims: bool | None = None,
        has_contract_pricing: bool | None = None,
        warranty_make_id: int | None = None,
        # Output
        id_accessible: bool = False,
        language: str | None = None,
    ) -> dict:
        """
        Add or update one or more vendors in eBis Cloud.

        Supports two calling modes:
        - **Batch mode**: Pass a list of vendor dicts via `vendor_batch`. Each dict must
          include `Mode` and the relevant fields. `LineNumber` is returned in the response.
        - **Single-record mode**: Pass `mode` and individual field parameters directly.

        Mode values:
        - **Insert**: Create a new vendor. Requires `vendor_name`.
        - **Update**: Update general fields. Matches on `id`; `vendor_name` used as fallback.
        - **Delete**: Delete a vendor. Returns a confirmation token (`UserValidateTempToken`).
          Resubmit with the token to confirm.
        - **Inactivate**: Inactivate a vendor. Also returns a confirmation token.
        - **Activate**: Activate a vendor.
        - **ChangeName**: Rename a vendor. Requires `change_to_name`.

        Use get_vendor_addupdate_lists() to find valid IDs for any ID parameter.

        Args:
            vendor_batch: List of vendor dicts for batch mode.
            mode: Operation mode — Insert, Update, Delete, Inactivate, Activate, ChangeName.
            id: Vendor ID — primary lookup key for Update/Delete/Inactivate/Activate/ChangeName.
            vendor_name: Vendor name. Required for Insert; fallback lookup for other modes.
            user_validate_temp_token: Confirmation token returned from a Delete/Inactivate
                                       request. Resubmit with this token to confirm the action.
            change_to_name: New vendor name for ChangeName mode.
            contact: Vendor contact name.
            address: Address line 1.
            address2: Address line 2.
            city: Vendor city.
            state: Vendor state.
            zip: Vendor ZIP/postal code.
            country: Vendor country.
            country_use: If True, use the country field in address formatting.
            ship_address: Shipping address line 1.
            ship_address2: Shipping address line 2.
            ship_city: Shipping city.
            ship_state: Shipping state.
            ship_zip: Shipping ZIP/postal code.
            ship_country: Shipping country.
            ship_country_use: If True, use the shipping country field.
            phone1: Primary phone number.
            phone2: Secondary phone number.
            phone3: Tertiary phone number.
            phone4: Quaternary phone number.
            phone1_type_id: Type ID for phone1.
            phone2_type_id: Type ID for phone2.
            phone3_type_id: Type ID for phone3.
            phone4_type_id: Type ID for phone4.
            email: Vendor email address.
            url: Vendor website URL.
            account: Vendor account number.
            customer_code: Customer code at the vendor.
            notes: Vendor notes.
            gl_account_number: GL account number.
            supplier_site_name: Supplier site name.
            terms_id: Payment terms ID.
            vendor_class_id: Vendor class ID.
            currency_id: Currency ID.
            ship_method_id: Shipping method ID.
            tax_id: Tax ID string.
            is_supplier: If True, mark as a parts supplier.
            is_osr: If True, mark as an outside repair vendor.
            is_tools: If True, mark as a tools vendor.
            do_not_create_po: If True, prevent PO creation for this vendor.
            limit_to_city_id: Limit this vendor to a specific city ID.
            approve_type_id: Approval type ID.
            approve_expires: Approval expiry date, e.g. "2025-12-31".
            has_warranty_claims: If True, vendor has warranty claims.
            has_contract_pricing: If True, vendor has contract pricing.
            warranty_make_id: Make ID associated with vendor warranty.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.
            language: Language for generic list parameter lookups (default: "English").

        Returns:
            Per-vendor results with LineNumber, MessageID, MessageText, ID, and Action.
            For Delete/Inactivate, an unconfirmed response includes a UserValidateTempToken.
        """
        if vendor_batch is not None:
            return self.post("vendor/addupdate", {"VendorBatch": vendor_batch})

        body: dict[str, Any] = {}

        if mode is not None:
            body["Mode"] = mode
        if id is not None:
            body["ID"] = id
        if vendor_name is not None:
            body["VendorName"] = vendor_name
        if user_validate_temp_token is not None:
            body["UserValidateTempToken"] = user_validate_temp_token
        if change_to_name is not None:
            body["ChangeToName"] = change_to_name
        if contact is not None:
            body["Contact"] = contact
        if address is not None:
            body["Address"] = address
        if address2 is not None:
            body["Address2"] = address2
        if city is not None:
            body["City"] = city
        if state is not None:
            body["State"] = state
        if zip is not None:
            body["Zip"] = zip
        if country is not None:
            body["Country"] = country
        if country_use is not None:
            body["CountryUse"] = country_use
        if ship_address is not None:
            body["ShipAddress"] = ship_address
        if ship_address2 is not None:
            body["ShipAddress2"] = ship_address2
        if ship_city is not None:
            body["ShipCity"] = ship_city
        if ship_state is not None:
            body["ShipState"] = ship_state
        if ship_zip is not None:
            body["ShipZip"] = ship_zip
        if ship_country is not None:
            body["ShipCountry"] = ship_country
        if ship_country_use is not None:
            body["ShipCountryUse"] = ship_country_use
        if phone1 is not None:
            body["Phone1"] = phone1
        if phone2 is not None:
            body["Phone2"] = phone2
        if phone3 is not None:
            body["Phone3"] = phone3
        if phone4 is not None:
            body["Phone4"] = phone4
        if phone1_type_id is not None:
            body["Phone1TypeID"] = phone1_type_id
        if phone2_type_id is not None:
            body["Phone2TypeID"] = phone2_type_id
        if phone3_type_id is not None:
            body["Phone3TypeID"] = phone3_type_id
        if phone4_type_id is not None:
            body["Phone4TypeID"] = phone4_type_id
        if email is not None:
            body["Email"] = email
        if url is not None:
            body["Url"] = url
        if account is not None:
            body["Account"] = account
        if customer_code is not None:
            body["CustomerCode"] = customer_code
        if notes is not None:
            body["Notes"] = notes
        if gl_account_number is not None:
            body["GLAccountNumber"] = gl_account_number
        if supplier_site_name is not None:
            body["SupplierSiteName"] = supplier_site_name
        if terms_id is not None:
            body["TermsID"] = terms_id
        if vendor_class_id is not None:
            body["VendorClassID"] = vendor_class_id
        if currency_id is not None:
            body["CurrencyID"] = currency_id
        if ship_method_id is not None:
            body["ShipMethodID"] = ship_method_id
        if tax_id is not None:
            body["TaxID"] = tax_id
        if is_supplier is not None:
            body["IsSupplier"] = is_supplier
        if is_osr is not None:
            body["IsOsr"] = is_osr
        if is_tools is not None:
            body["IsTools"] = is_tools
        if do_not_create_po is not None:
            body["DoNotCreatePO"] = do_not_create_po
        if limit_to_city_id is not None:
            body["LimitToCityID"] = limit_to_city_id
        if approve_type_id is not None:
            body["ApproveTypeID"] = approve_type_id
        if approve_expires is not None:
            body["ApproveExpires"] = approve_expires
        if has_warranty_claims is not None:
            body["HasWarrantyClaims"] = has_warranty_claims
        if has_contract_pricing is not None:
            body["HasContractPricing"] = has_contract_pricing
        if warranty_make_id is not None:
            body["WarrantyMakeID"] = warranty_make_id
        if id_accessible:
            body["IDAccessible"] = True
        if language is not None:
            body["Language"] = language

        return self.post("vendor/addupdate", body)
