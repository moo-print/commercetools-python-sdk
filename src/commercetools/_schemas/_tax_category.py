# DO NOT EDIT! This file is automatically generated
import marshmallow

from commercetools import helpers, types
from commercetools._schemas._common import (
    BaseResourceSchema,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

__all__ = [
    "SubRateSchema",
    "TaxCategoryAddTaxRateActionSchema",
    "TaxCategoryChangeNameActionSchema",
    "TaxCategoryDraftSchema",
    "TaxCategoryPagedQueryResponseSchema",
    "TaxCategoryReferenceSchema",
    "TaxCategoryRemoveTaxRateActionSchema",
    "TaxCategoryReplaceTaxRateActionSchema",
    "TaxCategoryResourceIdentifierSchema",
    "TaxCategorySchema",
    "TaxCategorySetDescriptionActionSchema",
    "TaxCategorySetKeyActionSchema",
    "TaxCategoryUpdateActionSchema",
    "TaxCategoryUpdateSchema",
    "TaxRateDraftSchema",
    "TaxRateSchema",
]


class SubRateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.SubRate`."""

    name = marshmallow.fields.String(allow_none=True)
    amount = marshmallow.fields.Float(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.SubRate(**data)


class TaxCategoryDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryDraft`."""

    name = marshmallow.fields.String(allow_none=True)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    rates = helpers.LazyNestedField(
        nested="commercetools._schemas._tax_category.TaxRateDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.TaxCategoryDraft(**data)


class TaxCategoryPagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryPagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = helpers.LazyNestedField(
        nested="commercetools._schemas._tax_category.TaxCategorySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.TaxCategoryPagedQueryResponse(**data)


class TaxCategoryReferenceSchema(ReferenceSchema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryReference`."""

    obj = helpers.LazyNestedField(
        nested="commercetools._schemas._tax_category.TaxCategorySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.TaxCategoryReference(**data)


class TaxCategoryResourceIdentifierSchema(ResourceIdentifierSchema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryResourceIdentifier`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.TaxCategoryResourceIdentifier(**data)


class TaxCategorySchema(BaseResourceSchema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategory`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )
    last_modified_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.LastModifiedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="lastModifiedBy",
    )
    created_by = helpers.LazyNestedField(
        nested="commercetools._schemas._common.CreatedBySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="createdBy",
    )
    name = marshmallow.fields.String(allow_none=True)
    description = marshmallow.fields.String(allow_none=True, missing=None)
    rates = helpers.LazyNestedField(
        nested="commercetools._schemas._tax_category.TaxRateSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.TaxCategory(**data)


class TaxCategoryUpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryUpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.TaxCategoryUpdateAction(**data)


class TaxCategoryUpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryUpdate`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "addTaxRate": "commercetools._schemas._tax_category.TaxCategoryAddTaxRateActionSchema",
                "changeName": "commercetools._schemas._tax_category.TaxCategoryChangeNameActionSchema",
                "removeTaxRate": "commercetools._schemas._tax_category.TaxCategoryRemoveTaxRateActionSchema",
                "replaceTaxRate": "commercetools._schemas._tax_category.TaxCategoryReplaceTaxRateActionSchema",
                "setDescription": "commercetools._schemas._tax_category.TaxCategorySetDescriptionActionSchema",
                "setKey": "commercetools._schemas._tax_category.TaxCategorySetKeyActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.TaxCategoryUpdate(**data)


class TaxRateDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.TaxRateDraft`."""

    name = marshmallow.fields.String(allow_none=True)
    amount = marshmallow.fields.Float(allow_none=True, missing=None)
    included_in_price = marshmallow.fields.Bool(
        allow_none=True, data_key="includedInPrice"
    )
    country = marshmallow.fields.String()
    state = marshmallow.fields.String(allow_none=True, missing=None)
    sub_rates = helpers.LazyNestedField(
        nested="commercetools._schemas._tax_category.SubRateSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
        data_key="subRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.TaxRateDraft(**data)


class TaxRateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.TaxRate`."""

    id = marshmallow.fields.String(allow_none=True, missing=None)
    name = marshmallow.fields.String(allow_none=True)
    amount = marshmallow.fields.Float(allow_none=True)
    included_in_price = marshmallow.fields.Bool(
        allow_none=True, data_key="includedInPrice"
    )
    country = marshmallow.fields.String()
    state = marshmallow.fields.String(allow_none=True, missing=None)
    sub_rates = helpers.LazyNestedField(
        nested="commercetools._schemas._tax_category.SubRateSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
        data_key="subRates",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.TaxRate(**data)


class TaxCategoryAddTaxRateActionSchema(TaxCategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryAddTaxRateAction`."""

    tax_rate = helpers.LazyNestedField(
        nested="commercetools._schemas._tax_category.TaxRateDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="taxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.TaxCategoryAddTaxRateAction(**data)


class TaxCategoryChangeNameActionSchema(TaxCategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryChangeNameAction`."""

    name = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.TaxCategoryChangeNameAction(**data)


class TaxCategoryRemoveTaxRateActionSchema(TaxCategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryRemoveTaxRateAction`."""

    tax_rate_id = marshmallow.fields.String(allow_none=True, data_key="taxRateId")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.TaxCategoryRemoveTaxRateAction(**data)


class TaxCategoryReplaceTaxRateActionSchema(TaxCategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategoryReplaceTaxRateAction`."""

    tax_rate_id = marshmallow.fields.String(allow_none=True, data_key="taxRateId")
    tax_rate = helpers.LazyNestedField(
        nested="commercetools._schemas._tax_category.TaxRateDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="taxRate",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.TaxCategoryReplaceTaxRateAction(**data)


class TaxCategorySetDescriptionActionSchema(TaxCategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategorySetDescriptionAction`."""

    description = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.TaxCategorySetDescriptionAction(**data)


class TaxCategorySetKeyActionSchema(TaxCategoryUpdateActionSchema):
    """Marshmallow schema for :class:`commercetools.types.TaxCategorySetKeyAction`."""

    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return types.TaxCategorySetKeyAction(**data)