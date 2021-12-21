# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen

import datetime
import enum
import typing

from ._abstract import _BaseType
from .common import ImportResource

if typing.TYPE_CHECKING:
    from .common import (
        ChannelKeyReference,
        CustomerGroupKeyReference,
        DiscountedPrice,
        PriceTier,
        ProductKeyReference,
        ProductVariantKeyReference,
        TypedMoney,
    )
    from .customfields import Custom

__all__ = ["PriceImport", "SubRate", "TaxRate"]


class SubRate(_BaseType):
    name: str
    amount: float

    def __init__(self, *, name: str, amount: float):
        self.name = name
        self.amount = amount
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "SubRate":
        from ._schemas.prices import SubRateSchema

        return SubRateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.prices import SubRateSchema

        return SubRateSchema().dump(self)


class TaxRate(_BaseType):
    id: typing.Optional[str]
    name: str
    amount: float
    included_in_price: bool
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: str
    state: typing.Optional[str]
    sub_rates: typing.Optional[typing.List["SubRate"]]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        name: str,
        amount: float,
        included_in_price: bool,
        country: str,
        state: typing.Optional[str] = None,
        sub_rates: typing.Optional[typing.List["SubRate"]] = None
    ):
        self.id = id
        self.name = name
        self.amount = amount
        self.included_in_price = included_in_price
        self.country = country
        self.state = state
        self.sub_rates = sub_rates
        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TaxRate":
        from ._schemas.prices import TaxRateSchema

        return TaxRateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.prices import TaxRateSchema

        return TaxRateSchema().dump(self)


class PriceImport(ImportResource):
    """The data representation for a Price to be imported that is persisted as a [Price](/../api/projects/products#price) in the Project."""

    #: Maps to `Price.value`. TypedMoney is what is called BaseMoney in the HTTP API.
    value: "TypedMoney"
    #: Maps to `Price.county`.
    country: typing.Optional[str]
    #: Maps to `Price.validFrom`.
    valid_from: typing.Optional[datetime.datetime]
    #: Maps to `Price.validUntil`.
    valid_until: typing.Optional[datetime.datetime]
    #: The Reference to the [CustomerGroup](/../api/projects/customerGroups#customergroup) with which the Price is associated.
    #: If referenced CustomerGroup does not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary CustomerGroup is created.
    customer_group: typing.Optional["CustomerGroupKeyReference"]
    #: The Reference to the [Channel](/../api/projects/channels#channel) with which the Price is associated.
    #: If referenced Channel does not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary Channel is created.
    channel: typing.Optional["ChannelKeyReference"]
    #: Sets a discounted price from an external service.
    discounted: typing.Optional["DiscountedPrice"]
    #: Only the Price updates will be published to `staged` and `current` projection.
    publish: typing.Optional[bool]
    #: The tiered prices for this price.
    tiers: typing.Optional[typing.List["PriceTier"]]
    #: The custom fields for this price.
    custom: typing.Optional["Custom"]
    #: The ProductVariant in which this Price is contained.
    #: The Reference to the [ProductVariant](/../api/projects/products#productvariant) with which the Price is associated.
    #: If referenced ProductVariant does not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary ProductVariant is created.
    product_variant: "ProductVariantKeyReference"
    #: The Product in which the Product Variant containing this Price is contained. Maps to `ProductVariant.product`.
    #: The Reference to the [Product](/../api/projects/products#product) with which the Price is associated.
    #: If referenced Product does not exist, the `state` of the [ImportOperation](/import-operation#importoperation) will be set to `unresolved` until the necessary Product is created.
    product: "ProductKeyReference"

    def __init__(
        self,
        *,
        key: str,
        value: "TypedMoney",
        country: typing.Optional[str] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None,
        customer_group: typing.Optional["CustomerGroupKeyReference"] = None,
        channel: typing.Optional["ChannelKeyReference"] = None,
        discounted: typing.Optional["DiscountedPrice"] = None,
        publish: typing.Optional[bool] = None,
        tiers: typing.Optional[typing.List["PriceTier"]] = None,
        custom: typing.Optional["Custom"] = None,
        product_variant: "ProductVariantKeyReference",
        product: "ProductKeyReference"
    ):
        self.value = value
        self.country = country
        self.valid_from = valid_from
        self.valid_until = valid_until
        self.customer_group = customer_group
        self.channel = channel
        self.discounted = discounted
        self.publish = publish
        self.tiers = tiers
        self.custom = custom
        self.product_variant = product_variant
        self.product = product
        super().__init__(key=key)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceImport":
        from ._schemas.prices import PriceImportSchema

        return PriceImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.prices import PriceImportSchema

        return PriceImportSchema().dump(self)
