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
from ..project import (
    BusinessUnitConfigurationStatus,
    OrderSearchStatus,
    SearchIndexingConfigurationStatus,
)
from ..shipping_method import ShippingRateTierType

# Fields


# Marshmallow Schemas
class BusinessUnitConfigurationSchema(helpers.BaseSchema):
    my_business_unit_status_on_creation = marshmallow_enum.EnumField(
        BusinessUnitConfigurationStatus,
        by_value=True,
        allow_none=True,
        load_default=None,
        data_key="myBusinessUnitStatusOnCreation",
    )
    my_business_unit_associate_role_on_creation = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".associate_role.AssociateRoleKeyReferenceSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="myBusinessUnitAssociateRoleOnCreation",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.BusinessUnitConfiguration(**data)


class CartsConfigurationSchema(helpers.BaseSchema):
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="deleteDaysAfterLastModification",
    )
    country_tax_rate_fallback_enabled = marshmallow.fields.Boolean(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="countryTaxRateFallbackEnabled",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.CartsConfiguration(**data)


class ExternalOAuthSchema(helpers.BaseSchema):
    url = marshmallow.fields.String(allow_none=True, load_default=None)
    authorization_header = marshmallow.fields.String(
        allow_none=True, load_default=None, data_key="authorizationHeader"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ExternalOAuth(**data)


class ProjectSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, load_default=None)
    key = marshmallow.fields.String(allow_none=True, load_default=None)
    name = marshmallow.fields.String(allow_none=True, load_default=None)
    countries = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, load_default=None
    )
    currencies = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, load_default=None
    )
    languages = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, load_default=None
    )
    created_at = marshmallow.fields.DateTime(
        allow_none=True, load_default=None, data_key="createdAt"
    )
    trial_until = marshmallow.fields.String(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="trialUntil",
    )
    messages = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".message.MessagesConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    carts = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CartsConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )
    shopping_lists = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShoppingListsConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="shoppingLists",
    )
    shipping_rate_input_type = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CartClassification": helpers.absmod(
                __name__, ".CartClassificationTypeSchema"
            ),
            "CartScore": helpers.absmod(__name__, ".CartScoreTypeSchema"),
            "CartValue": helpers.absmod(__name__, ".CartValueTypeSchema"),
        },
        metadata={"omit_empty": True},
        load_default=None,
        data_key="shippingRateInputType",
    )
    external_o_auth = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalOAuthSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="externalOAuth",
    )
    search_indexing = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SearchIndexingConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="searchIndexing",
    )
    business_units = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".BusinessUnitConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="businessUnits",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.Project(**data)


class ProjectUpdateSchema(helpers.BaseSchema):
    version = marshmallow.fields.Integer(allow_none=True, load_default=None)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            allow_none=True,
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeMyBusinessUnitStatusOnCreation": helpers.absmod(
                    __name__, ".ProjectChangeBusinessUnitStatusOnCreationActionSchema"
                ),
                "changeCartsConfiguration": helpers.absmod(
                    __name__, ".ProjectChangeCartsConfigurationActionSchema"
                ),
                "changeCountries": helpers.absmod(
                    __name__, ".ProjectChangeCountriesActionSchema"
                ),
                "changeCountryTaxRateFallbackEnabled": helpers.absmod(
                    __name__, ".ProjectChangeCountryTaxRateFallbackEnabledActionSchema"
                ),
                "changeCurrencies": helpers.absmod(
                    __name__, ".ProjectChangeCurrenciesActionSchema"
                ),
                "changeLanguages": helpers.absmod(
                    __name__, ".ProjectChangeLanguagesActionSchema"
                ),
                "changeMessagesConfiguration": helpers.absmod(
                    __name__, ".ProjectChangeMessagesConfigurationActionSchema"
                ),
                "changeMessagesEnabled": helpers.absmod(
                    __name__, ".ProjectChangeMessagesEnabledActionSchema"
                ),
                "changeName": helpers.absmod(
                    __name__, ".ProjectChangeNameActionSchema"
                ),
                "changeOrderSearchStatus": helpers.absmod(
                    __name__, ".ProjectChangeOrderSearchStatusActionSchema"
                ),
                "changeProductSearchIndexingEnabled": helpers.absmod(
                    __name__, ".ProjectChangeProductSearchIndexingEnabledActionSchema"
                ),
                "changeShoppingListsConfiguration": helpers.absmod(
                    __name__, ".ProjectChangeShoppingListsConfigurationActionSchema"
                ),
                "setMyBusinessUnitAssociateRoleOnCreation": helpers.absmod(
                    __name__,
                    ".ProjectSetBusinessUnitAssociateRoleOnCreationActionSchema",
                ),
                "setExternalOAuth": helpers.absmod(
                    __name__, ".ProjectSetExternalOAuthActionSchema"
                ),
                "setShippingRateInputType": helpers.absmod(
                    __name__, ".ProjectSetShippingRateInputTypeActionSchema"
                ),
            },
        ),
        allow_none=True,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ProjectUpdate(**data)


class ProjectUpdateActionSchema(helpers.BaseSchema):
    action = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectUpdateAction(**data)


class SearchIndexingConfigurationSchema(helpers.BaseSchema):
    products = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SearchIndexingConfigurationValuesSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )
    orders = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".SearchIndexingConfigurationValuesSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SearchIndexingConfiguration(**data)


