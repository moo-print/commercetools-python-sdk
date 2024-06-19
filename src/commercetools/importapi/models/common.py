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

if typing.TYPE_CHECKING:
    from .customfields import Custom

__all__ = [
    "Address",
    "Asset",
    "AssetDimensions",
    "AssetSource",
    "CartDiscountKeyReference",
    "CartKeyReference",
    "CategoryKeyReference",
    "ChannelKeyReference",
    "CustomObjectKeyReference",
    "CustomerGroupKeyReference",
    "CustomerKeyReference",
    "DiscountCodeKeyReference",
    "DiscountedPrice",
    "EnumValue",
    "HighPrecisionMoney",
    "Image",
    "ImportResource",
    "ImportResourceType",
    "KeyReference",
    "LocalizedEnumValue",
    "LocalizedString",
    "Money",
    "MoneyType",
    "OrderKeyReference",
    "PaymentKeyReference",
    "PriceKeyReference",
    "PriceTier",
    "ProcessingState",
    "ProductDiscountKeyReference",
    "ProductKeyReference",
    "ProductPriceModeEnum",
    "ProductTypeKeyReference",
    "ProductVariantKeyReference",
    "ReferenceType",
    "ShippingMethodKeyReference",
    "StateKeyReference",
    "StoreKeyReference",
    "TaxCategoryKeyReference",
    "TypeKeyReference",
    "TypedMoney",
    "UnresolvedReferences",
]


class Asset(_BaseType):
    #: User-defined identifier for the asset.
    #: Asset keys are unique inside their container (a product variant or a category).
    key: str
    sources: typing.List["AssetSource"]
    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    name: "LocalizedString"
    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    description: typing.Optional["LocalizedString"]
    tags: typing.Optional[typing.List["str"]]
    #: The representation to be sent to the server when creating a resource with custom fields.
    custom: typing.Optional["Custom"]

    def __init__(
        self,
        *,
        key: str,
        sources: typing.List["AssetSource"],
        name: "LocalizedString",
        description: typing.Optional["LocalizedString"] = None,
        tags: typing.Optional[typing.List["str"]] = None,
        custom: typing.Optional["Custom"] = None
    ):
        self.key = key
        self.sources = sources
        self.name = name
        self.description = description
        self.tags = tags
        self.custom = custom

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Asset":
        from ._schemas.common import AssetSchema

        return AssetSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AssetSchema

        return AssetSchema().dump(self)


class AssetDimensions(_BaseType):
    """The width and height of the Asset Source."""

    #: The width of the asset source.
    w: int
    #: The height of the asset source.
    h: int

    def __init__(self, *, w: int, h: int):
        self.w = w
        self.h = h

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AssetDimensions":
        from ._schemas.common import AssetDimensionsSchema

        return AssetDimensionsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AssetDimensionsSchema

        return AssetDimensionsSchema().dump(self)


class AssetSource(_BaseType):
    """An AssetSource is a representation of an Asset in a specific format, for example, a video in a certain encoding or an image in a certain resolution."""

    uri: str
    key: typing.Optional[str]
    #: The width and height of the Asset Source.
    dimensions: typing.Optional["AssetDimensions"]
    content_type: typing.Optional[str]

    def __init__(
        self,
        *,
        uri: str,
        key: typing.Optional[str] = None,
        dimensions: typing.Optional["AssetDimensions"] = None,
        content_type: typing.Optional[str] = None
    ):
        self.uri = uri
        self.key = key
        self.dimensions = dimensions
        self.content_type = content_type

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AssetSource":
        from ._schemas.common import AssetSourceSchema

        return AssetSourceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AssetSourceSchema

        return AssetSourceSchema().dump(self)


