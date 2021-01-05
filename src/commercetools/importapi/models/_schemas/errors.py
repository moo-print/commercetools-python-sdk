# Generated file, please do not change!!!
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..common import ProcessingState

# Fields


# Marshmallow Schemas
class ErrorResponseSchema(helpers.BaseSchema):
    status_code = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="statusCode"
    )
    message = marshmallow.fields.String(allow_none=True, missing=None)
    error = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    error_description = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    errors = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("code", "code"),
            discriminator_schemas={
                "access_denied": helpers.absmod(__name__, ".AccessDeniedErrorSchema"),
                "invalid_scope": helpers.absmod(__name__, ".InvalidScopeErrorSchema"),
                "InvalidOperation": helpers.absmod(__name__, ".InvalidOperationSchema"),
                "DuplicateAttributeValue": helpers.absmod(
                    __name__, ".DuplicateAttributeValueErrorSchema"
                ),
                "DuplicateAttributeValues": helpers.absmod(
                    __name__, ".DuplicateAttributeValuesErrorSchema"
                ),
                "DuplicateField": helpers.absmod(
                    __name__, ".DuplicateFieldErrorSchema"
                ),
                "DuplicateVariantValues": helpers.absmod(
                    __name__, ".DuplicateVariantValuesErrorSchema"
                ),
                "insufficient_scope": helpers.absmod(
                    __name__, ".InsufficientScopeErrorSchema"
                ),
                "InvalidCredentials": helpers.absmod(
                    __name__, ".InvalidCredentialsErrorSchema"
                ),
                "invalid_token": helpers.absmod(__name__, ".InvalidTokenErrorSchema"),
                "InvalidField": helpers.absmod(__name__, ".InvalidFieldErrorSchema"),
                "InvalidJsonInput": helpers.absmod(__name__, ".InvalidJsonInputSchema"),
                "InvalidInput": helpers.absmod(__name__, ".InvalidInputSchema"),
                "ResourceNotFound": helpers.absmod(
                    __name__, ".ResourceNotFoundErrorSchema"
                ),
                "ResourceCreation": helpers.absmod(
                    __name__, ".ResourceCreationErrorSchema"
                ),
                "ResourceUpdate": helpers.absmod(
                    __name__, ".ResourceUpdateErrorSchema"
                ),
                "ResourceDeletion": helpers.absmod(
                    __name__, ".ResourceDeletionErrorSchema"
                ),
                "RequiredField": helpers.absmod(__name__, ".RequiredFieldErrorSchema"),
                "InvalidTransition": helpers.absmod(
                    __name__, ".InvalidStateTransitionErrorSchema"
                ),
                "ConcurrentModification": helpers.absmod(
                    __name__, ".ConcurrentModificationErrorSchema"
                ),
                "Contention": helpers.absmod(__name__, ".ContentionErrorSchema"),
                "Generic": helpers.absmod(__name__, ".GenericErrorSchema"),
            },
        ),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ErrorResponse(**data)


class ErrorObjectSchema(helpers.BaseSchema):
    code = marshmallow.fields.String(allow_none=True, missing=None)
    message = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ErrorObject(**data)


class AccessDeniedErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.AccessDeniedError(**data)


class InvalidScopeErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidScopeError(**data)


class InvalidOperationSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidOperation(**data)


