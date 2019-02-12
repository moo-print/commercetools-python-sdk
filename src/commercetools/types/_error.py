# DO NOT EDIT! This file is automatically generated

import datetime
import typing

import attr

if typing.TYPE_CHECKING:
    from ._common import Price, ReferenceTypeId
    from ._product import Attribute
__all__ = [
    "AccessDeniedError",
    "ConcurrentModificationError",
    "DiscountCodeNonApplicableError",
    "DuplicateAttributeValueError",
    "DuplicateAttributeValuesError",
    "DuplicateFieldError",
    "DuplicatePriceScopeError",
    "DuplicateVariantValuesError",
    "ErrorObject",
    "ErrorResponse",
    "InsufficientScopeError",
    "InvalidCredentialsError",
    "InvalidCurrentPasswordError",
    "InvalidFieldError",
    "InvalidInputError",
    "InvalidItemShippingDetailsError",
    "InvalidJsonInputError",
    "InvalidOperationError",
    "InvalidSubjectError",
    "InvalidTokenError",
    "MissingTaxRateForCountryError",
    "NoMatchingProductDiscountFoundError",
    "OutOfStockError",
    "PriceChangedError",
    "ReferenceExistsError",
    "RequiredFieldError",
    "ResourceNotFoundError",
    "ShippingMethodDoesNotMatchCartError",
    "VariantValues",
]


@attr.s(auto_attribs=True, init=False, repr=False)
class ErrorObject:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ErrorObjectSchema`."
    #: :class:`str`
    code: typing.Optional[str]
    #: :class:`str`
    message: typing.Optional[str]

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        self.code = code
        self.message = message

    def __repr__(self) -> str:
        return "ErrorObject(code=%r, message=%r)" % (self.code, self.message)


@attr.s(auto_attribs=True, init=False, repr=False)
class ErrorResponse:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ErrorResponseSchema`."
    #: :class:`int` `(Named` ``statusCode`` `in Commercetools)`
    status_code: typing.Optional[int]
    #: :class:`str`
    message: typing.Optional[str]
    #: Optional :class:`str`
    error: typing.Optional[str]
    #: Optional :class:`str`
    error_description: typing.Optional[str]
    #: Optional :class:`list`
    errors: typing.Optional[list]

    def __init__(
        self,
        *,
        status_code: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        errors: typing.Optional[list] = None
    ) -> None:
        self.status_code = status_code
        self.message = message
        self.error = error
        self.error_description = error_description
        self.errors = errors

    def __repr__(self) -> str:
        return (
            "ErrorResponse(status_code=%r, message=%r, error=%r, error_description=%r, errors=%r)"
            % (
                self.status_code,
                self.message,
                self.error,
                self.error_description,
                self.errors,
            )
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class VariantValues:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.VariantValuesSchema`."
    #: Optional :class:`str`
    sku: typing.Optional[str]
    #: List of :class:`commercetools.types.Price`
    prices: typing.Optional[typing.List["Price"]]
    #: List of :class:`commercetools.types.Attribute`
    attributes: typing.Optional[typing.List["Attribute"]]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        prices: typing.Optional[typing.List["Price"]] = None,
        attributes: typing.Optional[typing.List["Attribute"]] = None
    ) -> None:
        self.sku = sku
        self.prices = prices
        self.attributes = attributes

    def __repr__(self) -> str:
        return "VariantValues(sku=%r, prices=%r, attributes=%r)" % (
            self.sku,
            self.prices,
            self.attributes,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class AccessDeniedError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.AccessDeniedErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="access_denied", message=message)

    def __repr__(self) -> str:
        return "AccessDeniedError(code=%r, message=%r)" % (self.code, self.message)


@attr.s(auto_attribs=True, init=False, repr=False)
class ConcurrentModificationError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ConcurrentModificationErrorSchema`."
    #: Optional :class:`int` `(Named` ``currentVersion`` `in Commercetools)`
    current_version: typing.Optional[int]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        current_version: typing.Optional[int] = None
    ) -> None:
        self.current_version = current_version
        super().__init__(code="ConcurrentModification", message=message)

    def __repr__(self) -> str:
        return (
            "ConcurrentModificationError(code=%r, message=%r, current_version=%r)"
            % (self.code, self.message, self.current_version)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeNonApplicableError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeNonApplicableErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="DiscountCodeNonApplicable", message=message)

    def __repr__(self) -> str:
        return "DiscountCodeNonApplicableError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DuplicateAttributeValueError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DuplicateAttributeValueErrorSchema`."
    #: :class:`commercetools.types.Attribute`
    attribute: typing.Optional["Attribute"]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        attribute: typing.Optional["Attribute"] = None
    ) -> None:
        self.attribute = attribute
        super().__init__(code="DuplicateAttributeValue", message=message)

    def __repr__(self) -> str:
        return "DuplicateAttributeValueError(code=%r, message=%r, attribute=%r)" % (
            self.code,
            self.message,
            self.attribute,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DuplicateAttributeValuesError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DuplicateAttributeValuesErrorSchema`."
    #: List of :class:`commercetools.types.Attribute`
    attributes: typing.Optional[typing.List["Attribute"]]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        attributes: typing.Optional[typing.List["Attribute"]] = None
    ) -> None:
        self.attributes = attributes
        super().__init__(code="DuplicateAttributeValues", message=message)

    def __repr__(self) -> str:
        return "DuplicateAttributeValuesError(code=%r, message=%r, attributes=%r)" % (
            self.code,
            self.message,
            self.attributes,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DuplicateFieldError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DuplicateFieldErrorSchema`."
    #: Optional :class:`str`
    field: typing.Optional[str]
    #: Optional :class:`typing.Any` `(Named` ``duplicateValue`` `in Commercetools)`
    duplicate_value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        field: typing.Optional[str] = None,
        duplicate_value: typing.Optional[typing.Any] = None
    ) -> None:
        self.field = field
        self.duplicate_value = duplicate_value
        super().__init__(code="DuplicateField", message=message)

    def __repr__(self) -> str:
        return (
            "DuplicateFieldError(code=%r, message=%r, field=%r, duplicate_value=%r)"
            % (self.code, self.message, self.field, self.duplicate_value)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DuplicatePriceScopeError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DuplicatePriceScopeErrorSchema`."
    #: List of :class:`commercetools.types.Price` `(Named` ``conflictingPrices`` `in Commercetools)`
    conflicting_prices: typing.Optional[typing.List["Price"]]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        conflicting_prices: typing.Optional[typing.List["Price"]] = None
    ) -> None:
        self.conflicting_prices = conflicting_prices
        super().__init__(code="DuplicatePriceScope", message=message)

    def __repr__(self) -> str:
        return (
            "DuplicatePriceScopeError(code=%r, message=%r, conflicting_prices=%r)"
            % (self.code, self.message, self.conflicting_prices)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DuplicateVariantValuesError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DuplicateVariantValuesErrorSchema`."
    #: :class:`commercetools.types.VariantValues` `(Named` ``variantValues`` `in Commercetools)`
    variant_values: typing.Optional["VariantValues"]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        variant_values: typing.Optional["VariantValues"] = None
    ) -> None:
        self.variant_values = variant_values
        super().__init__(code="DuplicateVariantValues", message=message)

    def __repr__(self) -> str:
        return "DuplicateVariantValuesError(code=%r, message=%r, variant_values=%r)" % (
            self.code,
            self.message,
            self.variant_values,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class InsufficientScopeError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InsufficientScopeErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="insufficient_scope", message=message)

    def __repr__(self) -> str:
        return "InsufficientScopeError(code=%r, message=%r)" % (self.code, self.message)