class Image(_BaseType):
    """An Image uploaded to commercetools Composable Commerce is stored in a Content Delivery Network and it's available in several pre-defined sizes. If you already have an image stored on an external service, you can save the URL when creating a new product or adding a variant, or you can add it later."""

    #: URL of the image in its original size. The URL must be unique within a single variant. It can be used to obtain the image in different sizes.
    url: str
    #: Dimensions of the original image. This can be used by your application, for example, to determine whether the image is large enough to display a zoom view.
    dimensions: "AssetDimensions"
    #: Custom label that can be used, for example, as an image description.
    label: typing.Optional[str]

    def __init__(
        self,
        *,
        url: str,
        dimensions: "AssetDimensions",
        label: typing.Optional[str] = None
    ):
        self.url = url
        self.dimensions = dimensions
        self.label = label

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Image":
        from ._schemas.common import ImageSchema

        return ImageSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ImageSchema

        return ImageSchema().dump(self)


class EnumValue(_BaseType):
    key: str
    label: str

    def __init__(self, *, key: str, label: str):
        self.key = key
        self.label = label

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "EnumValue":
        from ._schemas.common import EnumValueSchema

        return EnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import EnumValueSchema

        return EnumValueSchema().dump(self)


class LocalizedEnumValue(_BaseType):
    key: str
    #: A localized string is a JSON object where the keys are of [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag), and the values the corresponding strings used for that language.
    #: ```json
    #: {
    #:   "de": "Hundefutter",
    #:   "en": "dog food"
    #: }
    #: ```
    label: "LocalizedString"

    def __init__(self, *, key: str, label: "LocalizedString"):
        self.key = key
        self.label = label

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "LocalizedEnumValue":
        from ._schemas.common import LocalizedEnumValueSchema

        return LocalizedEnumValueSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import LocalizedEnumValueSchema

        return LocalizedEnumValueSchema().dump(self)


class LocalizedString(typing.Dict[str, str]):
    pass


class ImportResource(_BaseType):
    """A representation of the resource to import.
    Import resources are similar to draft types, but they only support key references.
    In general, import resources are more granular then regular resources.
    They are optimized for incremental updates and therefore have a slightly different structure.

    """

    #: User-defined unique identifier.
    key: str

    def __init__(self, *, key: str):
        self.key = key

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ImportResource":
        from ._schemas.common import ImportResourceSchema

        return ImportResourceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ImportResourceSchema

        return ImportResourceSchema().dump(self)


class KeyReference(_BaseType):
    """References a resource by key."""

    key: str
    #: The type of the referenced resource.
    type_id: "ReferenceType"

    def __init__(self, *, key: str, type_id: "ReferenceType"):
        self.key = key
        self.type_id = type_id

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "KeyReference":
        if data["typeId"] == "cart":
            from ._schemas.common import CartKeyReferenceSchema

            return CartKeyReferenceSchema().load(data)
        if data["typeId"] == "cart-discount":
            from ._schemas.common import CartDiscountKeyReferenceSchema

            return CartDiscountKeyReferenceSchema().load(data)
        if data["typeId"] == "category":
            from ._schemas.common import CategoryKeyReferenceSchema

            return CategoryKeyReferenceSchema().load(data)
        if data["typeId"] == "channel":
            from ._schemas.common import ChannelKeyReferenceSchema

            return ChannelKeyReferenceSchema().load(data)
        if data["typeId"] == "customer":
            from ._schemas.common import CustomerKeyReferenceSchema

            return CustomerKeyReferenceSchema().load(data)
        if data["typeId"] == "customer-group":
            from ._schemas.common import CustomerGroupKeyReferenceSchema

            return CustomerGroupKeyReferenceSchema().load(data)
        if data["typeId"] == "discount-code":
            from ._schemas.common import DiscountCodeKeyReferenceSchema

            return DiscountCodeKeyReferenceSchema().load(data)
        if data["typeId"] == "order":
            from ._schemas.common import OrderKeyReferenceSchema

            return OrderKeyReferenceSchema().load(data)
        if data["typeId"] == "payment":
            from ._schemas.common import PaymentKeyReferenceSchema

            return PaymentKeyReferenceSchema().load(data)
        if data["typeId"] == "price":
            from ._schemas.common import PriceKeyReferenceSchema

            return PriceKeyReferenceSchema().load(data)
        if data["typeId"] == "product":
            from ._schemas.common import ProductKeyReferenceSchema

            return ProductKeyReferenceSchema().load(data)
        if data["typeId"] == "product-discount":
            from ._schemas.common import ProductDiscountKeyReferenceSchema

            return ProductDiscountKeyReferenceSchema().load(data)
        if data["typeId"] == "product-type":
            from ._schemas.common import ProductTypeKeyReferenceSchema

            return ProductTypeKeyReferenceSchema().load(data)
        if data["typeId"] == "product-variant":
            from ._schemas.common import ProductVariantKeyReferenceSchema

            return ProductVariantKeyReferenceSchema().load(data)
        if data["typeId"] == "shipping-method":
            from ._schemas.common import ShippingMethodKeyReferenceSchema

            return ShippingMethodKeyReferenceSchema().load(data)
        if data["typeId"] == "state":
            from ._schemas.common import StateKeyReferenceSchema

            return StateKeyReferenceSchema().load(data)
        if data["typeId"] == "store":
            from ._schemas.common import StoreKeyReferenceSchema

            return StoreKeyReferenceSchema().load(data)
        if data["typeId"] == "tax-category":
            from ._schemas.common import TaxCategoryKeyReferenceSchema

            return TaxCategoryKeyReferenceSchema().load(data)
        if data["typeId"] == "type":
            from ._schemas.common import TypeKeyReferenceSchema

            return TypeKeyReferenceSchema().load(data)
        if data["typeId"] == "key-value-document":
            from ._schemas.common import CustomObjectKeyReferenceSchema

            return CustomObjectKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import KeyReferenceSchema

        return KeyReferenceSchema().dump(self)


