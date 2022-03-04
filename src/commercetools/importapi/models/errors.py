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
from .common import ProcessingState

if typing.TYPE_CHECKING:
    from .common import ProcessingState
    from .prices import PriceImport
    from .productvariants import Attribute

__all__ = [
    "AccessDeniedError",
    "ConcurrentModificationError",
    "ContentionError",
    "DuplicateAttributeValueError",
    "DuplicateAttributeValuesError",
    "DuplicateFieldError",
    "DuplicateVariantValuesError",
    "ErrorObject",
    "ErrorResponse",
    "GenericError",
    "InsufficientScopeError",
    "InvalidCredentialsError",
    "InvalidFieldError",
    "InvalidInput",
    "InvalidJsonInput",
    "InvalidOperation",
    "InvalidScopeError",
    "InvalidStateTransitionError",
    "InvalidTokenError",
    "RequiredFieldError",
    "ResourceCreationError",
    "ResourceDeletionError",
    "ResourceNotFoundError",
    "ResourceUpdateError",
    "VariantValues",
]


class ErrorResponse(_BaseType):
    """The response in case of an error."""

    #: The http status code of the response.
    status_code: int
    #: Describes the error.
    message: str
    #: This property is only used for OAuth2 errors.
    #: Contains the error code.
    error: typing.Optional[str]
    #: This property is only used for OAuth2 errors.
    #: Additional information to assist the client developer in
    #: understanding the error.
    error_description: typing.Optional[str]
    #: The errors that caused this error response.
    errors: typing.Optional[typing.List["ErrorObject"]]

    def __init__(
        self,
        *,
        status_code: int,
        message: str,
        error: typing.Optional[str] = None,
        error_description: typing.Optional[str] = None,
        errors: typing.Optional[typing.List["ErrorObject"]] = None
    ):
        self.status_code = status_code
        self.message = message
        self.error = error
        self.error_description = error_description
        self.errors = errors

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ErrorResponse":
        from ._schemas.errors import ErrorResponseSchema

        return ErrorResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ErrorResponseSchema

        return ErrorResponseSchema().dump(self)


class ErrorObject(_BaseType):
    code: str
    message: str

    def __init__(self, *, code: str, message: str):
        self.code = code
        self.message = message

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ErrorObject":
        if data["code"] == "access_denied":
            from ._schemas.errors import AccessDeniedErrorSchema

            return AccessDeniedErrorSchema().load(data)
        if data["code"] == "invalid_scope":
            from ._schemas.errors import InvalidScopeErrorSchema

            return InvalidScopeErrorSchema().load(data)
        if data["code"] == "InvalidOperation":
            from ._schemas.errors import InvalidOperationSchema

            return InvalidOperationSchema().load(data)
        if data["code"] == "DuplicateAttributeValue":
            from ._schemas.errors import DuplicateAttributeValueErrorSchema

            return DuplicateAttributeValueErrorSchema().load(data)
        if data["code"] == "DuplicateAttributeValues":
            from ._schemas.errors import DuplicateAttributeValuesErrorSchema

            return DuplicateAttributeValuesErrorSchema().load(data)
        if data["code"] == "DuplicateField":
            from ._schemas.errors import DuplicateFieldErrorSchema

            return DuplicateFieldErrorSchema().load(data)
        if data["code"] == "DuplicateVariantValues":
            from ._schemas.errors import DuplicateVariantValuesErrorSchema

            return DuplicateVariantValuesErrorSchema().load(data)
        if data["code"] == "insufficient_scope":
            from ._schemas.errors import InsufficientScopeErrorSchema

            return InsufficientScopeErrorSchema().load(data)
        if data["code"] == "InvalidCredentials":
            from ._schemas.errors import InvalidCredentialsErrorSchema

            return InvalidCredentialsErrorSchema().load(data)
        if data["code"] == "invalid_token":
            from ._schemas.errors import InvalidTokenErrorSchema

            return InvalidTokenErrorSchema().load(data)
        if data["code"] == "InvalidField":
            from ._schemas.errors import InvalidFieldErrorSchema

            return InvalidFieldErrorSchema().load(data)
        if data["code"] == "InvalidJsonInput":
            from ._schemas.errors import InvalidJsonInputSchema

            return InvalidJsonInputSchema().load(data)
        if data["code"] == "InvalidInput":
            from ._schemas.errors import InvalidInputSchema

            return InvalidInputSchema().load(data)
        if data["code"] == "ResourceNotFound":
            from ._schemas.errors import ResourceNotFoundErrorSchema

            return ResourceNotFoundErrorSchema().load(data)
        if data["code"] == "ResourceCreation":
            from ._schemas.errors import ResourceCreationErrorSchema

            return ResourceCreationErrorSchema().load(data)
        if data["code"] == "ResourceUpdate":
            from ._schemas.errors import ResourceUpdateErrorSchema

            return ResourceUpdateErrorSchema().load(data)
        if data["code"] == "ResourceDeletion":
            from ._schemas.errors import ResourceDeletionErrorSchema

            return ResourceDeletionErrorSchema().load(data)
        if data["code"] == "RequiredField":
            from ._schemas.errors import RequiredFieldErrorSchema

            return RequiredFieldErrorSchema().load(data)
        if data["code"] == "InvalidTransition":
            from ._schemas.errors import InvalidStateTransitionErrorSchema

            return InvalidStateTransitionErrorSchema().load(data)
        if data["code"] == "ConcurrentModification":
            from ._schemas.errors import ConcurrentModificationErrorSchema

            return ConcurrentModificationErrorSchema().load(data)
        if data["code"] == "Contention":
            from ._schemas.errors import ContentionErrorSchema

            return ContentionErrorSchema().load(data)
        if data["code"] == "Generic":
            from ._schemas.errors import GenericErrorSchema

            return GenericErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ErrorObjectSchema

        return ErrorObjectSchema().dump(self)