@attr.s(auto_attribs=True, init=False, repr=False)
class InvalidCredentialsError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InvalidCredentialsErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="InvalidCredentials", message=message)

    def __repr__(self) -> str:
        return "InvalidCredentialsError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class InvalidCurrentPasswordError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InvalidCurrentPasswordErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="InvalidCurrentPassword", message=message)

    def __repr__(self) -> str:
        return "InvalidCurrentPasswordError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class InvalidFieldError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InvalidFieldErrorSchema`."
    #: :class:`str`
    field: typing.Optional[str]
    #: :class:`typing.Any` `(Named` ``invalidValue`` `in Commercetools)`
    invalid_value: typing.Optional[typing.Any]
    #: Optional :class:`list` `(Named` ``allowedValues`` `in Commercetools)`
    allowed_values: typing.Optional[list]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        field: typing.Optional[str] = None,
        invalid_value: typing.Optional[typing.Any] = None,
        allowed_values: typing.Optional[list] = None
    ) -> None:
        self.field = field
        self.invalid_value = invalid_value
        self.allowed_values = allowed_values
        super().__init__(code="InvalidField", message=message)

    def __repr__(self) -> str:
        return (
            "InvalidFieldError(code=%r, message=%r, field=%r, invalid_value=%r, allowed_values=%r)"
            % (
                self.code,
                self.message,
                self.field,
                self.invalid_value,
                self.allowed_values,
            )
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class InvalidInputError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InvalidInputErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="InvalidInput", message=message)

    def __repr__(self) -> str:
        return "InvalidInputError(code=%r, message=%r)" % (self.code, self.message)