class CartKeyReference(KeyReference):
    """References a cart by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CART)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartKeyReference":
        from ._schemas.common import CartKeyReferenceSchema

        return CartKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CartKeyReferenceSchema

        return CartKeyReferenceSchema().dump(self)


class CartDiscountKeyReference(KeyReference):
    """References a cart discount by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CART_DISCOUNT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartDiscountKeyReference":
        from ._schemas.common import CartDiscountKeyReferenceSchema

        return CartDiscountKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CartDiscountKeyReferenceSchema

        return CartDiscountKeyReferenceSchema().dump(self)


class CategoryKeyReference(KeyReference):
    """References a category by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CATEGORY)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CategoryKeyReference":
        from ._schemas.common import CategoryKeyReferenceSchema

        return CategoryKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CategoryKeyReferenceSchema

        return CategoryKeyReferenceSchema().dump(self)


class ChannelKeyReference(KeyReference):
    """References a channel by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CHANNEL)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ChannelKeyReference":
        from ._schemas.common import ChannelKeyReferenceSchema

        return ChannelKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ChannelKeyReferenceSchema

        return ChannelKeyReferenceSchema().dump(self)


class CustomerKeyReference(KeyReference):
    """References a customer by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CUSTOMER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CustomerKeyReference":
        from ._schemas.common import CustomerKeyReferenceSchema

        return CustomerKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CustomerKeyReferenceSchema

        return CustomerKeyReferenceSchema().dump(self)


class CustomerGroupKeyReference(KeyReference):
    """References a customer group by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.CUSTOMER_GROUP)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomerGroupKeyReference":
        from ._schemas.common import CustomerGroupKeyReferenceSchema

        return CustomerGroupKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CustomerGroupKeyReferenceSchema

        return CustomerGroupKeyReferenceSchema().dump(self)


class DiscountCodeKeyReference(KeyReference):
    """References a discount code by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.DISCOUNT_CODE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DiscountCodeKeyReference":
        from ._schemas.common import DiscountCodeKeyReferenceSchema

        return DiscountCodeKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import DiscountCodeKeyReferenceSchema

        return DiscountCodeKeyReferenceSchema().dump(self)


class OrderKeyReference(KeyReference):
    """References an order by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.ORDER)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderKeyReference":
        from ._schemas.common import OrderKeyReferenceSchema

        return OrderKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import OrderKeyReferenceSchema

        return OrderKeyReferenceSchema().dump(self)