class AccessDeniedError(ErrorObject):
    """This is the generic error code for access denied. In case of a wrong scope, an [InvalidScopeError](#invalidscopeerror) will be returned."""

    def __init__(self, *, message: str):

        super().__init__(message=message, code="access_denied")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "AccessDeniedError":
        from ._schemas.errors import AccessDeniedErrorSchema

        return AccessDeniedErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import AccessDeniedErrorSchema

        return AccessDeniedErrorSchema().dump(self)


class InvalidScopeError(ErrorObject):
    """The requested scope is invalid, unknown, malformed, or exceeds the scope granted by the resource owner."""

    def __init__(self, *, message: str):

        super().__init__(message=message, code="invalid_scope")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidScopeError":
        from ._schemas.errors import InvalidScopeErrorSchema

        return InvalidScopeErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidScopeErrorSchema

        return InvalidScopeErrorSchema().dump(self)


class InvalidOperation(ErrorObject):
    """The resources in the request are not in the valid state for the operation.
    The client application should validate the constraints described in the error message before sending the request again.

    """

    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidOperation")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidOperation":
        from ._schemas.errors import InvalidOperationSchema

        return InvalidOperationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidOperationSchema

        return InvalidOperationSchema().dump(self)


class DuplicateAttributeValueError(ErrorObject):
    """The `Unique` [Attribute Constraint](/../api/projects/productTypes#attributeconstraint-enum) was violated."""

    #: The attribute in conflict.
    attribute: "Attribute"

    def __init__(self, *, message: str, attribute: "Attribute"):
        self.attribute = attribute

        super().__init__(message=message, code="DuplicateAttributeValue")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateAttributeValueError":
        from ._schemas.errors import DuplicateAttributeValueErrorSchema

        return DuplicateAttributeValueErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import DuplicateAttributeValueErrorSchema

        return DuplicateAttributeValueErrorSchema().dump(self)


class DuplicateAttributeValuesError(ErrorObject):
    """The `CombinationUnique` [Attribute Constraint](/../api/projects/productTypes#attributeconstraint-enum) was violated."""

    attributes: typing.List["Attribute"]

    def __init__(self, *, message: str, attributes: typing.List["Attribute"]):
        self.attributes = attributes

        super().__init__(message=message, code="DuplicateAttributeValues")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateAttributeValuesError":
        from ._schemas.errors import DuplicateAttributeValuesErrorSchema

        return DuplicateAttributeValuesErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import DuplicateAttributeValuesErrorSchema

        return DuplicateAttributeValuesErrorSchema().dump(self)


class DuplicateFieldError(ErrorObject):
    """The given value already exists for a field that is checked for unique values."""

    #: The name of the field.
    field: typing.Optional[str]
    #: The offending duplicate value.
    duplicate_value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        message: str,
        field: typing.Optional[str] = None,
        duplicate_value: typing.Optional[typing.Any] = None
    ):
        self.field = field
        self.duplicate_value = duplicate_value

        super().__init__(message=message, code="DuplicateField")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DuplicateFieldError":
        from ._schemas.errors import DuplicateFieldErrorSchema

        return DuplicateFieldErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import DuplicateFieldErrorSchema

        return DuplicateFieldErrorSchema().dump(self)


