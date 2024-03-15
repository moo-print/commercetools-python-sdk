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
from .cart import InventoryMode, RoundingMode, TaxCalculationMode, TaxMode
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .business_unit import BusinessUnitKeyReference
    from .cart import (
        CustomLineItem,
        DirectDiscount,
        InventoryMode,
        LineItem,
        RoundingMode,
        ShippingInfo,
        ShippingRateInput,
        TaxCalculationMode,
        TaxedPrice,
        TaxMode,
    )
    from .common import Address, CreatedBy, LastModifiedBy, ReferenceTypeId, TypedMoney
    from .customer import CustomerReference, CustomerResourceIdentifier
    from .customer_group import CustomerGroupReference
    from .order import PaymentInfo
    from .quote_request import QuoteRequestReference
    from .staged_quote import StagedQuoteReference, StagedQuoteResourceIdentifier
    from .state import StateReference, StateResourceIdentifier
    from .store import StoreKeyReference
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "Quote",
    "QuoteChangeCustomerAction",
    "QuoteChangeQuoteStateAction",
    "QuoteDraft",
    "QuotePagedQueryResponse",
    "QuoteReference",
    "QuoteRequestQuoteRenegotiationAction",
    "QuoteResourceIdentifier",
    "QuoteSetCustomFieldAction",
    "QuoteSetCustomTypeAction",
    "QuoteState",
    "QuoteTransitionStateAction",
    "QuoteUpdate",
    "QuoteUpdateAction",
]