class PaymentKeyReference(KeyReference):
    """References a payment by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PAYMENT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PaymentKeyReference":
        from ._schemas.common import PaymentKeyReferenceSchema

        return PaymentKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PaymentKeyReferenceSchema

        return PaymentKeyReferenceSchema().dump(self)


class PriceKeyReference(KeyReference):
    """References a price by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRICE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceKeyReference":
        from ._schemas.common import PriceKeyReferenceSchema

        return PriceKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PriceKeyReferenceSchema

        return PriceKeyReferenceSchema().dump(self)


class ProductKeyReference(KeyReference):
    """References a product by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRODUCT)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductKeyReference":
        from ._schemas.common import ProductKeyReferenceSchema

        return ProductKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductKeyReferenceSchema

        return ProductKeyReferenceSchema().dump(self)


class ProductDiscountKeyReference(KeyReference):
    """References a product discount by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRODUCT_DISCOUNT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductDiscountKeyReference":
        from ._schemas.common import ProductDiscountKeyReferenceSchema

        return ProductDiscountKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductDiscountKeyReferenceSchema

        return ProductDiscountKeyReferenceSchema().dump(self)


class ProductTypeKeyReference(KeyReference):
    """References a product type by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRODUCT_TYPE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductTypeKeyReference":
        from ._schemas.common import ProductTypeKeyReferenceSchema

        return ProductTypeKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductTypeKeyReferenceSchema

        return ProductTypeKeyReferenceSchema().dump(self)


class ProductVariantKeyReference(KeyReference):
    """References a product variant by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.PRODUCT_VARIANT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductVariantKeyReference":
        from ._schemas.common import ProductVariantKeyReferenceSchema

        return ProductVariantKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ProductVariantKeyReferenceSchema

        return ProductVariantKeyReferenceSchema().dump(self)


class ShippingMethodKeyReference(KeyReference):
    """References a shipping method by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.SHIPPING_METHOD)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShippingMethodKeyReference":
        from ._schemas.common import ShippingMethodKeyReferenceSchema

        return ShippingMethodKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import ShippingMethodKeyReferenceSchema

        return ShippingMethodKeyReferenceSchema().dump(self)


class StateKeyReference(KeyReference):
    """References a state by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.STATE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateKeyReference":
        from ._schemas.common import StateKeyReferenceSchema

        return StateKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import StateKeyReferenceSchema

        return StateKeyReferenceSchema().dump(self)


class StoreKeyReference(KeyReference):
    """References a store by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.STORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StoreKeyReference":
        from ._schemas.common import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import StoreKeyReferenceSchema

        return StoreKeyReferenceSchema().dump(self)


class TaxCategoryKeyReference(KeyReference):
    """References a tax category by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.TAX_CATEGORY)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "TaxCategoryKeyReference":
        from ._schemas.common import TaxCategoryKeyReferenceSchema

        return TaxCategoryKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import TaxCategoryKeyReferenceSchema

        return TaxCategoryKeyReferenceSchema().dump(self)