class DuplicateAttributeValueErrorSchema(ErrorObjectSchema):
    attribute = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "boolean": helpers.absmod(
                __name__, ".productvariants.BooleanAttributeSchema"
            ),
            "boolean-set": helpers.absmod(
                __name__, ".productvariants.BooleanSetAttributeSchema"
            ),
            "date": helpers.absmod(__name__, ".productvariants.DateAttributeSchema"),
            "date-set": helpers.absmod(
                __name__, ".productvariants.DateSetAttributeSchema"
            ),
            "datetime": helpers.absmod(
                __name__, ".productvariants.DateTimeAttributeSchema"
            ),
            "datetime-set": helpers.absmod(
                __name__, ".productvariants.DateTimeSetAttributeSchema"
            ),
            "enum": helpers.absmod(__name__, ".productvariants.EnumAttributeSchema"),
            "enum-set": helpers.absmod(
                __name__, ".productvariants.EnumSetAttributeSchema"
            ),
            "lenum": helpers.absmod(
                __name__, ".productvariants.LocalizableEnumAttributeSchema"
            ),
            "lenum-set": helpers.absmod(
                __name__, ".productvariants.LocalizableEnumSetAttributeSchema"
            ),
            "ltext": helpers.absmod(
                __name__, ".productvariants.LocalizableTextAttributeSchema"
            ),
            "ltext-set": helpers.absmod(
                __name__, ".productvariants.LocalizableTextSetAttributeSchema"
            ),
            "money": helpers.absmod(__name__, ".productvariants.MoneyAttributeSchema"),
            "money-set": helpers.absmod(
                __name__, ".productvariants.MoneySetAttributeSchema"
            ),
            "number": helpers.absmod(
                __name__, ".productvariants.NumberAttributeSchema"
            ),
            "number-set": helpers.absmod(
                __name__, ".productvariants.NumberSetAttributeSchema"
            ),
            "reference": helpers.absmod(
                __name__, ".productvariants.ReferenceAttributeSchema"
            ),
            "reference-set": helpers.absmod(
                __name__, ".productvariants.ReferenceSetAttributeSchema"
            ),
            "text": helpers.absmod(__name__, ".productvariants.TextAttributeSchema"),
            "text-set": helpers.absmod(
                __name__, ".productvariants.TextSetAttributeSchema"
            ),
            "time": helpers.absmod(__name__, ".productvariants.TimeAttributeSchema"),
            "time-set": helpers.absmod(
                __name__, ".productvariants.TimeSetAttributeSchema"
            ),
        },
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateAttributeValueError(**data)