class Quote(BaseResource):
    #: User-defined unique identifier of the Quote.
    key: typing.Optional[str]
    #: Present on resources created after 1 February 2019 except for [events not tracked](/../api/general-concepts#events-tracked).
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1 February 2019 except for [events not tracked](/../api/general-concepts#events-tracked).
    created_by: typing.Optional["CreatedBy"]
    #: Quote Request related to the Quote.
    quote_request: "QuoteRequestReference"
    #: Staged Quote related to the Quote.
    staged_quote: "StagedQuoteReference"
    #: The [Buyer](/../api/quotes-overview#buyer) who owns the Quote.
    customer: typing.Optional["CustomerReference"]
    #: Set automatically when `customer` is set and the Customer is a member of a Customer Group.
    #: Not updated if Customer is changed after Quote creation.
    #: Used for Product Variant price selection.
    customer_group: typing.Optional["CustomerGroupReference"]
    #: Expiration date for the Quote.
    valid_to: typing.Optional[datetime.datetime]
    #: Message from the [Seller](/../api/quotes-overview#seller) included in the offer.
    seller_comment: typing.Optional[str]
    #: Message from the [Buyer](/../api/quotes-overview#buyer) included in the [renegotiation request](ctp:api:type:QuoteRequestQuoteRenegotiationAction).
    buyer_comment: typing.Optional[str]
    #: The Store to which the [Buyer](/../api/quotes-overview#buyer) belongs.
    store: typing.Optional["StoreKeyReference"]
    #: The Line Items for which the Quote is requested.
    line_items: typing.List["LineItem"]
    #: The Custom Line Items for which the Quote is requested.
    custom_line_items: typing.List["CustomLineItem"]
    #: Sum of all `totalPrice` fields of the `lineItems` and `customLineItems`, as well as the `price` field of `shippingInfo` (if it exists).
    #: `totalPrice` may or may not include the taxes: it depends on the taxRate.includedInPrice property of each price.
    total_price: "TypedMoney"
    #: Not set until the shipping address is set.
    #: Will be set automatically in the `Platform` TaxMode.
    #: For the `External` tax mode it will be set  as soon as the external tax rates for all line items, custom line items, and shipping in the cart are set.
    taxed_price: typing.Optional["TaxedPrice"]
    #: Used to determine the eligible [ShippingMethods](ctp:api:type:ShippingMethod)
    #: and rates as well as the tax rate of the Line Items.
    shipping_address: typing.Optional["Address"]
    #: Address used for invoicing.
    billing_address: typing.Optional["Address"]
    #: Inventory mode of the Cart referenced in the [QuoteRequestDraft](ctp:api:type:QuoteRequestDraft).
    inventory_mode: typing.Optional["InventoryMode"]
    #: Tax mode of the Cart referenced in the [QuoteRequestDraft](ctp:api:type:QuoteRequestDraft).
    tax_mode: "TaxMode"
    #: When calculating taxes for `taxedPrice`, the selected mode is used for rounding.
    tax_rounding_mode: "RoundingMode"
    #: When calculating taxes for `taxedPrice`, the selected mode is used for calculating the price with `LineItemLevel` (horizontally) or `UnitPriceLevel` (vertically) calculation mode.
    tax_calculation_mode: "TaxCalculationMode"
    #: Used for Product Variant price selection.
    country: typing.Optional[str]
    #: Set automatically once the [ShippingMethod](ctp:api:type:ShippingMethod) is set.
    shipping_info: typing.Optional["ShippingInfo"]
    #: Log of payment transactions related to the Quote.
    payment_info: typing.Optional["PaymentInfo"]
    #: Used to select a [ShippingRatePriceTier](ctp:api:type:ShippingRatePriceTier).
    shipping_rate_input: typing.Optional["ShippingRateInput"]
    #: Contains addresses for carts with multiple shipping addresses.
    #: Line items reference these addresses under their `shippingDetails`.
    #: The addresses captured here are not used to determine eligible shipping methods or the applicable tax rate.
    #: Only the cart's `shippingAddress` is used for this.
    item_shipping_addresses: typing.Optional[typing.List["Address"]]
    #: Discounts that are only valid for the Quote and cannot be associated to any other Cart or Order.
    direct_discounts: typing.Optional[typing.List["DirectDiscount"]]
    #: Custom Fields on the Quote.
    custom: typing.Optional["CustomFields"]
    #: Predefined states tracking the status of the Quote.
    quote_state: "QuoteState"
    #: [State](ctp:api:type:State) of the Quote.
    #: This reference can point to a State in a custom workflow.
    state: typing.Optional["StateReference"]
    #: The Purchase Order Number is typically set by the [Buyer](/quotes-overview#buyer) on a [QuoteRequest](ctp:api:type:QuoteRequest) to
    #: track the purchase order during the [quote and order flow](/../api/quotes-overview#intended-workflow).
    purchase_order_number: typing.Optional[str]
    #: The [BusinessUnit](ctp:api:type:BusinessUnit) for the Quote.
    business_unit: typing.Optional["BusinessUnitKeyReference"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        key: typing.Optional[str] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        quote_request: "QuoteRequestReference",
        staged_quote: "StagedQuoteReference",
        customer: typing.Optional["CustomerReference"] = None,
        customer_group: typing.Optional["CustomerGroupReference"] = None,
        valid_to: typing.Optional[datetime.datetime] = None,
        seller_comment: typing.Optional[str] = None,
        buyer_comment: typing.Optional[str] = None,
        store: typing.Optional["StoreKeyReference"] = None,
        line_items: typing.List["LineItem"],
        custom_line_items: typing.List["CustomLineItem"],
        total_price: "TypedMoney",
        taxed_price: typing.Optional["TaxedPrice"] = None,
        shipping_address: typing.Optional["Address"] = None,
        billing_address: typing.Optional["Address"] = None,
        inventory_mode: typing.Optional["InventoryMode"] = None,
        tax_mode: "TaxMode",
        tax_rounding_mode: "RoundingMode",
        tax_calculation_mode: "TaxCalculationMode",
        country: typing.Optional[str] = None,
        shipping_info: typing.Optional["ShippingInfo"] = None,
        payment_info: typing.Optional["PaymentInfo"] = None,
        shipping_rate_input: typing.Optional["ShippingRateInput"] = None,
        item_shipping_addresses: typing.Optional[typing.List["Address"]] = None,
        direct_discounts: typing.Optional[typing.List["DirectDiscount"]] = None,
        custom: typing.Optional["CustomFields"] = None,
        quote_state: "QuoteState",
        state: typing.Optional["StateReference"] = None,
        purchase_order_number: typing.Optional[str] = None,
        business_unit: typing.Optional["BusinessUnitKeyReference"] = None
    ):
        self.key = key
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.quote_request = quote_request
        self.staged_quote = staged_quote
        self.customer = customer
        self.customer_group = customer_group
        self.valid_to = valid_to
        self.seller_comment = seller_comment
        self.buyer_comment = buyer_comment
        self.store = store
        self.line_items = line_items
        self.custom_line_items = custom_line_items
        self.total_price = total_price
        self.taxed_price = taxed_price
        self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.inventory_mode = inventory_mode
        self.tax_mode = tax_mode
        self.tax_rounding_mode = tax_rounding_mode
        self.tax_calculation_mode = tax_calculation_mode
        self.country = country
        self.shipping_info = shipping_info
        self.payment_info = payment_info
        self.shipping_rate_input = shipping_rate_input
        self.item_shipping_addresses = item_shipping_addresses
        self.direct_discounts = direct_discounts
        self.custom = custom
        self.quote_state = quote_state
        self.state = state
        self.purchase_order_number = purchase_order_number
        self.business_unit = business_unit

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "Quote":
        from ._schemas.quote import QuoteSchema

        return QuoteSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteSchema

        return QuoteSchema().dump(self)


class QuoteDraft(_BaseType):
    #: User-defined unique identifier for the Quote.
    key: typing.Optional[str]
    #: StagedQuote from which the Quote is created.
    staged_quote: "StagedQuoteResourceIdentifier"
    #: Current version of the StagedQuote.
    staged_quote_version: int
    #: If `true`, the `stagedQuoteState` of the referenced [StagedQuote](/../api/projects/staged-quotes#stagedquote) will be set to `Sent`.
    staged_quote_state_to_sent: typing.Optional[bool]
    #: [State](ctp:api:type:State) of the Quote.
    #: This reference can point to a State in a custom workflow.
    state: typing.Optional["StateReference"]
    #: [Custom Fields](/../api/projects/custom-fields) to be added to the Quote.
    #:
    #: - If specified, the Custom Fields are merged with the Custom Fields on the referenced [StagedQuote](/../api/projects/staged-quotes#stagedquote) and added to the Quote.
    #: - If empty, the Custom Fields on the referenced [StagedQuote](/../api/projects/staged-quotes#stagedquote) are added to the Quote automatically.
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        staged_quote: "StagedQuoteResourceIdentifier",
        staged_quote_version: int,
        staged_quote_state_to_sent: typing.Optional[bool] = None,
        state: typing.Optional["StateReference"] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.key = key
        self.staged_quote = staged_quote
        self.staged_quote_version = staged_quote_version
        self.staged_quote_state_to_sent = staged_quote_state_to_sent
        self.state = state
        self.custom = custom

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QuoteDraft":
        from ._schemas.quote import QuoteDraftSchema

        return QuoteDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteDraftSchema

        return QuoteDraftSchema().dump(self)


class QuotePagedQueryResponse(_BaseType):
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with results containing an array of [Quote](ctp:api:type:Quote)."""

    #: Number of [results requested](/../api/general-concepts#limit).
    limit: int
    #: Number of [elements skipped](/../api/general-concepts#offset).
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/../api/general-concepts#strong-consistency).
    #: This field is returned by default.
    #: For improved performance, calculating this field can be deactivated by using the query parameter `withTotal=false`.
    #: When the results are filtered with a [Query Predicate](/../api/predicates/query), `total` is subject to a [limit](/../api/limits#queries).
    total: typing.Optional[int]
    #: Quotes matching the query.
    results: typing.List["Quote"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["Quote"]
    ):
        self.limit = limit
        self.offset = offset
        self.count = count
        self.total = total
        self.results = results

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuotePagedQueryResponse":
        from ._schemas.quote import QuotePagedQueryResponseSchema

        return QuotePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuotePagedQueryResponseSchema

        return QuotePagedQueryResponseSchema().dump(self)


class QuoteReference(Reference):
    """[Reference](ctp:api:type:Reference) to a [Quote](ctp:api:type:Quote)."""

    #: Contains the representation of the expanded Quote.
    #: Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for Quote.
    obj: typing.Optional["Quote"]

    def __init__(self, *, id: str, obj: typing.Optional["Quote"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.QUOTE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QuoteReference":
        from ._schemas.quote import QuoteReferenceSchema

        return QuoteReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteReferenceSchema

        return QuoteReferenceSchema().dump(self)


class QuoteResourceIdentifier(ResourceIdentifier):
    """[ResourceIdentifier](ctp:api:type:ResourceIdentifier) to a [Quote](ctp:api:type:Quote)."""

    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.QUOTE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteResourceIdentifier":
        from ._schemas.quote import QuoteResourceIdentifierSchema

        return QuoteResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteResourceIdentifierSchema

        return QuoteResourceIdentifierSchema().dump(self)


class QuoteState(enum.Enum):
    """Predefined states tracking the status of the Quote."""

    PENDING = "Pending"
    DECLINED = "Declined"
    DECLINED_FOR_RENEGOTIATION = "DeclinedForRenegotiation"
    RENEGOTIATION_ADDRESSED = "RenegotiationAddressed"
    ACCEPTED = "Accepted"
    WITHDRAWN = "Withdrawn"


class QuoteUpdate(_BaseType):
    #: Expected version of the [Quote](ctp:api:type:Quote) to which the changes should be applied.
    #: If the expected version does not match the actual version, a [ConcurrentModification](ctp:api:type:ConcurrentModificationError) error will be returned.
    version: int
    #: Update actions to be performed on the [Quote](ctp:api:type:Quote).
    actions: typing.List["QuoteUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["QuoteUpdateAction"]):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QuoteUpdate":
        from ._schemas.quote import QuoteUpdateSchema

        return QuoteUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteUpdateSchema

        return QuoteUpdateSchema().dump(self)


class QuoteUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "QuoteUpdateAction":
        if data["action"] == "changeCustomer":
            from ._schemas.quote import QuoteChangeCustomerActionSchema

            return QuoteChangeCustomerActionSchema().load(data)
        if data["action"] == "changeQuoteState":
            from ._schemas.quote import QuoteChangeQuoteStateActionSchema

            return QuoteChangeQuoteStateActionSchema().load(data)
        if data["action"] == "requestQuoteRenegotiation":
            from ._schemas.quote import QuoteRequestQuoteRenegotiationActionSchema

            return QuoteRequestQuoteRenegotiationActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.quote import QuoteSetCustomFieldActionSchema

            return QuoteSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.quote import QuoteSetCustomTypeActionSchema

            return QuoteSetCustomTypeActionSchema().load(data)
        if data["action"] == "transitionState":
            from ._schemas.quote import QuoteTransitionStateActionSchema

            return QuoteTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteUpdateActionSchema

        return QuoteUpdateActionSchema().dump(self)


class QuoteChangeCustomerAction(QuoteUpdateAction):
    """Changes the owner of a Quote to a different Customer.
    Customer Group is not updated.
    This update action produces the [Quote Customer Changed](ctp:api:type:QuoteCustomerChangedMessage) Message.

    """

    #: New Customer to own the Quote.
    customer: "CustomerResourceIdentifier"

    def __init__(self, *, customer: "CustomerResourceIdentifier"):
        self.customer = customer

        super().__init__(action="changeCustomer")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteChangeCustomerAction":
        from ._schemas.quote import QuoteChangeCustomerActionSchema

        return QuoteChangeCustomerActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteChangeCustomerActionSchema

        return QuoteChangeCustomerActionSchema().dump(self)


class QuoteChangeQuoteStateAction(QuoteUpdateAction):
    #: New state to be set for the Quote.
    quote_state: "QuoteState"

    def __init__(self, *, quote_state: "QuoteState"):
        self.quote_state = quote_state

        super().__init__(action="changeQuoteState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteChangeQuoteStateAction":
        from ._schemas.quote import QuoteChangeQuoteStateActionSchema

        return QuoteChangeQuoteStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteChangeQuoteStateActionSchema

        return QuoteChangeQuoteStateActionSchema().dump(self)


class QuoteRequestQuoteRenegotiationAction(QuoteUpdateAction):
    """Represents the Buyer requesting renegotiation for a Quote. Valid for Quotes in a `Pending` [state](ctp:api:type:QuoteState)."""

    #: Message from the [Buyer](/api/quotes-overview#buyer) regarding the Quote renegotiation request.
    buyer_comment: typing.Optional[str]

    def __init__(self, *, buyer_comment: typing.Optional[str] = None):
        self.buyer_comment = buyer_comment

        super().__init__(action="requestQuoteRenegotiation")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteRequestQuoteRenegotiationAction":
        from ._schemas.quote import QuoteRequestQuoteRenegotiationActionSchema

        return QuoteRequestQuoteRenegotiationActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteRequestQuoteRenegotiationActionSchema

        return QuoteRequestQuoteRenegotiationActionSchema().dump(self)


class QuoteSetCustomFieldAction(QuoteUpdateAction):
    #: Name of the [Custom Field](/../api/projects/custom-fields).
    name: str
    #: If `value` is absent or `null`, this field will be removed if it exists.
    #: Removing a field that does not exist returns an [InvalidOperation](ctp:api:type:InvalidOperationError) error.
    #: If `value` is provided, it is set for the field defined by `name`.
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value

        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteSetCustomFieldAction":
        from ._schemas.quote import QuoteSetCustomFieldActionSchema

        return QuoteSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteSetCustomFieldActionSchema

        return QuoteSetCustomFieldActionSchema().dump(self)


class QuoteSetCustomTypeAction(QuoteUpdateAction):
    #: Defines the [Type](ctp:api:type:Type) that extends the Quote with [Custom Fields](/../api/projects/custom-fields).
    #: If absent, any existing Type and Custom Fields are removed from the Quote.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](/../api/projects/custom-fields) fields for the Quote.
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ):
        self.type = type
        self.fields = fields

        super().__init__(action="setCustomType")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteSetCustomTypeAction":
        from ._schemas.quote import QuoteSetCustomTypeActionSchema

        return QuoteSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteSetCustomTypeActionSchema

        return QuoteSetCustomTypeActionSchema().dump(self)


class QuoteTransitionStateAction(QuoteUpdateAction):
    """If the existing [State](ctp:api:type:State) has set `transitions`, there must be a direct transition to the new State. If `transitions` is not set, no validation is performed. This update action produces the [Quote State Transition](ctp:api:type:QuoteStateTransitionMessage) Message."""

    #: Value to set.
    #: If there is no State yet, this must be an initial State.
    state: "StateResourceIdentifier"
    #: Switch validations on or off.
    force: typing.Optional[bool]

    def __init__(
        self, *, state: "StateResourceIdentifier", force: typing.Optional[bool] = None
    ):
        self.state = state
        self.force = force

        super().__init__(action="transitionState")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "QuoteTransitionStateAction":
        from ._schemas.quote import QuoteTransitionStateActionSchema

        return QuoteTransitionStateActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.quote import QuoteTransitionStateActionSchema

        return QuoteTransitionStateActionSchema().dump(self)