class SearchIndexingConfigurationValuesSchema(helpers.BaseSchema):
    status = marshmallow_enum.EnumField(
        SearchIndexingConfigurationStatus,
        by_value=True,
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
    )
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="lastModifiedAt",
    )
    last_modified_by = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".common.LastModifiedBySchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="lastModifiedBy",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.SearchIndexingConfigurationValues(**data)


class ShippingRateInputTypeSchema(helpers.BaseSchema):
    type = marshmallow_enum.EnumField(
        ShippingRateTierType, by_value=True, allow_none=True, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.ShippingRateInputType(**data)


class CartClassificationTypeSchema(ShippingRateInputTypeSchema):
    values = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".type.CustomFieldLocalizedEnumValueSchema"),
        allow_none=True,
        many=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartClassificationType(**data)


class CartScoreTypeSchema(ShippingRateInputTypeSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartScoreType(**data)


class CartValueTypeSchema(ShippingRateInputTypeSchema):

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return models.CartValueType(**data)


class ShoppingListsConfigurationSchema(helpers.BaseSchema):
    delete_days_after_last_modification = marshmallow.fields.Integer(
        allow_none=True,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="deleteDaysAfterLastModification",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):

        return models.ShoppingListsConfiguration(**data)


class ProjectChangeBusinessUnitStatusOnCreationActionSchema(ProjectUpdateActionSchema):
    status = marshmallow_enum.EnumField(
        BusinessUnitConfigurationStatus,
        by_value=True,
        allow_none=True,
        load_default=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeBusinessUnitStatusOnCreationAction(**data)


class ProjectChangeCartsConfigurationActionSchema(ProjectUpdateActionSchema):
    carts_configuration = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".CartsConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="cartsConfiguration",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeCartsConfigurationAction(**data)


class ProjectChangeCountriesActionSchema(ProjectUpdateActionSchema):
    countries = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeCountriesAction(**data)


class ProjectChangeCountryTaxRateFallbackEnabledActionSchema(ProjectUpdateActionSchema):
    country_tax_rate_fallback_enabled = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="countryTaxRateFallbackEnabled"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeCountryTaxRateFallbackEnabledAction(**data)


class ProjectChangeCurrenciesActionSchema(ProjectUpdateActionSchema):
    currencies = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeCurrenciesAction(**data)


class ProjectChangeLanguagesActionSchema(ProjectUpdateActionSchema):
    languages = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), allow_none=True, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeLanguagesAction(**data)


class ProjectChangeMessagesConfigurationActionSchema(ProjectUpdateActionSchema):
    messages_configuration = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".message.MessagesConfigurationDraftSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="messagesConfiguration",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeMessagesConfigurationAction(**data)


class ProjectChangeMessagesEnabledActionSchema(ProjectUpdateActionSchema):
    messages_enabled = marshmallow.fields.Boolean(
        allow_none=True, load_default=None, data_key="messagesEnabled"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeMessagesEnabledAction(**data)


class ProjectChangeNameActionSchema(ProjectUpdateActionSchema):
    name = marshmallow.fields.String(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeNameAction(**data)


class ProjectChangeOrderSearchStatusActionSchema(ProjectUpdateActionSchema):
    status = marshmallow_enum.EnumField(
        OrderSearchStatus, by_value=True, allow_none=True, load_default=None
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeOrderSearchStatusAction(**data)


class ProjectChangeProductSearchIndexingEnabledActionSchema(ProjectUpdateActionSchema):
    enabled = marshmallow.fields.Boolean(allow_none=True, load_default=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeProductSearchIndexingEnabledAction(**data)


class ProjectChangeShoppingListsConfigurationActionSchema(ProjectUpdateActionSchema):
    shopping_lists_configuration = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ShoppingListsConfigurationSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="shoppingListsConfiguration",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectChangeShoppingListsConfigurationAction(**data)


class ProjectSetBusinessUnitAssociateRoleOnCreationActionSchema(
    ProjectUpdateActionSchema
):
    associate_role = helpers.LazyNestedField(
        nested=helpers.absmod(
            __name__, ".associate_role.AssociateRoleResourceIdentifierSchema"
        ),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        load_default=None,
        data_key="associateRole",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectSetBusinessUnitAssociateRoleOnCreationAction(**data)


class ProjectSetExternalOAuthActionSchema(ProjectUpdateActionSchema):
    external_o_auth = helpers.LazyNestedField(
        nested=helpers.absmod(__name__, ".ExternalOAuthSchema"),
        allow_none=True,
        unknown=marshmallow.EXCLUDE,
        metadata={"omit_empty": True},
        load_default=None,
        data_key="externalOAuth",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectSetExternalOAuthAction(**data)


class ProjectSetShippingRateInputTypeActionSchema(ProjectUpdateActionSchema):
    shipping_rate_input_type = helpers.Discriminator(
        allow_none=True,
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CartClassification": helpers.absmod(
                __name__, ".CartClassificationTypeSchema"
            ),
            "CartScore": helpers.absmod(__name__, ".CartScoreTypeSchema"),
            "CartValue": helpers.absmod(__name__, ".CartValueTypeSchema"),
        },
        metadata={"omit_empty": True},
        load_default=None,
        data_key="shippingRateInputType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["action"]
        return models.ProjectSetShippingRateInputTypeAction(**data)