class TypeKeyReference(KeyReference):
    """References a type by key."""

    def __init__(self, *, key: str):

        super().__init__(key=key, type_id=ReferenceType.TYPE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypeKeyReference":
        from ._schemas.common import TypeKeyReferenceSchema

        return TypeKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import TypeKeyReferenceSchema

        return TypeKeyReferenceSchema().dump(self)


class CustomObjectKeyReference(KeyReference):
    """References a key value document by key."""

    container: str

    def __init__(self, *, key: str, container: str):
        self.container = container

        super().__init__(key=key, type_id=ReferenceType.KEY_VALUE_DOCUMENT)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CustomObjectKeyReference":
        from ._schemas.common import CustomObjectKeyReferenceSchema

        return CustomObjectKeyReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import CustomObjectKeyReferenceSchema

        return CustomObjectKeyReferenceSchema().dump(self)


class UnresolvedReferences(_BaseType):
    key: str
    #: The type of the referenced resource.
    type_id: "ReferenceType"

    def __init__(self, *, key: str, type_id: "ReferenceType"):
        self.key = key
        self.type_id = type_id

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "UnresolvedReferences":
        from ._schemas.common import UnresolvedReferencesSchema

        return UnresolvedReferencesSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import UnresolvedReferencesSchema

        return UnresolvedReferencesSchema().dump(self)


class MoneyType(enum.Enum):
    CENT_PRECISION = "centPrecision"
    HIGH_PRECISION = "highPrecision"


class TypedMoney(_BaseType):
    type: "MoneyType"
    fraction_digits: typing.Optional[int]
    cent_amount: int
    #: The currency code compliant to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).
    currency_code: str

    def __init__(
        self,
        *,
        type: "MoneyType",
        fraction_digits: typing.Optional[int] = None,
        cent_amount: int,
        currency_code: str
    ):
        self.type = type
        self.fraction_digits = fraction_digits
        self.cent_amount = cent_amount
        self.currency_code = currency_code

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "TypedMoney":
        if data["type"] == "highPrecision":
            from ._schemas.common import HighPrecisionMoneySchema

            return HighPrecisionMoneySchema().load(data)
        if data["type"] == "centPrecision":
            from ._schemas.common import MoneySchema

            return MoneySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import TypedMoneySchema

        return TypedMoneySchema().dump(self)


class HighPrecisionMoney(TypedMoney):
    precise_amount: int

    def __init__(
        self,
        *,
        fraction_digits: typing.Optional[int] = None,
        cent_amount: int,
        currency_code: str,
        precise_amount: int
    ):
        self.precise_amount = precise_amount

        super().__init__(
            fraction_digits=fraction_digits,
            cent_amount=cent_amount,
            currency_code=currency_code,
            type=MoneyType.HIGH_PRECISION,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "HighPrecisionMoney":
        from ._schemas.common import HighPrecisionMoneySchema

        return HighPrecisionMoneySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import HighPrecisionMoneySchema

        return HighPrecisionMoneySchema().dump(self)


class Money(TypedMoney):

    def __init__(
        self,
        *,
        fraction_digits: typing.Optional[int] = None,
        cent_amount: int,
        currency_code: str
    ):

        super().__init__(
            fraction_digits=fraction_digits,
            cent_amount=cent_amount,
            currency_code=currency_code,
            type=MoneyType.CENT_PRECISION,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Money":
        from ._schemas.common import MoneySchema

        return MoneySchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import MoneySchema

        return MoneySchema().dump(self)


class DiscountedPrice(_BaseType):
    value: "TypedMoney"
    #: Reference to a ProductDiscount.
    discount: "ProductDiscountKeyReference"

    def __init__(self, *, value: "TypedMoney", discount: "ProductDiscountKeyReference"):
        self.value = value
        self.discount = discount

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DiscountedPrice":
        from ._schemas.common import DiscountedPriceSchema

        return DiscountedPriceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import DiscountedPriceSchema

        return DiscountedPriceSchema().dump(self)


class PriceTier(_BaseType):
    """A price tier is selected instead of the default price when a certain quantity of the ProductVariant is added to a cart and ordered."""

    #: The minimum quantity this price tier is valid for.
    minimum_quantity: int
    #: The currency of a price tier is always the same as the currency of the base Price.
    value: "TypedMoney"

    def __init__(self, *, minimum_quantity: int, value: "TypedMoney"):
        self.minimum_quantity = minimum_quantity
        self.value = value

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "PriceTier":
        from ._schemas.common import PriceTierSchema

        return PriceTierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import PriceTierSchema

        return PriceTierSchema().dump(self)


class ImportResourceType(enum.Enum):
    """The resource types that can be imported."""

    CATEGORY = "category"
    CUSTOMER = "customer"
    INVENTORY = "inventory"
    ORDER = "order"
    ORDER_PATCH = "order-patch"
    PRICE = "price"
    PRODUCT = "product"
    PRODUCT_DRAFT = "product-draft"
    PRODUCT_TYPE = "product-type"
    PRODUCT_VARIANT = "product-variant"
    PRODUCT_VARIANT_PATCH = "product-variant-patch"
    STANDALONE_PRICE = "standalone-price"
    TYPE = "type"
    DISCOUNT_CODE = "discount-code"


class ReferenceType(enum.Enum):
    """The type of the referenced resource."""

    CART = "cart"
    CART_DISCOUNT = "cart-discount"
    CATEGORY = "category"
    CHANNEL = "channel"
    CUSTOMER = "customer"
    CUSTOMER_GROUP = "customer-group"
    DISCOUNT_CODE = "discount-code"
    ORDER = "order"
    PAYMENT = "payment"
    PRICE = "price"
    PRODUCT = "product"
    PRODUCT_DISCOUNT = "product-discount"
    PRODUCT_TYPE = "product-type"
    PRODUCT_VARIANT = "product-variant"
    SHIPPING_METHOD = "shipping-method"
    STATE = "state"
    STORE = "store"
    TAX_CATEGORY = "tax-category"
    TYPE = "type"
    KEY_VALUE_DOCUMENT = "key-value-document"


class ProcessingState(enum.Enum):
    """Every [Import Operation](/import-operation) is assigned one of the following states."""

    PROCESSING = "processing"
    VALIDATION_FAILED = "validationFailed"
    UNRESOLVED = "unresolved"
    WAIT_FOR_MASTER_VARIANT = "waitForMasterVariant"
    IMPORTED = "imported"
    REJECTED = "rejected"
    CANCELED = "canceled"


class Address(_BaseType):
    id: typing.Optional[str]
    key: typing.Optional[str]
    title: typing.Optional[str]
    salutation: typing.Optional[str]
    first_name: typing.Optional[str]
    last_name: typing.Optional[str]
    street_name: typing.Optional[str]
    street_number: typing.Optional[str]
    additional_street_info: typing.Optional[str]
    postal_code: typing.Optional[str]
    city: typing.Optional[str]
    region: typing.Optional[str]
    state: typing.Optional[str]
    #: A two-digit country code as per [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    country: str
    company: typing.Optional[str]
    department: typing.Optional[str]
    building: typing.Optional[str]
    apartment: typing.Optional[str]
    p_o_box: typing.Optional[str]
    phone: typing.Optional[str]
    mobile: typing.Optional[str]
    email: typing.Optional[str]
    fax: typing.Optional[str]
    additional_address_info: typing.Optional[str]
    external_id: typing.Optional[str]
    #: Custom Fields defined for the Address. Custom Fields can only be applied to `shippingAddress`.
    custom: typing.Optional["Custom"]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        salutation: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        street_name: typing.Optional[str] = None,
        street_number: typing.Optional[str] = None,
        additional_street_info: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        country: str,
        company: typing.Optional[str] = None,
        department: typing.Optional[str] = None,
        building: typing.Optional[str] = None,
        apartment: typing.Optional[str] = None,
        p_o_box: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        mobile: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        fax: typing.Optional[str] = None,
        additional_address_info: typing.Optional[str] = None,
        external_id: typing.Optional[str] = None,
        custom: typing.Optional["Custom"] = None
    ):
        self.id = id
        self.key = key
        self.title = title
        self.salutation = salutation
        self.first_name = first_name
        self.last_name = last_name
        self.street_name = street_name
        self.street_number = street_number
        self.additional_street_info = additional_street_info
        self.postal_code = postal_code
        self.city = city
        self.region = region
        self.state = state
        self.country = country
        self.company = company
        self.department = department
        self.building = building
        self.apartment = apartment
        self.p_o_box = p_o_box
        self.phone = phone
        self.mobile = mobile
        self.email = email
        self.fax = fax
        self.additional_address_info = additional_address_info
        self.external_id = external_id
        self.custom = custom

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Address":
        from ._schemas.common import AddressSchema

        return AddressSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.common import AddressSchema

        return AddressSchema().dump(self)


class ProductPriceModeEnum(enum.Enum):
    EMBEDDED = "Embedded"
    STANDALONE = "Standalone"