@attr.s(auto_attribs=True, init=False, repr=False)
class InvalidItemShippingDetailsError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InvalidItemShippingDetailsErrorSchema`."
    #: :class:`str`
    subject: typing.Optional[str]
    #: :class:`str` `(Named` ``itemId`` `in Commercetools)`
    item_id: typing.Optional[str]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        item_id: typing.Optional[str] = None
    ) -> None:
        self.subject = subject
        self.item_id = item_id
        super().__init__(code="InvalidItemShippingDetails", message=message)

    def __repr__(self) -> str:
        return (
            "InvalidItemShippingDetailsError(code=%r, message=%r, subject=%r, item_id=%r)"
            % (self.code, self.message, self.subject, self.item_id)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class InvalidJsonInputError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InvalidJsonInputErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="InvalidJsonInput", message=message)

    def __repr__(self) -> str:
        return "InvalidJsonInputError(code=%r, message=%r)" % (self.code, self.message)


@attr.s(auto_attribs=True, init=False, repr=False)
class InvalidOperationError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InvalidOperationErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="InvalidOperation", message=message)

    def __repr__(self) -> str:
        return "InvalidOperationError(code=%r, message=%r)" % (self.code, self.message)


@attr.s(auto_attribs=True, init=False, repr=False)
class InvalidSubjectError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InvalidSubjectErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="InvalidSubject", message=message)

    def __repr__(self) -> str:
        return "InvalidSubjectError(code=%r, message=%r)" % (self.code, self.message)


@attr.s(auto_attribs=True, init=False, repr=False)
class InvalidTokenError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InvalidTokenErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="invalid_token", message=message)

    def __repr__(self) -> str:
        return "InvalidTokenError(code=%r, message=%r)" % (self.code, self.message)


@attr.s(auto_attribs=True, init=False, repr=False)
class MissingTaxRateForCountryError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.MissingTaxRateForCountryErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="MissingTaxRateForCountry", message=message)

    def __repr__(self) -> str:
        return "MissingTaxRateForCountryError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class NoMatchingProductDiscountFoundError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.NoMatchingProductDiscountFoundErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="NoMatchingProductDiscountFound", message=message)

    def __repr__(self) -> str:
        return "NoMatchingProductDiscountFoundError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class OutOfStockError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.OutOfStockErrorSchema`."
    #: List of :class:`str` `(Named` ``lineItems`` `in Commercetools)`
    line_items: typing.Optional[typing.List[str]]
    #: List of :class:`str`
    skus: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        line_items: typing.Optional[typing.List[str]] = None,
        skus: typing.Optional[typing.List[str]] = None
    ) -> None:
        self.line_items = line_items
        self.skus = skus
        super().__init__(code="OutOfStock", message=message)

    def __repr__(self) -> str:
        return "OutOfStockError(code=%r, message=%r, line_items=%r, skus=%r)" % (
            self.code,
            self.message,
            self.line_items,
            self.skus,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class PriceChangedError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PriceChangedErrorSchema`."
    #: List of :class:`str` `(Named` ``lineItems`` `in Commercetools)`
    line_items: typing.Optional[typing.List[str]]
    #: :class:`bool`
    shipping: typing.Optional[bool]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        line_items: typing.Optional[typing.List[str]] = None,
        shipping: typing.Optional[bool] = None
    ) -> None:
        self.line_items = line_items
        self.shipping = shipping
        super().__init__(code="PriceChanged", message=message)

    def __repr__(self) -> str:
        return "PriceChangedError(code=%r, message=%r, line_items=%r, shipping=%r)" % (
            self.code,
            self.message,
            self.line_items,
            self.shipping,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class ReferenceExistsError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ReferenceExistsErrorSchema`."
    #: Optional :class:`commercetools.types.ReferenceTypeId` `(Named` ``referencedBy`` `in Commercetools)`
    referenced_by: typing.Optional["ReferenceTypeId"]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        referenced_by: typing.Optional["ReferenceTypeId"] = None
    ) -> None:
        self.referenced_by = referenced_by
        super().__init__(code="ReferenceExists", message=message)

    def __repr__(self) -> str:
        return "ReferenceExistsError(code=%r, message=%r, referenced_by=%r)" % (
            self.code,
            self.message,
            self.referenced_by,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class RequiredFieldError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.RequiredFieldErrorSchema`."
    #: :class:`str`
    field: typing.Optional[str]

    def __init__(
        self,
        *,
        code: typing.Optional[str] = None,
        message: typing.Optional[str] = None,
        field: typing.Optional[str] = None
    ) -> None:
        self.field = field
        super().__init__(code="RequiredField", message=message)

    def __repr__(self) -> str:
        return "RequiredFieldError(code=%r, message=%r, field=%r)" % (
            self.code,
            self.message,
            self.field,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class ResourceNotFoundError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ResourceNotFoundErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="ResourceNotFound", message=message)

    def __repr__(self) -> str:
        return "ResourceNotFoundError(code=%r, message=%r)" % (self.code, self.message)


@attr.s(auto_attribs=True, init=False, repr=False)
class ShippingMethodDoesNotMatchCartError(ErrorObject):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ShippingMethodDoesNotMatchCartErrorSchema`."

    def __init__(
        self, *, code: typing.Optional[str] = None, message: typing.Optional[str] = None
    ) -> None:
        super().__init__(code="ShippingMethodDoesNotMatchCart", message=message)

    def __repr__(self) -> str:
        return "ShippingMethodDoesNotMatchCartError(code=%r, message=%r)" % (
            self.code,
            self.message,
        )