class DuplicateVariantValuesError(ErrorObject):
    """The given combination of values of a [Product Variant](/../api/projects/products#productvariant) conflicts with an existing one.
    Every [Product Variant](/../api/projects/products#productvariant) must have a distinct combination of SKU, prices, and custom attribute values.

    """

    #: The offending variant values.
    variant_values: "VariantValues"

    def __init__(self, *, message: str, variant_values: "VariantValues"):
        self.variant_values = variant_values

        super().__init__(message=message, code="DuplicateVariantValues")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "DuplicateVariantValuesError":
        from ._schemas.errors import DuplicateVariantValuesErrorSchema

        return DuplicateVariantValuesErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import DuplicateVariantValuesErrorSchema

        return DuplicateVariantValuesErrorSchema().dump(self)


class VariantValues(_BaseType):
    sku: typing.Optional[str]
    prices: typing.List["PriceImport"]
    attributes: typing.List["Attribute"]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        prices: typing.List["PriceImport"],
        attributes: typing.List["Attribute"]
    ):
        self.sku = sku
        self.prices = prices
        self.attributes = attributes

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "VariantValues":
        from ._schemas.errors import VariantValuesSchema

        return VariantValuesSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import VariantValuesSchema

        return VariantValuesSchema().dump(self)


class InsufficientScopeError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="insufficient_scope")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InsufficientScopeError":
        from ._schemas.errors import InsufficientScopeErrorSchema

        return InsufficientScopeErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InsufficientScopeErrorSchema

        return InsufficientScopeErrorSchema().dump(self)


class InvalidCredentialsError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidCredentials")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InvalidCredentialsError":
        from ._schemas.errors import InvalidCredentialsErrorSchema

        return InvalidCredentialsErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidCredentialsErrorSchema

        return InvalidCredentialsErrorSchema().dump(self)


class InvalidTokenError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="invalid_token")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidTokenError":
        from ._schemas.errors import InvalidTokenErrorSchema

        return InvalidTokenErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidTokenErrorSchema

        return InvalidTokenErrorSchema().dump(self)


class InvalidFieldError(ErrorObject):
    """A given field is not supported.
    This error occurs, for example, if the field `variants`, which is not supported by [Product Import](/product#productimport), is sent to the Product Import endpoint.

    """

    #: The name of the field.
    field: str
    #: The invalid value.
    invalid_value: typing.Any
    #: The set of allowed values for the field, if any.
    allowed_values: typing.Optional[typing.List["typing.Any"]]
    resource_index: typing.Optional[int]

    def __init__(
        self,
        *,
        message: str,
        field: str,
        invalid_value: typing.Any,
        allowed_values: typing.Optional[typing.List["typing.Any"]] = None,
        resource_index: typing.Optional[int] = None
    ):
        self.field = field
        self.invalid_value = invalid_value
        self.allowed_values = allowed_values
        self.resource_index = resource_index

        super().__init__(message=message, code="InvalidField")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidFieldError":
        from ._schemas.errors import InvalidFieldErrorSchema

        return InvalidFieldErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidFieldErrorSchema

        return InvalidFieldErrorSchema().dump(self)


class InvalidJsonInput(ErrorObject):
    """An invalid JSON input has been sent to the service.
    Either the JSON is syntactically incorrect or the JSON has an unexpected shape, for example, a required field is missing.
    The client application should validate the input according to the constraints described in the error message before sending the request again.

    """

    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidJsonInput")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidJsonInput":
        from ._schemas.errors import InvalidJsonInputSchema

        return InvalidJsonInputSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidJsonInputSchema

        return InvalidJsonInputSchema().dump(self)


class InvalidInput(ErrorObject):
    """An invalid input has been sent to the service. The client application should validate the input according to the
    constraints described in the error message before sending the request again.

    """

    def __init__(self, *, message: str):

        super().__init__(message=message, code="InvalidInput")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "InvalidInput":
        from ._schemas.errors import InvalidInputSchema

        return InvalidInputSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidInputSchema

        return InvalidInputSchema().dump(self)


