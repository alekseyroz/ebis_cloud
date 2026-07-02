"""Tests that EbisClient correctly composes all 11 domain mixins."""

from __future__ import annotations

import inspect

from ebis_cloud import EbisClient
from ebis_cloud._equipment import EquipmentMixin
from ebis_cloud._http import HttpMixin
from ebis_cloud._inventory import InventoryMixin
from ebis_cloud._meters import MetersMixin
from ebis_cloud._otc import OtcMixin
from ebis_cloud._parts import PartsMixin
from ebis_cloud._pm import PmMixin
from ebis_cloud._purchase_orders import PurchaseOrdersMixin
from ebis_cloud._service_requests import ServiceRequestsMixin
from ebis_cloud._users import UsersMixin
from ebis_cloud._vendors import VendorsMixin
from ebis_cloud._workorders import WorkordersMixin

DOMAIN_MIXINS = [
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
]


def _public_methods(cls) -> set[str]:
    return {
        name
        for name, value in vars(cls).items()
        if inspect.isfunction(value) and not name.startswith("_")
    }


def test_client_constructor_sets_base_url_username_password():
    client = EbisClient("https://host.test/api", "alice", "s3cret")
    assert client._base_url == "https://host.test/api"
    assert client._username == "alice"
    assert client._password == "s3cret"


def test_client_inherits_from_http_mixin_and_all_11_domain_mixins():
    for mixin in [HttpMixin, *DOMAIN_MIXINS]:
        assert issubclass(EbisClient, mixin), f"EbisClient must inherit {mixin.__name__}"
    assert len(DOMAIN_MIXINS) == 11


def test_client_exposes_every_method_from_every_domain_mixin_as_callable():
    client = EbisClient("https://host.test/api", "alice", "s3cret")

    expected_methods: set[str] = set()
    for mixin in DOMAIN_MIXINS:
        expected_methods |= _public_methods(mixin)

    for method_name in expected_methods:
        assert hasattr(client, method_name), f"missing method {method_name}"
        assert callable(getattr(client, method_name)), f"{method_name} is not callable"


def test_total_method_count_across_domain_mixins():
    expected_methods: set[str] = set()
    per_mixin_counts = {}
    for mixin in DOMAIN_MIXINS:
        methods = _public_methods(mixin)
        per_mixin_counts[mixin.__name__] = len(methods)
        expected_methods |= methods

    # Sanity check: no accidental name collisions across mixins (would silently
    # shadow a method and reduce the total).
    assert sum(per_mixin_counts.values()) == len(expected_methods), (
        "duplicate method names across mixins detected: "
        f"{per_mixin_counts}"
    )

    # The domain mixins currently define 54 public API methods in total.
    assert len(expected_methods) == 54


def test_no_method_name_collisions_between_http_mixin_and_domain_mixins():
    http_methods = _public_methods(HttpMixin)
    domain_methods: set[str] = set()
    for mixin in DOMAIN_MIXINS:
        domain_methods |= _public_methods(mixin)

    assert http_methods.isdisjoint(domain_methods)
