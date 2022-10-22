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
from .shipping_method import ShippingRateTierType

if typing.TYPE_CHECKING:
    from .common import LastModifiedBy
    from .message import MessagesConfiguration, MessagesConfigurationDraft
    from .shipping_method import ShippingRateTierType
    from .type import CustomFieldLocalizedEnumValue

__all__ = [
    "BusinessUnitConfiguration",
    "BusinessUnitConfigurationStatus",
    "CartClassificationType",
    "CartScoreType",
    "CartValueType",
    "CartsConfiguration",
    "ExternalOAuth",
    "OrderSearchStatus",
    "Project",
    "ProjectChangeBusinessUnitStatusOnCreationAction",
    "ProjectChangeCartsConfigurationAction",
    "ProjectChangeCountriesAction",
    "ProjectChangeCountryTaxRateFallbackEnabledAction",
    "ProjectChangeCurrenciesAction",
    "ProjectChangeLanguagesAction",
    "ProjectChangeMessagesConfigurationAction",
    "ProjectChangeMessagesEnabledAction",
    "ProjectChangeNameAction",
    "ProjectChangeOrderSearchStatusAction",
    "ProjectChangeProductSearchIndexingEnabledAction",
    "ProjectChangeShoppingListsConfigurationAction",
    "ProjectSetExternalOAuthAction",
    "ProjectSetShippingRateInputTypeAction",
    "ProjectUpdate",
    "ProjectUpdateAction",
    "SearchIndexingConfiguration",
    "SearchIndexingConfigurationStatus",
    "SearchIndexingConfigurationValues",
    "ShippingRateInputType",
    "ShoppingListsConfiguration",
]


class BusinessUnitConfiguration(_BaseType):
    #: Status of Business Units created using the [My Business Unit endpoint](/../api/projects/me-business-units#create-businessunit).
    my_business_unit_status_on_creation: "BusinessUnitConfigurationStatus"

    def __init__(
        self, *, my_business_unit_status_on_creation: "BusinessUnitConfigurationStatus"
    ):
        self.my_business_unit_status_on_creation = my_business_unit_status_on_creation

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "BusinessUnitConfiguration":
        from ._schemas.project import BusinessUnitConfigurationSchema

        return BusinessUnitConfigurationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import BusinessUnitConfigurationSchema

        return BusinessUnitConfigurationSchema().dump(self)


class BusinessUnitConfigurationStatus(enum.Enum):
    """Default value for [Business Unit Status](ctp:api:type:BusinessUnitStatus) configured though [Project settings](/../api/projects/project#change-my-business-unit-status-on-creation)."""

    ACTIVE = "Active"
    INACTIVE = "Inactive"


class CartsConfiguration(_BaseType):
    #: Default value for the `deleteDaysAfterLastModification` parameter of the [CartDraft](ctp:api:type:CartDraft). This field may not be present on Projects created before January 2020.
    delete_days_after_last_modification: typing.Optional[int]
    #: Indicates if country _- no state_ Tax Rate fallback should be used when a shipping address state is not explicitly covered in the rates lists of all Tax Categories of a Cart Line Items. This field may not be present on Projects created before June 2020.
    country_tax_rate_fallback_enabled: typing.Optional[bool]

    def __init__(
        self,
        *,
        delete_days_after_last_modification: typing.Optional[int] = None,
        country_tax_rate_fallback_enabled: typing.Optional[bool] = None
    ):
        self.delete_days_after_last_modification = delete_days_after_last_modification
        self.country_tax_rate_fallback_enabled = country_tax_rate_fallback_enabled

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartsConfiguration":
        from ._schemas.project import CartsConfigurationSchema

        return CartsConfigurationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import CartsConfigurationSchema

        return CartsConfigurationSchema().dump(self)


