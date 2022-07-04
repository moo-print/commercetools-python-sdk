# This file is automatically generated by the rmf-codegen project.
#
# The Python code generator is maintained by Lab Digital. If you want to
# contribute to this project then please do not edit this file directly
# but send a pull request to the Lab Digital fork of rmf-codegen at
# https://github.com/labd/rmf-codegen
import re
import typing

import marshmallow
import marshmallow_enum

from commercetools import helpers

from ... import models
from ..cart import InventoryMode, RoundingMode, TaxCalculationMode, TaxMode
from ..common import ReferenceTypeId
from ..quote_request import QuoteRequestState
from .common import BaseResourceSchema, ReferenceSchema, ResourceIdentifierSchema
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class QuoteRequestSchema(BaseResourceSchema):
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.CreatedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="createdBy",
    )
    quote_request_state = marshmallow_enum.EnumField(
        QuoteRequestState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="quoteRequestState",
    )
    comment = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    customer_group = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer_group.CustomerGroupReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="customerGroup",
    )
    store = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".store.StoreKeyReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.LineItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="lineItems",
    )
    custom_line_items = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.CustomLineItemSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="customLineItems",
    )
    total_price = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": helpers.absmod(
                __name__, ".common.CentPrecisionMoneySchema"
            ),
            "highPrecision": helpers.absmod(
                __name__, ".common.HighPrecisionMoneySchema"
            ),
        },
        missing=None,
        data_key="totalPrice",
    )
    taxed_price = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.TaxedPriceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="taxedPrice",
    )
    shipping_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingAddress",
    )
    billing_address = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="billingAddress",
    )
    inventory_mode = marshmallow_enum.EnumField(
        InventoryMode,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="inventoryMode",
    )
    tax_mode = marshmallow_enum.EnumField(
        TaxMode, by_value=True, allow_none=True, missing=None, data_key="taxMode"
    )
    tax_rounding_mode = marshmallow_enum.EnumField(
        RoundingMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxRoundingMode",
    )
    tax_calculation_mode = marshmallow_enum.EnumField(
        TaxCalculationMode,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="taxCalculationMode",
    )
    country = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    shipping_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.ShippingInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingInfo",
    )
    payment_info = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".order.PaymentInfoSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="paymentInfo",
    )
    shipping_rate_input = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "Classification": helpers.absmod(
                __name__, ".cart.ClassificationShippingRateInputSchema"
            ),
            "Score": helpers.absmod(__name__, ".cart.ScoreShippingRateInputSchema"),
        },
        metadata={"omit_empty": True},
        missing=None,
        data_key="shippingRateInput",
    )
    item_shipping_addresses = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.AddressSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="itemShippingAddresses",
    )
    direct_discounts = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.DirectDiscountSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="directDiscounts",
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.QuoteRequest(**data)


class QuoteRequestDraftSchema(helpers.BaseSchema):
    cart = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".cart.CartResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    cart_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="cartVersion"
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    comment = marshmallow.fields.String(allow_none=True, missing=None)
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.QuoteRequestDraft(**data)


class QuoteRequestPagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".QuoteRequestSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.QuoteRequestPagedQueryResponse(**data)


class QuoteRequestReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".QuoteRequestSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.QuoteRequestReference(**data)


class QuoteRequestResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.QuoteRequestResourceIdentifier(**data)


class QuoteRequestUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeQuoteRequestState": helpers.absmod(
                    __name__, ".QuoteRequestChangeQuoteRequestStateActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".QuoteRequestSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".QuoteRequestSetCustomTypeActionSchema"
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

        return models.QuoteRequestUpdate(**data)


class QuoteRequestUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.QuoteRequestUpdateAction(**data)


class QuoteRequestChangeQuoteRequestStateActionSchema(QuoteRequestUpdateActionSchema):
    quote_request_state = marshmallow_enum.EnumField(
        QuoteRequestState,
        by_value=True,
        allow_none=True,
        missing=None,
        data_key="quoteRequestState",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.QuoteRequestChangeQuoteRequestStateAction(**data)


class QuoteRequestSetCustomFieldActionSchema(QuoteRequestUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.QuoteRequestSetCustomFieldAction(**data)


class QuoteRequestSetCustomTypeActionSchema(QuoteRequestUpdateActionSchema):
    type = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.TypeResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    fields = FieldContainerField(
        allow_none=True,
        values=marshmallow.fields.Raw(allow_none=True),
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.QuoteRequestSetCustomTypeAction(**data)