class DuplicateAttributeValuesErrorSchema(ErrorObjectSchema):
    attributes = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "boolean": helpers.absmod(
                    __name__, ".productvariants.BooleanAttributeSchema"
                ),
                "boolean-set": helpers.absmod(
                    __name__, ".productvariants.BooleanSetAttributeSchema"
                ),
                "date": helpers.absmod(
                    __name__, ".productvariants.DateAttributeSchema"
                ),
                "date-set": helpers.absmod(
                    __name__, ".productvariants.DateSetAttributeSchema"
                ),
                "datetime": helpers.absmod(
                    __name__, ".productvariants.DateTimeAttributeSchema"
                ),
                "datetime-set": helpers.absmod(
                    __name__, ".productvariants.DateTimeSetAttributeSchema"
                ),
                "enum": helpers.absmod(
                    __name__, ".productvariants.EnumAttributeSchema"
                ),
                "enum-set": helpers.absmod(
                    __name__, ".productvariants.EnumSetAttributeSchema"
                ),
                "lenum": helpers.absmod(
                    __name__, ".productvariants.LocalizableEnumAttributeSchema"
                ),
                "lenum-set": helpers.absmod(
                    __name__, ".productvariants.LocalizableEnumSetAttributeSchema"
                ),
                "ltext": helpers.absmod(
                    __name__, ".productvariants.LocalizableTextAttributeSchema"
                ),
                "ltext-set": helpers.absmod(
                    __name__, ".productvariants.LocalizableTextSetAttributeSchema"
                ),
                "money": helpers.absmod(
                    __name__, ".productvariants.MoneyAttributeSchema"
                ),
                "money-set": helpers.absmod(
                    __name__, ".productvariants.MoneySetAttributeSchema"
                ),
                "number": helpers.absmod(
                    __name__, ".productvariants.NumberAttributeSchema"
                ),
                "number-set": helpers.absmod(
                    __name__, ".productvariants.NumberSetAttributeSchema"
                ),
                "reference": helpers.absmod(
                    __name__, ".productvariants.ReferenceAttributeSchema"
                ),
                "reference-set": helpers.absmod(
                    __name__, ".productvariants.ReferenceSetAttributeSchema"
                ),
                "text": helpers.absmod(
                    __name__, ".productvariants.TextAttributeSchema"
                ),
                "text-set": helpers.absmod(
                    __name__, ".productvariants.TextSetAttributeSchema"
                ),
                "time": helpers.absmod(
                    __name__, ".productvariants.TimeAttributeSchema"
                ),
                "time-set": helpers.absmod(
                    __name__, ".productvariants.TimeSetAttributeSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateAttributeValuesError(**data)


class DuplicateFieldErrorSchema(ErrorObjectSchema):
    field = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    duplicate_value = marshmallow.fields.Raw(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="duplicateValue",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateFieldError(**data)


class DuplicateVariantValuesErrorSchema(ErrorObjectSchema):
    variant_values = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".VariantValuesSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="variantValues",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.DuplicateVariantValuesError(**data)


class VariantValuesSchema(helpers.BaseSchema):
    sku = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    prices = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".prices.PriceImportSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    attributes = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("type", "type"),
            discriminator_schemas={
                "boolean": helpers.absmod(
                    __name__, ".productvariants.BooleanAttributeSchema"
                ),
                "boolean-set": helpers.absmod(
                    __name__, ".productvariants.BooleanSetAttributeSchema"
                ),
                "date": helpers.absmod(
                    __name__, ".productvariants.DateAttributeSchema"
                ),
                "date-set": helpers.absmod(
                    __name__, ".productvariants.DateSetAttributeSchema"
                ),
                "datetime": helpers.absmod(
                    __name__, ".productvariants.DateTimeAttributeSchema"
                ),
                "datetime-set": helpers.absmod(
                    __name__, ".productvariants.DateTimeSetAttributeSchema"
                ),
                "enum": helpers.absmod(
                    __name__, ".productvariants.EnumAttributeSchema"
                ),
                "enum-set": helpers.absmod(
                    __name__, ".productvariants.EnumSetAttributeSchema"
                ),
                "lenum": helpers.absmod(
                    __name__, ".productvariants.LocalizableEnumAttributeSchema"
                ),
                "lenum-set": helpers.absmod(
                    __name__, ".productvariants.LocalizableEnumSetAttributeSchema"
                ),
                "ltext": helpers.absmod(
                    __name__, ".productvariants.LocalizableTextAttributeSchema"
                ),
                "ltext-set": helpers.absmod(
                    __name__, ".productvariants.LocalizableTextSetAttributeSchema"
                ),
                "money": helpers.absmod(
                    __name__, ".productvariants.MoneyAttributeSchema"
                ),
                "money-set": helpers.absmod(
                    __name__, ".productvariants.MoneySetAttributeSchema"
                ),
                "number": helpers.absmod(
                    __name__, ".productvariants.NumberAttributeSchema"
                ),
                "number-set": helpers.absmod(
                    __name__, ".productvariants.NumberSetAttributeSchema"
                ),
                "reference": helpers.absmod(
                    __name__, ".productvariants.ReferenceAttributeSchema"
                ),
                "reference-set": helpers.absmod(
                    __name__, ".productvariants.ReferenceSetAttributeSchema"
                ),
                "text": helpers.absmod(
                    __name__, ".productvariants.TextAttributeSchema"
                ),
                "text-set": helpers.absmod(
                    __name__, ".productvariants.TextSetAttributeSchema"
                ),
                "time": helpers.absmod(
                    __name__, ".productvariants.TimeAttributeSchema"
                ),
                "time-set": helpers.absmod(
                    __name__, ".productvariants.TimeSetAttributeSchema"
                ),
            },
        ),
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.VariantValues(**data)


class InsufficientScopeErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InsufficientScopeError(**data)


class InvalidCredentialsErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidCredentialsError(**data)


class InvalidTokenErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidTokenError(**data)


class InvalidFieldErrorSchema(ErrorObjectSchema):
    field = marshmallow.fields.String(allow_none=True, missing=None)
    invalid_value = marshmallow.fields.Raw(
        allow_none=True, missing=None, data_key="invalidValue"
    )
    allowed_values = marshmallow.fields.List(
        marshmallow.fields.Raw(allow_none=True),
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="allowedValues",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidFieldError(**data)


class InvalidJsonInputSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidJsonInput(**data)


class InvalidInputSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidInput(**data)


class ResourceNotFoundErrorSchema(ErrorObjectSchema):
    resource = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ResourceNotFoundError(**data)


class ResourceCreationErrorSchema(ErrorObjectSchema):
    resource = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ResourceCreationError(**data)


class ResourceUpdateErrorSchema(ErrorObjectSchema):
    resource = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ResourceUpdateError(**data)


class ResourceDeletionErrorSchema(ErrorObjectSchema):
    resource = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ResourceDeletionError(**data)


class RequiredFieldErrorSchema(ErrorObjectSchema):
    field = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.RequiredFieldError(**data)


class InvalidStateTransitionErrorSchema(ErrorObjectSchema):
    current_state = marshmallow_enum.EnumField(
        ProcessingState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="currentState",
    )
    new_state = marshmallow_enum.EnumField(
        ProcessingState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="newState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.InvalidStateTransitionError(**data)


class ConcurrentModificationErrorSchema(ErrorObjectSchema):
    specified_version = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="specifiedVersion",
    )
    current_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="currentVersion"
    )
    conflicted_resource = marshmallow.fields.Raw(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="conflictedResource",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ConcurrentModificationError(**data)


class ContentionErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.ContentionError(**data)


class GenericErrorSchema(ErrorObjectSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["code"]
        return models.GenericError(**data)