class ExternalOAuth(_BaseType):
    """Represents a RFC 7662 compliant [OAuth 2.0 Token Introspection](https://datatracker.ietf.org/doc/html/rfc7662) endpoint. For more information, see [Requesting an access token using an external OAuth 2.0 server](/../api/authorization#requesting-an-access-token-using-an-external-oauth-server).

    You can only configure **one** external OAuth 2.0 endpoint per Project. To authenticate using multiple external services (such as social network logins), use a middle layer authentication service.

    """

    #: URL with authorization header.
    url: str
    #: Partially hidden on retrieval.
    authorization_header: str

    def __init__(self, *, url: str, authorization_header: str):
        self.url = url
        self.authorization_header = authorization_header

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ExternalOAuth":
        from ._schemas.project import ExternalOAuthSchema

        return ExternalOAuthSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ExternalOAuthSchema

        return ExternalOAuthSchema().dump(self)


class OrderSearchStatus(enum.Enum):
    """Specifies the status of the [Order Search](/../api/projects/order-search) index."""

    ACTIVATED = "Activated"
    DEACTIVATED = "Deactivated"


class Project(_BaseType):
    #: Current version of the Project.
    version: int
    #: User-defined unique identifier of the Project.
    key: str
    #: Name of the Project.
    name: str
    #: Country code of the geographic location.
    countries: typing.List["str"]
    #: Currency code of the country. A Project must have at least one currency.
    currencies: typing.List["str"]
    #: Language of the country. A Project must have at least one language.
    languages: typing.List["str"]
    #: Date and time (UTC) the Project was initially created.
    created_at: datetime.datetime
    #: Date in YYYY-MM format specifying when the trial period for the Project ends. Only present on Projects in trial period.
    trial_until: typing.Optional[str]
    #: Holds the configuration for the [Messages Query](/../api/projects/messages) feature.
    messages: "MessagesConfiguration"
    #: Holds the configuration for the [Carts](/../api/projects/carts) feature.
    carts: "CartsConfiguration"
    #: Holds the configuration for the [Shopping Lists](/../api/projects/shoppingLists) feature. This field may not be present on Projects created before January 2020.
    shopping_lists: typing.Optional["ShoppingListsConfiguration"]
    #: Holds the configuration for the [tiered shipping rates](ctp:api:type:ShippingRatePriceTier) feature.
    shipping_rate_input_type: typing.Optional["ShippingRateInputType"]
    #: Represents a RFC 7662 compliant [OAuth 2.0 Token Introspection](https://datatracker.ietf.org/doc/html/rfc7662) endpoint.
    external_o_auth: typing.Optional["ExternalOAuth"]
    #: Controls indexing of resources to be provided on high performance read-only search endpoints.
    search_indexing: typing.Optional["SearchIndexingConfiguration"]
    #: Holds configuration specific to [Business Units](ctp:api:type:BusinessUnit).
    business_units: typing.Optional["BusinessUnitConfiguration"]

    def __init__(
        self,
        *,
        version: int,
        key: str,
        name: str,
        countries: typing.List["str"],
        currencies: typing.List["str"],
        languages: typing.List["str"],
        created_at: datetime.datetime,
        trial_until: typing.Optional[str] = None,
        messages: "MessagesConfiguration",
        carts: "CartsConfiguration",
        shopping_lists: typing.Optional["ShoppingListsConfiguration"] = None,
        shipping_rate_input_type: typing.Optional["ShippingRateInputType"] = None,
        external_o_auth: typing.Optional["ExternalOAuth"] = None,
        search_indexing: typing.Optional["SearchIndexingConfiguration"] = None,
        business_units: typing.Optional["BusinessUnitConfiguration"] = None
    ):
        self.version = version
        self.key = key
        self.name = name
        self.countries = countries
        self.currencies = currencies
        self.languages = languages
        self.created_at = created_at
        self.trial_until = trial_until
        self.messages = messages
        self.carts = carts
        self.shopping_lists = shopping_lists
        self.shipping_rate_input_type = shipping_rate_input_type
        self.external_o_auth = external_o_auth
        self.search_indexing = search_indexing
        self.business_units = business_units

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Project":
        from ._schemas.project import ProjectSchema

        return ProjectSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectSchema

        return ProjectSchema().dump(self)


