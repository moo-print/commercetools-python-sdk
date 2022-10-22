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
from ..quote import QuoteState
from .common import BaseResourceSchema, ReferenceSchema, ResourceIdentifierSchema
from .type import FieldContainerField

# Fields


# Marshmallow Schemas
class QuoteSchema(BaseResourceSchema):
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
    quote_request = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".quote_request.QuoteRequestReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="quoteRequest",
    )
    staged_quote = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".staged_quote.StagedQuoteReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="stagedQuote",
    )
    customer = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".customer.CustomerReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
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
    valid_to = marshmallow.fields.DateTime(
        allow_none=True, metadata={"omit_empty": True}, missing=None, data_key="validTo"
    )
    seller_comment = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="sellerComment",
    )
    buyer_comment = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="buyerComment",
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
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    business_unit = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".business_unit.BusinessUnitKeyReferenceSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
        data_key="businessUnit",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Quote(**data)


class QuoteDraftSchema(helpers.BaseSchema):
    staged_quote = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".staged_quote.StagedQuoteResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
        data_key="stagedQuote",
    )
    staged_quote_version = marshmallow.fields.Integer(
        allow_none=True, missing=None, data_key="stagedQuoteVersion"
    )
    key = marshmallow.fields.String(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    custom = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldsDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateReferenceSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.QuoteDraft(**data)


class QuotePagedQueryResponseSchema(helpers.BaseSchema):
    limit = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True, missing=None)
    count = marshmallow.fields.Integer(allow_none=True, missing=None)
    total = marshmallow.fields.Integer(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )
    results = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".QuoteSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.QuotePagedQueryResponse(**data)


class QuoteReferenceSchema(ReferenceSchema):
    obj = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".QuoteSchema"),
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
        return models.QuoteReference(**data)


class QuoteResourceIdentifierSchema(ResourceIdentifierSchema):
    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return models.QuoteResourceIdentifier(**data)


class QuoteUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, missing=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeQuoteState": helpers.absmod(
                    __name__, ".QuoteChangeQuoteStateActionSchema"
                ),
                "requestQuoteRenegotiation": helpers.absmod(
                    __name__, ".QuoteRequestQuoteRenegotiationActionSchema"
                ),
                "setCustomField": helpers.absmod(
                    __name__, ".QuoteSetCustomFieldActionSchema"
                ),
                "setCustomType": helpers.absmod(
                    __name__, ".QuoteSetCustomTypeActionSchema"
                ),
                "transitionState": helpers.absmod(
                    __name__, ".QuoteTransitionStateActionSchema"
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

        return models.QuoteUpdate(**data)


class QuoteUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.QuoteUpdateAction(**data)


class QuoteChangeQuoteStateActionSchema(QuoteUpdateActionSchema):
    quote_state = marshmallow_enum.EnumField(
        QuoteState, by_value=True, allow_none=True, missing=None, data_key="quoteState"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.QuoteChangeQuoteStateAction(**data)


class QuoteRequestQuoteRenegotiationActionSchema(QuoteUpdateActionSchema):
    buyer_comment = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        missing=None,
        data_key="buyerComment",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.QuoteRequestQuoteRenegotiationAction(**data)


class QuoteSetCustomFieldActionSchema(QuoteUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, missing=None)
    value = marshmallow.fields.Raw(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.QuoteSetCustomFieldAction(**data)


class QuoteSetCustomTypeActionSchema(QuoteUpdateActionSchema):
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
        return models.QuoteSetCustomTypeAction(**data)


class QuoteTransitionStateActionSchema(QuoteUpdateActionSchema):
    state = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".state.StateResourceIdentifierSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        missing=None,
    )
    force = marshmallow.fields.Boolean(
        allow_none=True, metadata={"omit_empty": True}, missing=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.QuoteTransitionStateAction(**data)
