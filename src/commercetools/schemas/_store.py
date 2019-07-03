# DO NOT EDIT! This file is automatically generated

import marshmallow

from commercetools import helpers, types
from commercetools.schemas._common import (
    BaseResourceSchema,
    KeyReferenceSchema,
    LocalizedStringField,
    PagedQueryResponseSchema,
    ReferenceSchema,
    ResourceIdentifierSchema,
)

__all__ = [
    "StoreDraftSchema",
    "StoreKeyReferenceSchema",
    "StorePagedQueryResponseSchema",
    "StoreReferenceSchema",
    "StoreResourceIdentifierSchema",
    "StoreSchema",
    "StoreSetNameActionSchema",
    "StoreUpdateActionSchema",
    "StoreUpdateSchema",
]


class StoreDraftSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.StoreDraft`."
    key = marshmallow.fields.String(allow_none=True)
    name = LocalizedStringField(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.StoreDraft(**data)


class StoreKeyReferenceSchema(KeyReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.StoreKeyReference`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.StoreKeyReference(**data)


class StorePagedQueryResponseSchema(PagedQueryResponseSchema):
    "Marshmallow schema for :class:`commercetools.types.StorePagedQueryResponse`."
    results = marshmallow.fields.Nested(
        nested="commercetools.schemas._store.StoreSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.StorePagedQueryResponse(**data)


class StoreReferenceSchema(ReferenceSchema):
    "Marshmallow schema for :class:`commercetools.types.StoreReference`."
    obj = marshmallow.fields.Nested(
        nested="commercetools.schemas._store.StoreSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.StoreReference(**data)


class StoreResourceIdentifierSchema(ResourceIdentifierSchema):
    "Marshmallow schema for :class:`commercetools.types.StoreResourceIdentifier`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type_id"]
        return types.StoreResourceIdentifier(**data)


class StoreSchema(BaseResourceSchema):
    "Marshmallow schema for :class:`commercetools.types.Store`."
    key = marshmallow.fields.String(allow_none=True)
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.Store(**data)


class StoreUpdateActionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.StoreUpdateAction`."
    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StoreUpdateAction(**data)


class StoreUpdateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.StoreUpdate`."
    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "setName": "commercetools.schemas._store.StoreSetNameActionSchema"
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.StoreUpdate(**data)


class StoreSetNameActionSchema(StoreUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.StoreSetNameAction`."
    name = LocalizedStringField(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.StoreSetNameAction(**data)