class ProjectUpdate(_BaseType):
    #: Expected version of the Project on which the changes should be applied. If the expected version does not match the actual version, a [409 Conflict](/../api/errors#409-conflict) will be returned.
    version: int
    #: Update actions to be performed on the Project.
    actions: typing.List["ProjectUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["ProjectUpdateAction"]):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProjectUpdate":
        from ._schemas.project import ProjectUpdateSchema

        return ProjectUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectUpdateSchema

        return ProjectUpdateSchema().dump(self)


class ProjectUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProjectUpdateAction":
        if data["action"] == "changeMyBusinessUnitStatusOnCreation":
            from ._schemas.project import (
                ProjectChangeBusinessUnitStatusOnCreationActionSchema,
            )

            return ProjectChangeBusinessUnitStatusOnCreationActionSchema().load(data)
        if data["action"] == "changeCartsConfiguration":
            from ._schemas.project import ProjectChangeCartsConfigurationActionSchema

            return ProjectChangeCartsConfigurationActionSchema().load(data)
        if data["action"] == "changeCountries":
            from ._schemas.project import ProjectChangeCountriesActionSchema

            return ProjectChangeCountriesActionSchema().load(data)
        if data["action"] == "changeCountryTaxRateFallbackEnabled":
            from ._schemas.project import (
                ProjectChangeCountryTaxRateFallbackEnabledActionSchema,
            )

            return ProjectChangeCountryTaxRateFallbackEnabledActionSchema().load(data)
        if data["action"] == "changeCurrencies":
            from ._schemas.project import ProjectChangeCurrenciesActionSchema

            return ProjectChangeCurrenciesActionSchema().load(data)
        if data["action"] == "changeLanguages":
            from ._schemas.project import ProjectChangeLanguagesActionSchema

            return ProjectChangeLanguagesActionSchema().load(data)
        if data["action"] == "changeMessagesConfiguration":
            from ._schemas.project import ProjectChangeMessagesConfigurationActionSchema

            return ProjectChangeMessagesConfigurationActionSchema().load(data)
        if data["action"] == "changeMessagesEnabled":
            from ._schemas.project import ProjectChangeMessagesEnabledActionSchema

            return ProjectChangeMessagesEnabledActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.project import ProjectChangeNameActionSchema

            return ProjectChangeNameActionSchema().load(data)
        if data["action"] == "changeOrderSearchStatus":
            from ._schemas.project import ProjectChangeOrderSearchStatusActionSchema

            return ProjectChangeOrderSearchStatusActionSchema().load(data)
        if data["action"] == "changeProductSearchIndexingEnabled":
            from ._schemas.project import (
                ProjectChangeProductSearchIndexingEnabledActionSchema,
            )

            return ProjectChangeProductSearchIndexingEnabledActionSchema().load(data)
        if data["action"] == "changeShoppingListsConfiguration":
            from ._schemas.project import (
                ProjectChangeShoppingListsConfigurationActionSchema,
            )

            return ProjectChangeShoppingListsConfigurationActionSchema().load(data)
        if data["action"] == "setExternalOAuth":
            from ._schemas.project import ProjectSetExternalOAuthActionSchema

            return ProjectSetExternalOAuthActionSchema().load(data)
        if data["action"] == "setShippingRateInputType":
            from ._schemas.project import ProjectSetShippingRateInputTypeActionSchema

            return ProjectSetShippingRateInputTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectUpdateActionSchema

        return ProjectUpdateActionSchema().dump(self)


class SearchIndexingConfiguration(_BaseType):
    """Controls indexing of resources to be provided on high performance read-only search endpoints."""

    #: Configuration for the [Product Projection Search](/../api/projects/products-search) and [Product Suggestions](/../api/projects/products-suggestions) endpoints.
    products: typing.Optional["SearchIndexingConfigurationValues"]
    #: Configuration for the [Order Search](/../api/projects/order-search) feature.
    orders: typing.Optional["SearchIndexingConfigurationValues"]

    def __init__(
        self,
        *,
        products: typing.Optional["SearchIndexingConfigurationValues"] = None,
        orders: typing.Optional["SearchIndexingConfigurationValues"] = None
    ):
        self.products = products
        self.orders = orders

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchIndexingConfiguration":
        from ._schemas.project import SearchIndexingConfigurationSchema

        return SearchIndexingConfigurationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import SearchIndexingConfigurationSchema

        return SearchIndexingConfigurationSchema().dump(self)


class SearchIndexingConfigurationStatus(enum.Enum):
    """Status of resource indexing."""

    ACTIVATED = "Activated"
    DEACTIVATED = "Deactivated"
    INDEXING = "Indexing"


class SearchIndexingConfigurationValues(_BaseType):
    #: Current status of resource indexing. Present on Projects from 1 February 2019.
    status: typing.Optional["SearchIndexingConfigurationStatus"]
    #: Date and time (UTC) the Project was last updated. Only present on Projects last modified after 1 February 2019.
    last_modified_at: typing.Optional[datetime.datetime]
    #: Present on resources created after 1 February 2019 except for [events not tracked](/../api/client-logging#events-tracked).
    last_modified_by: typing.Optional["LastModifiedBy"]

    def __init__(
        self,
        *,
        status: typing.Optional["SearchIndexingConfigurationStatus"] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None
    ):
        self.status = status
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "SearchIndexingConfigurationValues":
        from ._schemas.project import SearchIndexingConfigurationValuesSchema

        return SearchIndexingConfigurationValuesSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import SearchIndexingConfigurationValuesSchema

        return SearchIndexingConfigurationValuesSchema().dump(self)


class ShippingRateInputType(_BaseType):
    type: "ShippingRateTierType"

    def __init__(self, *, type: "ShippingRateTierType"):
        self.type = type

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ShippingRateInputType":
        if data["type"] == "CartClassification":
            from ._schemas.project import CartClassificationTypeSchema

            return CartClassificationTypeSchema().load(data)
        if data["type"] == "CartScore":
            from ._schemas.project import CartScoreTypeSchema

            return CartScoreTypeSchema().load(data)
        if data["type"] == "CartValue":
            from ._schemas.project import CartValueTypeSchema

            return CartValueTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ShippingRateInputTypeSchema

        return ShippingRateInputTypeSchema().dump(self)


class CartClassificationType(ShippingRateInputType):
    """Used when the ShippingRate maps to an abstract Cart categorization expressed by strings (for example, `Light`, `Medium`, or `Heavy`).
    Only keys defined in the `values` array can be used to create a tier or to set a value of the `shippingRateInput` on the [Cart](ctp:api:type:Cart).
    Keys must be unique.

    """

    #: The classification items that can be used for specifying any [ShippingRatePriceTier](ctp:api:type:ShippingRatePriceTier).
    values: typing.List["CustomFieldLocalizedEnumValue"]

    def __init__(self, *, values: typing.List["CustomFieldLocalizedEnumValue"]):
        self.values = values

        super().__init__(type=ShippingRateTierType.CART_CLASSIFICATION)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "CartClassificationType":
        from ._schemas.project import CartClassificationTypeSchema

        return CartClassificationTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import CartClassificationTypeSchema

        return CartClassificationTypeSchema().dump(self)


class CartScoreType(ShippingRateInputType):
    """Used when the ShippingRate maps to an abstract Cart categorization expressed by integers (such as shipping scores or weight ranges)."""

    def __init__(self):

        super().__init__(type=ShippingRateTierType.CART_SCORE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartScoreType":
        from ._schemas.project import CartScoreTypeSchema

        return CartScoreTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import CartScoreTypeSchema

        return CartScoreTypeSchema().dump(self)


class CartValueType(ShippingRateInputType):
    """Used when the ShippingRate maps to the sum of [LineItem](ctp:api:type:LineItem) Prices.
    The value of the Cart is used to select a tier.
    If chosen, it is not possible to set a value for the `shippingRateInput` on the [Cart](ctp:api:type:Cart).

    """

    def __init__(self):

        super().__init__(type=ShippingRateTierType.CART_VALUE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "CartValueType":
        from ._schemas.project import CartValueTypeSchema

        return CartValueTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import CartValueTypeSchema

        return CartValueTypeSchema().dump(self)


class ShoppingListsConfiguration(_BaseType):
    #: Default value for the `deleteDaysAfterLastModification` parameter of the [ShoppingListDraft](ctp:api:type:ShoppingListDraft).
    #: This field may not be present on Projects created before January 2020.
    delete_days_after_last_modification: typing.Optional[int]

    def __init__(
        self, *, delete_days_after_last_modification: typing.Optional[int] = None
    ):
        self.delete_days_after_last_modification = delete_days_after_last_modification

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ShoppingListsConfiguration":
        from ._schemas.project import ShoppingListsConfigurationSchema

        return ShoppingListsConfigurationSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ShoppingListsConfigurationSchema

        return ShoppingListsConfigurationSchema().dump(self)


class ProjectChangeBusinessUnitStatusOnCreationAction(ProjectUpdateAction):
    #: Status for Business Units created using the [My Business Unit endpoint](/../api/projects/me-business-units#create-businessunit).
    status: "BusinessUnitConfigurationStatus"

    def __init__(self, *, status: "BusinessUnitConfigurationStatus"):
        self.status = status

        super().__init__(action="changeMyBusinessUnitStatusOnCreation")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeBusinessUnitStatusOnCreationAction":
        from ._schemas.project import (
            ProjectChangeBusinessUnitStatusOnCreationActionSchema,
        )

        return ProjectChangeBusinessUnitStatusOnCreationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import (
            ProjectChangeBusinessUnitStatusOnCreationActionSchema,
        )

        return ProjectChangeBusinessUnitStatusOnCreationActionSchema().dump(self)


class ProjectChangeCartsConfigurationAction(ProjectUpdateAction):
    #: Configuration for the [Carts](/../api/projects/carts) feature.
    carts_configuration: "CartsConfiguration"

    def __init__(self, *, carts_configuration: "CartsConfiguration"):
        self.carts_configuration = carts_configuration

        super().__init__(action="changeCartsConfiguration")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeCartsConfigurationAction":
        from ._schemas.project import ProjectChangeCartsConfigurationActionSchema

        return ProjectChangeCartsConfigurationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeCartsConfigurationActionSchema

        return ProjectChangeCartsConfigurationActionSchema().dump(self)


class ProjectChangeCountriesAction(ProjectUpdateAction):
    #: New value to set. Must not be empty.
    countries: typing.List["str"]

    def __init__(self, *, countries: typing.List["str"]):
        self.countries = countries

        super().__init__(action="changeCountries")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeCountriesAction":
        from ._schemas.project import ProjectChangeCountriesActionSchema

        return ProjectChangeCountriesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeCountriesActionSchema

        return ProjectChangeCountriesActionSchema().dump(self)


class ProjectChangeCountryTaxRateFallbackEnabledAction(ProjectUpdateAction):
    #: When `true`, country _- no state_ Tax Rate is used as fallback. See [CartsConfiguration](ctp:api:type:CartsConfiguration).
    country_tax_rate_fallback_enabled: bool

    def __init__(self, *, country_tax_rate_fallback_enabled: bool):
        self.country_tax_rate_fallback_enabled = country_tax_rate_fallback_enabled

        super().__init__(action="changeCountryTaxRateFallbackEnabled")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeCountryTaxRateFallbackEnabledAction":
        from ._schemas.project import (
            ProjectChangeCountryTaxRateFallbackEnabledActionSchema,
        )

        return ProjectChangeCountryTaxRateFallbackEnabledActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import (
            ProjectChangeCountryTaxRateFallbackEnabledActionSchema,
        )

        return ProjectChangeCountryTaxRateFallbackEnabledActionSchema().dump(self)


class ProjectChangeCurrenciesAction(ProjectUpdateAction):
    #: New value to set. Must not be empty.
    currencies: typing.List["str"]

    def __init__(self, *, currencies: typing.List["str"]):
        self.currencies = currencies

        super().__init__(action="changeCurrencies")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeCurrenciesAction":
        from ._schemas.project import ProjectChangeCurrenciesActionSchema

        return ProjectChangeCurrenciesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeCurrenciesActionSchema

        return ProjectChangeCurrenciesActionSchema().dump(self)


class ProjectChangeLanguagesAction(ProjectUpdateAction):
    """If a language is used by a [Store](ctp:api:type:Store), it cannot be deleted. Attempts to delete such language will lead to [LanguageUsedInStores](/../api/errors#projects-400-language-used-in-stores) errors."""

    #: New value to set. Must not be empty.
    languages: typing.List["str"]

    def __init__(self, *, languages: typing.List["str"]):
        self.languages = languages

        super().__init__(action="changeLanguages")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeLanguagesAction":
        from ._schemas.project import ProjectChangeLanguagesActionSchema

        return ProjectChangeLanguagesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeLanguagesActionSchema

        return ProjectChangeLanguagesActionSchema().dump(self)


class ProjectChangeMessagesConfigurationAction(ProjectUpdateAction):
    #: Configuration for the [Messages Query](/../api/projects/messages) feature.
    messages_configuration: "MessagesConfigurationDraft"

    def __init__(self, *, messages_configuration: "MessagesConfigurationDraft"):
        self.messages_configuration = messages_configuration

        super().__init__(action="changeMessagesConfiguration")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeMessagesConfigurationAction":
        from ._schemas.project import ProjectChangeMessagesConfigurationActionSchema

        return ProjectChangeMessagesConfigurationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeMessagesConfigurationActionSchema

        return ProjectChangeMessagesConfigurationActionSchema().dump(self)


class ProjectChangeMessagesEnabledAction(ProjectUpdateAction):
    messages_enabled: bool

    def __init__(self, *, messages_enabled: bool):
        self.messages_enabled = messages_enabled

        super().__init__(action="changeMessagesEnabled")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeMessagesEnabledAction":
        from ._schemas.project import ProjectChangeMessagesEnabledActionSchema

        return ProjectChangeMessagesEnabledActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeMessagesEnabledActionSchema

        return ProjectChangeMessagesEnabledActionSchema().dump(self)


class ProjectChangeNameAction(ProjectUpdateAction):
    #: New value to set. Must not be empty.
    name: str

    def __init__(self, *, name: str):
        self.name = name

        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeNameAction":
        from ._schemas.project import ProjectChangeNameActionSchema

        return ProjectChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeNameActionSchema

        return ProjectChangeNameActionSchema().dump(self)


class ProjectChangeOrderSearchStatusAction(ProjectUpdateAction):
    #: Activates or deactivates the [Order Search](/../api/projects/order-search) feature. Activation will trigger building a search index for the Orders in the Project.
    status: "OrderSearchStatus"

    def __init__(self, *, status: "OrderSearchStatus"):
        self.status = status

        super().__init__(action="changeOrderSearchStatus")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeOrderSearchStatusAction":
        from ._schemas.project import ProjectChangeOrderSearchStatusActionSchema

        return ProjectChangeOrderSearchStatusActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectChangeOrderSearchStatusActionSchema

        return ProjectChangeOrderSearchStatusActionSchema().dump(self)


class ProjectChangeProductSearchIndexingEnabledAction(ProjectUpdateAction):
    #: If `false`, the indexing of [Product](ctp:api:type:Product) information will stop and the [Product Projection Search](/../api/projects/products-search) as well as the [Product Suggestions](/../api/projects/products-suggestions) endpoint will not be available anymore for this Project. The Project's [SearchIndexingConfiguration](ctp:api:type:SearchIndexingConfiguration) `status` for `products` will be changed to `"Deactivated"`.
    #:
    #: If `true`, the indexing of [Product](ctp:api:type:Product) information will start and the [Product Projection Search](/../api/projects/products-search) as well as the [Product Suggestions](/../api/projects/products-suggestions) endpoint will become available soon after for this Project. Proportional to the amount of information being indexed, the Project's [SearchIndexingConfiguration](ctp:api:type:SearchIndexingConfiguration) `status` for `products` will be shown as `"Indexing"` during this time. As soon as the indexing has finished, the configuration status will be changed to `"Activated"` making the aforementioned endpoints fully available for this Project.
    enabled: bool

    def __init__(self, *, enabled: bool):
        self.enabled = enabled

        super().__init__(action="changeProductSearchIndexingEnabled")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeProductSearchIndexingEnabledAction":
        from ._schemas.project import (
            ProjectChangeProductSearchIndexingEnabledActionSchema,
        )

        return ProjectChangeProductSearchIndexingEnabledActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import (
            ProjectChangeProductSearchIndexingEnabledActionSchema,
        )

        return ProjectChangeProductSearchIndexingEnabledActionSchema().dump(self)


class ProjectChangeShoppingListsConfigurationAction(ProjectUpdateAction):
    #: Configuration for the [Shopping Lists](/../api/projects/shoppingLists) feature.
    shopping_lists_configuration: "ShoppingListsConfiguration"

    def __init__(self, *, shopping_lists_configuration: "ShoppingListsConfiguration"):
        self.shopping_lists_configuration = shopping_lists_configuration

        super().__init__(action="changeShoppingListsConfiguration")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectChangeShoppingListsConfigurationAction":
        from ._schemas.project import (
            ProjectChangeShoppingListsConfigurationActionSchema,
        )

        return ProjectChangeShoppingListsConfigurationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import (
            ProjectChangeShoppingListsConfigurationActionSchema,
        )

        return ProjectChangeShoppingListsConfigurationActionSchema().dump(self)


class ProjectSetExternalOAuthAction(ProjectUpdateAction):
    #: Value to set. If empty, any existing value will be removed.
    external_o_auth: typing.Optional["ExternalOAuth"]

    def __init__(self, *, external_o_auth: typing.Optional["ExternalOAuth"] = None):
        self.external_o_auth = external_o_auth

        super().__init__(action="setExternalOAuth")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectSetExternalOAuthAction":
        from ._schemas.project import ProjectSetExternalOAuthActionSchema

        return ProjectSetExternalOAuthActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectSetExternalOAuthActionSchema

        return ProjectSetExternalOAuthActionSchema().dump(self)


class ProjectSetShippingRateInputTypeAction(ProjectUpdateAction):
    #: Value to set. If empty, any existing value will be removed.
    shipping_rate_input_type: typing.Optional["ShippingRateInputType"]

    def __init__(
        self,
        *,
        shipping_rate_input_type: typing.Optional["ShippingRateInputType"] = None
    ):
        self.shipping_rate_input_type = shipping_rate_input_type

        super().__init__(action="setShippingRateInputType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProjectSetShippingRateInputTypeAction":
        from ._schemas.project import ProjectSetShippingRateInputTypeActionSchema

        return ProjectSetShippingRateInputTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.project import ProjectSetShippingRateInputTypeActionSchema

        return ProjectSetShippingRateInputTypeActionSchema().dump(self)
