"""User API methods."""

from typing import Any


class UsersMixin:
    def get_user_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when querying users.

        Available list names: TechGroupID, CityID, HomeCityID, PartInspectorCityID,
        PartInspectorStockRoomID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("user/lists", params=params)

    def get_users(
        self,
        show_inactive: bool = False,
        primary_city: str | None = None,
        has_access_city: str | None = None,
        home_city: str | None = None,
        profile_name: str | None = None,
        tech_group_ids: list[int | str] | None = None,
        mode: str | None = None,
        city_ids: list[int | str] | None = None,
        valid_emails: bool | None = None,
        home_city_ids: list[int | str] | None = None,
        filter_text: str | None = None,
        page_on: int | None = None,
        page_per: int | None = None,
        find: str | None = None,
        part_inspector: bool | None = None,
        part_inspector_city_ids: list[int | str] | None = None,
        part_inspector_stock_room_ids: list[int | str] | None = None,
        has_media: bool = False,
        id_accessible: bool = False,
    ) -> dict:
        """
        List users associated with this eBis tenant.

        Use get_user_lists() to discover valid ID/name values.

        Args:
            show_inactive: If True, include inactive users in the results.
            primary_city: Filter by primary city name/abbreviation.
            has_access_city: Filter to users who have access to this city name/abbreviation.
            home_city: Filter by home city name/abbreviation.
            profile_name: Filter by user profile name.
            tech_group_ids: Filter by technician group IDs or names.
            mode: Filter by user mode string.
            city_ids: Filter by city IDs or names.
            valid_emails: If True, return only users with valid email addresses.
            home_city_ids: Filter by home city IDs or names.
            filter_text: General text filter applied across the user listing.
            page_on: Page number for paginated results (1-based).
            page_per: Number of results per page.
            find: General search string across user fields.
            part_inspector: If True, return only users who are part inspectors.
            part_inspector_city_ids: Filter part inspector users by city IDs or names.
            part_inspector_stock_room_ids: Filter part inspector users by stock room IDs or names.
            has_media: If True, return only users who have media attached.
            id_accessible: If True, child lists are keyed by ID rather than returned as arrays.

        Returns:
            User records matching the requested filters.
        """
        body: dict[str, Any] = {}

        if show_inactive:
            body["ShowInactive"] = True
        if primary_city is not None:
            body["PrimaryCity"] = primary_city
        if has_access_city is not None:
            body["HasAccessCity"] = has_access_city
        if home_city is not None:
            body["HomeCity"] = home_city
        if profile_name is not None:
            body["ProfileName"] = profile_name
        if tech_group_ids is not None:
            body["TechGroupID"] = tech_group_ids
        if mode is not None:
            body["Mode"] = mode
        if city_ids is not None:
            body["CityID"] = city_ids
        if valid_emails is not None:
            body["ValidEmails"] = valid_emails
        if home_city_ids is not None:
            body["HomeCityID"] = home_city_ids
        if filter_text is not None:
            body["FilterText"] = filter_text
        if page_on is not None:
            body["PageOn"] = page_on
        if page_per is not None:
            body["PagePer"] = page_per
        if find is not None:
            body["Find"] = find
        if part_inspector is not None:
            body["PartInspector"] = part_inspector
        if part_inspector_city_ids is not None:
            body["PartInspectorCityID"] = part_inspector_city_ids
        if part_inspector_stock_room_ids is not None:
            body["PartInspectorStockRoomID"] = part_inspector_stock_room_ids
        if has_media:
            body["HasMedia"] = True
        if id_accessible:
            body["IDAccessible"] = True

        return self.post("user", body)

    def logout_users(
        self,
        user_batch: list[dict] | None = None,
        stop_active_timers: bool = False,
        session_logout: bool = False,
        logout_user_id: int | None = None,
        sso_id: str | None = None,
        username: str | None = None,
    ) -> dict:
        """
        Log one or more users out of eBis and optionally stop their active service timers.

        Supports batch mode (user_batch) or single-user mode (individual params).

        Args:
            user_batch: List of user logout dicts for batch mode.
            stop_active_timers: If True, stop all active service timers for the user.
            session_logout: If True, log the user out of their active eBis session.
            logout_user_id: eBis user ID of the user to log out.
            sso_id: SSO identifier of the user to log out.
            username: Username of the user to log out.

        Returns:
            Result of the logout operation, including per-user MessageID and MessageText.
        """
        if user_batch is not None:
            return self.post("user/logout", {"UserBatch": user_batch})

        body: dict[str, Any] = {}

        if stop_active_timers:
            body["StopActiveTimers"] = True
        if session_logout:
            body["SessionLogout"] = True
        if logout_user_id is not None:
            body["LogoutUserID"] = logout_user_id
        if sso_id is not None:
            body["SsoID"] = sso_id
        if username is not None:
            body["Username"] = username

        return self.post("user/logout", body)

    def get_user_addupdate_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when adding or updating users.

        Available list names: UserID, UserProfileID, TechGroupID, CityDefaultID, CityHomeID,
        StockRoomDefaultID, PaperSizeID, TimeZoneID, DstID, DateFormatID, TimeFormatID,
        NumberFormatID, CostAndRetailCurrencyID, BatchSetTechProfileID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("user/addupdate/lists", params=params)

    def add_update_users(
        self,
        user_batch: list[dict] | None = None,
        mode: str | None = None,
        user_id: int | None = None,
        username: str | None = None,
        password: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
        phone1: str | None = None,
        inspector_code: str | None = None,
        user_profile_id: int | None = None,
        tech_group_id: int | None = None,
        city_default_id: int | None = None,
        city_home_id: int | None = None,
        stock_room_default_id: int | None = None,
        is_contractor: bool | None = None,
        is_technician: bool | None = None,
        paper_size_id: int | None = None,
        time_zone_id: int | None = None,
        pdf_file_action_id: int | None = None,
        dst_id: int | None = None,
        ui_color_mode_id: int | None = None,
        date_format_id: int | None = None,
        time_format_id: int | None = None,
        number_format_id: int | None = None,
        limit_stock_room: bool | None = None,
        limit_work_center: bool | None = None,
        limit_fleet_make: bool | None = None,
        limit_city_admin: bool | None = None,
        limit_company: bool | None = None,
        limit_wo_item_signoff: bool | None = None,
        start_work_time_converted: str | None = None,
        end_work_time: int | None = None,
        end_work_time_converted: str | None = None,
        auto_end_timers_eod: bool | None = None,
        show_os_parts_counts: bool | None = None,
        show_sr_counts: bool | None = None,
        badge_count_type: int | None = None,
        cost: float | None = None,
        retail: float | None = None,
        cost_and_retail_currency_id: int | None = None,
        po_approval: bool | None = None,
        po_approval_amount: float | None = None,
        po_approval_always: bool | None = None,
        os_cities: str | None = None,
        general_account_is: bool | None = None,
        on_the_job_training_is: bool | None = None,
        time_clock_disable: bool | None = None,
        time_clock_log_in_when_sign_in: bool | None = None,
        city_time_clock_id: int | None = None,
        employee_id: str | None = None,
        regular_hrs_worked: float | None = None,
        time_clock_user_group_id: int | None = None,
        accept_click_thru: bool | None = None,
        batch_set_tech_profile_id: int | None = None,
        sso_id: str | None = None,
        set_retail_as_wo_rate: bool | None = None,
        account_type: int | None = None,
        new_password: str | None = None,
        old_password: str | None = None,
        new_inspector_code: str | None = None,
        old_inspector_code: str | None = None,
        tenant_url: str | None = None,
        token_extend_minutes: int | None = None,
        default_paging_max_size: bool | None = None,
        show_welcome_screen: bool | None = None,
        ignore_limit_ip_access: bool | None = None,
        subscription_last_alert: str | None = None,
    ) -> dict:
        """
        Add or update one or more users in eBis Cloud.

        Supports batch mode (user_batch) or single-record mode.

        Mode values: Insert, Update, ResetPassword, Inactivate, Activate, BatchSetTech.

        Use get_user_addupdate_lists() to find valid IDs for any ID parameter.

        Args:
            user_batch: List of user dicts for batch mode.
            mode: Operation mode.
            user_id: eBis user ID.
            username: Username. Required for Insert.
            password: Password. Required for Insert.
            first_name: First name. Required for Insert.
            last_name: Last name. Required for Insert.
            email: Email address.
            phone1: Phone number.
            inspector_code: Inspector code for the user.
            user_profile_id: User profile ID. Required for Insert.
            tech_group_id: Technician group ID.
            city_default_id: Default city ID. Required for Insert.
            city_home_id: Home city ID.
            stock_room_default_id: Default stock room ID.
            is_contractor: If True, mark user as a contractor.
            is_technician: If True, mark user as a technician.
            paper_size_id: Preferred paper size ID.
            time_zone_id: Time zone ID.
            pdf_file_action_id: PDF file action preference ID.
            dst_id: Daylight saving time rule ID.
            ui_color_mode_id: UI color mode preference ID.
            date_format_id: Date format preference ID.
            time_format_id: Time format preference ID.
            number_format_id: Number format preference ID.
            limit_stock_room: If True, limit user to their default stock room.
            limit_work_center: If True, limit user to their assigned work center.
            limit_fleet_make: If True, limit user by fleet make.
            limit_city_admin: If True, limit user to city admin scope.
            limit_company: If True, limit user by company.
            limit_wo_item_signoff: If True, limit work order item signoff.
            start_work_time_converted: Work day start time, e.g. "08:00".
            end_work_time: Work day end time as integer.
            end_work_time_converted: Work day end time, e.g. "17:00".
            auto_end_timers_eod: If True, automatically end timers at end of day.
            show_os_parts_counts: If True, show outside parts counts.
            show_sr_counts: If True, show service request counts.
            badge_count_type: Badge count display type.
            cost: User cost rate.
            retail: User retail rate.
            cost_and_retail_currency_id: Currency ID for cost and retail rates.
            po_approval: If True, user can approve purchase orders.
            po_approval_amount: Maximum PO amount the user can approve.
            po_approval_always: If True, user must always approve POs.
            os_cities: Outside cities string.
            general_account_is: If True, mark as a general account.
            on_the_job_training_is: If True, mark user as on-the-job training.
            time_clock_disable: If True, disable time clock for this user.
            time_clock_log_in_when_sign_in: If True, log time clock when signing in.
            city_time_clock_id: City time clock ID.
            employee_id: Employee ID string.
            regular_hrs_worked: Regular hours worked per period.
            time_clock_user_group_id: Time clock user group ID.
            accept_click_thru: If True, user has accepted click-through agreement.
            batch_set_tech_profile_id: Profile ID for BatchSetTech mode.
            sso_id: SSO identifier for the user.
            set_retail_as_wo_rate: If True, use retail rate as the work order rate.
            account_type: Account type integer.
            new_password: New password — required for ResetPassword mode.
            old_password: Old password — used for password change verification.
            new_inspector_code: New inspector code.
            old_inspector_code: Old inspector code.
            tenant_url: Tenant URL override.
            token_extend_minutes: Number of minutes to extend the session token.
            default_paging_max_size: If True, use maximum page size by default.
            show_welcome_screen: If True, show the welcome screen on login.
            ignore_limit_ip_access: If True, bypass IP access restrictions.
            subscription_last_alert: Last subscription alert datetime.

        Returns:
            Per-user results with UserID, LineNumber, MessageID, MessageText, Action, and ID.
        """
        if user_batch is not None:
            return self.post("user/addupdate", {"UserBatch": user_batch})

        body: dict[str, Any] = {}

        if mode is not None:
            body["Mode"] = mode
        if user_id is not None:
            body["UserID"] = user_id
        if username is not None:
            body["Username"] = username
        if password is not None:
            body["Password"] = password
        if first_name is not None:
            body["FirstName"] = first_name
        if last_name is not None:
            body["LastName"] = last_name
        if email is not None:
            body["Email"] = email
        if phone1 is not None:
            body["Phone1"] = phone1
        if inspector_code is not None:
            body["InspectorCode"] = inspector_code
        if user_profile_id is not None:
            body["UserProfileID"] = user_profile_id
        if tech_group_id is not None:
            body["TechGroupID"] = tech_group_id
        if city_default_id is not None:
            body["CityDefaultID"] = city_default_id
        if city_home_id is not None:
            body["CityHomeID"] = city_home_id
        if stock_room_default_id is not None:
            body["StockRoomDefaultID"] = stock_room_default_id
        if is_contractor is not None:
            body["IsContractor"] = is_contractor
        if is_technician is not None:
            body["IsTechnician"] = is_technician
        if paper_size_id is not None:
            body["PaperSizeID"] = paper_size_id
        if time_zone_id is not None:
            body["TimeZoneID"] = time_zone_id
        if pdf_file_action_id is not None:
            body["PdfFileActionID"] = pdf_file_action_id
        if dst_id is not None:
            body["DstID"] = dst_id
        if ui_color_mode_id is not None:
            body["UiColorModeID"] = ui_color_mode_id
        if date_format_id is not None:
            body["DateFormatID"] = date_format_id
        if time_format_id is not None:
            body["TimeFormatID"] = time_format_id
        if number_format_id is not None:
            body["NumberFormatID"] = number_format_id
        if limit_stock_room is not None:
            body["LimitStockRoom"] = limit_stock_room
        if limit_work_center is not None:
            body["LimitWorkCenter"] = limit_work_center
        if limit_fleet_make is not None:
            body["LimitFleetMake"] = limit_fleet_make
        if limit_city_admin is not None:
            body["LimitCityAdmin"] = limit_city_admin
        if limit_company is not None:
            body["LimitCompany"] = limit_company
        if limit_wo_item_signoff is not None:
            body["LimitWoItemSignoff"] = limit_wo_item_signoff
        if start_work_time_converted is not None:
            body["StartWorkTimeConverted"] = start_work_time_converted
        if end_work_time is not None:
            body["EndWorkTime"] = end_work_time
        if end_work_time_converted is not None:
            body["EndWorkTimeConverted"] = end_work_time_converted
        if auto_end_timers_eod is not None:
            body["AutoEndTimersEOD"] = auto_end_timers_eod
        if show_os_parts_counts is not None:
            body["ShowOsPartsCounts"] = show_os_parts_counts
        if show_sr_counts is not None:
            body["ShowSrCounts"] = show_sr_counts
        if badge_count_type is not None:
            body["BadgeCountType"] = badge_count_type
        if cost is not None:
            body["Cost"] = cost
        if retail is not None:
            body["Retail"] = retail
        if cost_and_retail_currency_id is not None:
            body["CostAndRetailCurrencyID"] = cost_and_retail_currency_id
        if po_approval is not None:
            body["PoApproval"] = po_approval
        if po_approval_amount is not None:
            body["PoApprovalAmount"] = po_approval_amount
        if po_approval_always is not None:
            body["PoApprovalAlways"] = po_approval_always
        if os_cities is not None:
            body["OsCities"] = os_cities
        if general_account_is is not None:
            body["GeneralAccountIs"] = general_account_is
        if on_the_job_training_is is not None:
            body["OnTheJobTrainingIs"] = on_the_job_training_is
        if time_clock_disable is not None:
            body["TimeClockDisable"] = time_clock_disable
        if time_clock_log_in_when_sign_in is not None:
            body["TimeClockLogInWhenSignIn"] = time_clock_log_in_when_sign_in
        if city_time_clock_id is not None:
            body["CityTimeClockID"] = city_time_clock_id
        if employee_id is not None:
            body["EmployeeID"] = employee_id
        if regular_hrs_worked is not None:
            body["RegularHrsWorked"] = regular_hrs_worked
        if time_clock_user_group_id is not None:
            body["TimeClockUserGroupID"] = time_clock_user_group_id
        if accept_click_thru is not None:
            body["AcceptClickThru"] = accept_click_thru
        if batch_set_tech_profile_id is not None:
            body["BatchSetTechProfileID"] = batch_set_tech_profile_id
        if sso_id is not None:
            body["SsoID"] = sso_id
        if set_retail_as_wo_rate is not None:
            body["SetRetailAsWoRate"] = set_retail_as_wo_rate
        if account_type is not None:
            body["AccountType"] = account_type
        if new_password is not None:
            body["NewPassword"] = new_password
        if old_password is not None:
            body["OldPassword"] = old_password
        if new_inspector_code is not None:
            body["NewInspectorCode"] = new_inspector_code
        if old_inspector_code is not None:
            body["OldInspectorCode"] = old_inspector_code
        if tenant_url is not None:
            body["TenantUrl"] = tenant_url
        if token_extend_minutes is not None:
            body["TokenExtendMinutes"] = token_extend_minutes
        if default_paging_max_size is not None:
            body["DefaultPagingMaxSize"] = default_paging_max_size
        if show_welcome_screen is not None:
            body["ShowWelcomeScreen"] = show_welcome_screen
        if ignore_limit_ip_access is not None:
            body["IgnoreLimitIpAccess"] = ignore_limit_ip_access
        if subscription_last_alert is not None:
            body["SubscriptionLastAlert"] = subscription_last_alert

        return self.post("user/addupdate", body)

    def get_user_cities_admin_lists(self, list_names: list[str] | None = None) -> dict:
        """
        Retrieve the supporting reference lists used when editing user city access.

        Available list names: UserID, AddToUsersWithProfileID, CityID, IbsID, RegionID.

        Args:
            list_names: Optional list of specific list names to return.
                        If omitted, all lists are returned.

        Returns:
            Dict of requested reference lists, each containing {ID, Name} entries.
        """
        params = {}
        if list_names:
            params["name"] = ",".join(list_names)
        return self.get("user/cities/admin/lists", params=params)

    def edit_user_cities(
        self,
        mode: str,
        user_batch: list[dict] | None = None,
        user_id: int | str | None = None,
        all_cities: bool | None = None,
        add_to_all_users: bool | None = None,
        add_to_users_with_profile_id: int | str | None = None,
        email: str | None = None,
        city_ids: list[int | str] | None = None,
        ibs_ids: list[int | str] | None = None,
        region_ids: list[int | str] | None = None,
    ) -> dict:
        """
        Edit city, IBS, and region access for one or more users.

        Supports batch mode (user_batch) or single-operation mode.
        Mode values: Insert (grant access), Delete (remove access).

        Use get_user_cities_admin_lists() to discover valid IDs.

        Args:
            mode: (Required) "Insert" to grant access, "Delete" to remove access.
            user_batch: List of per-user operation dicts for batch mode.
            user_id: Target user by eBis ID or username.
            all_cities: If True, apply the operation to all cities, IBS, and regions.
            add_to_all_users: If True (Insert only), add the specified cities to all users.
            add_to_users_with_profile_id: Add cities to all users with this UserProfile ID or name.
            email: Target user by email address.
            city_ids: City IDs or names to insert/delete access for.
            ibs_ids: IBS IDs or names to insert/delete access for.
            region_ids: Region IDs or names to insert/delete access for.

        Returns:
            Per-user/operation results with MessageID and MessageText.
        """
        if user_batch is not None:
            return self.post("user/cities/admin", {"Mode": mode, "UserBatch": user_batch})

        body: dict[str, Any] = {
            "Mode": mode,
        }

        if user_id is not None:
            body["UserID"] = user_id
        if all_cities is not None:
            body["AllCities"] = all_cities
        if add_to_all_users is not None:
            body["AddToAllUsers"] = add_to_all_users
        if add_to_users_with_profile_id is not None:
            body["AddToUsersWithProfileID"] = add_to_users_with_profile_id
        if email is not None:
            body["Email"] = email
        if city_ids is not None:
            body["CityID"] = city_ids
        if ibs_ids is not None:
            body["IbsID"] = ibs_ids
        if region_ids is not None:
            body["RegionID"] = region_ids

        return self.post("user/cities/admin", body)