class ResourceNotFoundError(ErrorObject):
    resource: typing.Optional[typing.Any]

    def __init__(self, *, message: str, resource: typing.Optional[typing.Any] = None):
        self.resource = resource

        super().__init__(message=message, code="ResourceNotFound")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceNotFoundError":
        from ._schemas.errors import ResourceNotFoundErrorSchema

        return ResourceNotFoundErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ResourceNotFoundErrorSchema

        return ResourceNotFoundErrorSchema().dump(self)


class ResourceCreationError(ErrorObject):
    resource: typing.Optional[typing.Any]

    def __init__(self, *, message: str, resource: typing.Optional[typing.Any] = None):
        self.resource = resource

        super().__init__(message=message, code="ResourceCreation")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceCreationError":
        from ._schemas.errors import ResourceCreationErrorSchema

        return ResourceCreationErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ResourceCreationErrorSchema

        return ResourceCreationErrorSchema().dump(self)


class ResourceUpdateError(ErrorObject):
    resource: typing.Optional[typing.Any]

    def __init__(self, *, message: str, resource: typing.Optional[typing.Any] = None):
        self.resource = resource

        super().__init__(message=message, code="ResourceUpdate")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceUpdateError":
        from ._schemas.errors import ResourceUpdateErrorSchema

        return ResourceUpdateErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ResourceUpdateErrorSchema

        return ResourceUpdateErrorSchema().dump(self)


class ResourceDeletionError(ErrorObject):
    resource: typing.Optional[typing.Any]

    def __init__(self, *, message: str, resource: typing.Optional[typing.Any] = None):
        self.resource = resource

        super().__init__(message=message, code="ResourceDeletion")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ResourceDeletionError":
        from ._schemas.errors import ResourceDeletionErrorSchema

        return ResourceDeletionErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ResourceDeletionErrorSchema

        return ResourceDeletionErrorSchema().dump(self)


class RequiredFieldError(ErrorObject):
    """A required field is missing a value."""

    #: The name of the field.
    field: str

    def __init__(self, *, message: str, field: str):
        self.field = field

        super().__init__(message=message, code="RequiredField")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "RequiredFieldError":
        from ._schemas.errors import RequiredFieldErrorSchema

        return RequiredFieldErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import RequiredFieldErrorSchema

        return RequiredFieldErrorSchema().dump(self)


class InvalidStateTransitionError(ErrorObject):
    #: Every [Import Operation](/import-operation) is assigned with one of the following states.
    current_state: "ProcessingState"
    #: Every [Import Operation](/import-operation) is assigned with one of the following states.
    new_state: "ProcessingState"

    def __init__(
        self,
        *,
        message: str,
        current_state: "ProcessingState",
        new_state: "ProcessingState"
    ):
        self.current_state = current_state
        self.new_state = new_state

        super().__init__(message=message, code="InvalidTransition")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "InvalidStateTransitionError":
        from ._schemas.errors import InvalidStateTransitionErrorSchema

        return InvalidStateTransitionErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import InvalidStateTransitionErrorSchema

        return InvalidStateTransitionErrorSchema().dump(self)


class ConcurrentModificationError(ErrorObject):
    """The request conflicts with the current state of the involved resources.
    This error typically occurs when the request attempts to modify a resource that is out of date, that is, it has been modified by another client since the last time it was retrieved by the system attempting to update it.
    The client application should resolve the conflict (with or without involving the end-user) before retrying the request.

    """

    #: The version specified in the failed request.
    specified_version: typing.Optional[int]
    #: The current version of the resource.
    current_version: int
    #: The resource in conflict.
    conflicted_resource: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        message: str,
        specified_version: typing.Optional[int] = None,
        current_version: int,
        conflicted_resource: typing.Optional[typing.Any] = None
    ):
        self.specified_version = specified_version
        self.current_version = current_version
        self.conflicted_resource = conflicted_resource

        super().__init__(message=message, code="ConcurrentModification")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ConcurrentModificationError":
        from ._schemas.errors import ConcurrentModificationErrorSchema

        return ConcurrentModificationErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ConcurrentModificationErrorSchema

        return ConcurrentModificationErrorSchema().dump(self)


class ContentionError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="Contention")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ContentionError":
        from ._schemas.errors import ContentionErrorSchema

        return ContentionErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import ContentionErrorSchema

        return ContentionErrorSchema().dump(self)


class GenericError(ErrorObject):
    def __init__(self, *, message: str):

        super().__init__(message=message, code="Generic")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "GenericError":
        from ._schemas.errors import GenericErrorSchema

        return GenericErrorSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.errors import GenericErrorSchema

        return GenericErrorSchema().dump(self)
