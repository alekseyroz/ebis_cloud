"""Tests that WcClient correctly composes all 11 domain mixins."""

from __future__ import annotations

import inspect

from veryon_wc import WcClient
from veryon_wc._equipment import EquipmentMixin
from veryon_wc._http import HttpMixin
from veryon_wc._inventory import InventoryMixin
from veryon_wc._meters import MetersMixin
from veryon_wc._otc import OtcMixin
from veryon_wc._parts import PartsMixin
from veryon_wc._pm import PmMixin
from veryon_wc._purchase_orders import PurchaseOrdersMixin
from veryon_wc._service_requests import ServiceRequestsMixin
from veryon_wc._users import UsersMixin
from veryon_wc._vendors import VendorsMixin
from veryon_wc._workorders import WorkordersMixin

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
    client = WcClient("https://host.test/api", "alice", "s3cret")
    assert client._base_url == "https://host.test/api"
    assert client._username == "alice"
    assert client._password == "s3cret"


def test_client_inherits_from_http_mixin_and_all_11_domain_mixins():
    for mixin in [HttpMixin, *DOMAIN_MIXINS]:
        assert issubclass(WcClient, mixin), f"WcClient must inherit {mixin.__name__}"
    assert len(DOMAIN_MIXINS) == 11


def test_client_exposes_every_method_from_every_domain_mixin_as_callable():
    client = WcClient("https://host.test/api", "alice", "s3cret")

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
