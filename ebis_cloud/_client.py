"""EbisClient — the main entry point for the ebis_cloud library."""

from ._http import HttpMixin
from ._workorders import WorkordersMixin
from ._equipment import EquipmentMixin
from ._meters import MetersMixin
from ._pm import PmMixin
from ._parts import PartsMixin
from ._inventory import InventoryMixin
from ._purchase_orders import PurchaseOrdersMixin
from ._service_requests import ServiceRequestsMixin
from ._otc import OtcMixin
from ._users import UsersMixin
from ._vendors import VendorsMixin


class EbisClient(
    HttpMixin,
    WorkordersMixin,
    EquipmentMixin,
    MetersMixin,
    PmMixin,
    PartsMixin,
    InventoryMixin,
    PurchaseOrdersMixin,
    ServiceRequestsMixin,
    OtcMixin,
    UsersMixin,
    VendorsMixin,
):
    """Client for the eBis Cloud REST API."""

    def __init__(self, base_url: str, username: str, password: str) -> None:
        self._base_url = base_url.rstrip("/")
        self._username = username
        self._password = password
