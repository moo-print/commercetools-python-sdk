# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    LoggedResource,
    PagedQueryResponse,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._channel import ChannelResourceIdentifier
    from ._common import CreatedBy, LastModifiedBy
    from ._type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )
__all__ = [
    "InventoryAddQuantityAction",
    "InventoryChangeQuantityAction",
    "InventoryEntry",
    "InventoryEntryDraft",
    "InventoryEntryReference",
    "InventoryEntryResourceIdentifier",
    "InventoryPagedQueryResponse",
    "InventoryRemoveQuantityAction",
    "InventorySetCustomFieldAction",
    "InventorySetCustomTypeAction",
    "InventorySetExpectedDeliveryAction",
    "InventorySetRestockableInDaysAction",
    "InventorySetSupplyChannelAction",
    "InventoryUpdate",
    "InventoryUpdateAction",
]


class InventoryEntry(LoggedResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryEntrySchema`."
    #: :class:`str`
    sku: typing.Optional[str]
    #: Optional :class:`commercetools.types.ChannelResourceIdentifier` `(Named` ``supplyChannel`` `in Commercetools)`
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    #: :class:`int` `(Named` ``quantityOnStock`` `in Commercetools)`
    quantity_on_stock: typing.Optional[int]
    #: :class:`int` `(Named` ``availableQuantity`` `in Commercetools)`
    available_quantity: typing.Optional[int]
    #: Optional :class:`int` `(Named` ``restockableInDays`` `in Commercetools)`
    restockable_in_days: typing.Optional[int]
    #: Optional :class:`datetime.datetime` `(Named` ``expectedDelivery`` `in Commercetools)`
    expected_delivery: typing.Optional[datetime.datetime]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        sku: typing.Optional[str] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        quantity_on_stock: typing.Optional[int] = None,
        available_quantity: typing.Optional[int] = None,
        restockable_in_days: typing.Optional[int] = None,
        expected_delivery: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFields"] = None
    ) -> None:
        self.sku = sku
        self.supply_channel = supply_channel
        self.quantity_on_stock = quantity_on_stock
        self.available_quantity = available_quantity
        self.restockable_in_days = restockable_in_days
        self.expected_delivery = expected_delivery
        self.custom = custom
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
        )

    def __repr__(self) -> str:
        return (
            "InventoryEntry(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, sku=%r, supply_channel=%r, quantity_on_stock=%r, available_quantity=%r, restockable_in_days=%r, expected_delivery=%r, custom=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.sku,
                self.supply_channel,
                self.quantity_on_stock,
                self.available_quantity,
                self.restockable_in_days,
                self.expected_delivery,
                self.custom,
            )
        )


class InventoryEntryDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryEntryDraftSchema`."
    #: :class:`str`
    sku: typing.Optional[str]
    #: Optional :class:`commercetools.types.ChannelResourceIdentifier` `(Named` ``supplyChannel`` `in Commercetools)`
    supply_channel: typing.Optional["ChannelResourceIdentifier"]
    #: :class:`int` `(Named` ``quantityOnStock`` `in Commercetools)`
    quantity_on_stock: typing.Optional[int]
    #: Optional :class:`int` `(Named` ``restockableInDays`` `in Commercetools)`
    restockable_in_days: typing.Optional[int]
    #: Optional :class:`datetime.datetime` `(Named` ``expectedDelivery`` `in Commercetools)`
    expected_delivery: typing.Optional[datetime.datetime]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        sku: typing.Optional[str] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None,
        quantity_on_stock: typing.Optional[int] = None,
        restockable_in_days: typing.Optional[int] = None,
        expected_delivery: typing.Optional[datetime.datetime] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None
    ) -> None:
        self.sku = sku
        self.supply_channel = supply_channel
        self.quantity_on_stock = quantity_on_stock
        self.restockable_in_days = restockable_in_days
        self.expected_delivery = expected_delivery
        self.custom = custom
        super().__init__()

    def __repr__(self) -> str:
        return (
            "InventoryEntryDraft(sku=%r, supply_channel=%r, quantity_on_stock=%r, restockable_in_days=%r, expected_delivery=%r, custom=%r)"
            % (
                self.sku,
                self.supply_channel,
                self.quantity_on_stock,
                self.restockable_in_days,
                self.expected_delivery,
                self.custom,
            )
        )


class InventoryEntryReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryEntryReferenceSchema`."
    #: Optional :class:`commercetools.types.InventoryEntry`
    obj: typing.Optional["InventoryEntry"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        obj: typing.Optional["InventoryEntry"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.INVENTORY_ENTRY, id=id)

    def __repr__(self) -> str:
        return "InventoryEntryReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class InventoryEntryResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryEntryResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.INVENTORY_ENTRY, id=id, key=key)

    def __repr__(self) -> str:
        return "InventoryEntryResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class InventoryPagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryPagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.InventoryEntry`
    results: typing.Optional[typing.Sequence["InventoryEntry"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["InventoryEntry"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return (
            "InventoryPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


class InventoryUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryUpdateSchema`."
    #: :class:`int`
    version: typing.Optional[int]
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None
    ) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "InventoryUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class InventoryUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "InventoryUpdateAction(action=%r)" % (self.action,)


class InventoryAddQuantityAction(InventoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryAddQuantityActionSchema`."
    #: :class:`int`
    quantity: typing.Optional[int]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        quantity: typing.Optional[int] = None
    ) -> None:
        self.quantity = quantity
        super().__init__(action="addQuantity")

    def __repr__(self) -> str:
        return "InventoryAddQuantityAction(action=%r, quantity=%r)" % (
            self.action,
            self.quantity,
        )


class InventoryChangeQuantityAction(InventoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryChangeQuantityActionSchema`."
    #: :class:`int`
    quantity: typing.Optional[int]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        quantity: typing.Optional[int] = None
    ) -> None:
        self.quantity = quantity
        super().__init__(action="changeQuantity")

    def __repr__(self) -> str:
        return "InventoryChangeQuantityAction(action=%r, quantity=%r)" % (
            self.action,
            self.quantity,
        )


class InventoryRemoveQuantityAction(InventoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventoryRemoveQuantityActionSchema`."
    #: :class:`int`
    quantity: typing.Optional[int]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        quantity: typing.Optional[int] = None
    ) -> None:
        self.quantity = quantity
        super().__init__(action="removeQuantity")

    def __repr__(self) -> str:
        return "InventoryRemoveQuantityAction(action=%r, quantity=%r)" % (
            self.action,
            self.quantity,
        )


class InventorySetCustomFieldAction(InventoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventorySetCustomFieldActionSchema`."
    #: :class:`str`
    name: typing.Optional[str]
    #: Optional :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        value: typing.Optional[typing.Any] = None
    ) -> None:
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    def __repr__(self) -> str:
        return "InventorySetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


class InventorySetCustomTypeAction(InventoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventorySetCustomTypeActionSchema`."
    #: Optional :class:`commercetools.types.TypeResourceIdentifier`
    type: typing.Optional["TypeResourceIdentifier"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        type: typing.Optional["TypeResourceIdentifier"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    def __repr__(self) -> str:
        return "InventorySetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


class InventorySetExpectedDeliveryAction(InventoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventorySetExpectedDeliveryActionSchema`."
    #: Optional :class:`datetime.datetime` `(Named` ``expectedDelivery`` `in Commercetools)`
    expected_delivery: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        expected_delivery: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.expected_delivery = expected_delivery
        super().__init__(action="setExpectedDelivery")

    def __repr__(self) -> str:
        return "InventorySetExpectedDeliveryAction(action=%r, expected_delivery=%r)" % (
            self.action,
            self.expected_delivery,
        )


class InventorySetRestockableInDaysAction(InventoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventorySetRestockableInDaysActionSchema`."
    #: Optional :class:`int` `(Named` ``restockableInDays`` `in Commercetools)`
    restockable_in_days: typing.Optional[int]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        restockable_in_days: typing.Optional[int] = None
    ) -> None:
        self.restockable_in_days = restockable_in_days
        super().__init__(action="setRestockableInDays")

    def __repr__(self) -> str:
        return (
            "InventorySetRestockableInDaysAction(action=%r, restockable_in_days=%r)"
            % (self.action, self.restockable_in_days)
        )


class InventorySetSupplyChannelAction(InventoryUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.InventorySetSupplyChannelActionSchema`."
    #: Optional :class:`commercetools.types.ChannelResourceIdentifier` `(Named` ``supplyChannel`` `in Commercetools)`
    supply_channel: typing.Optional["ChannelResourceIdentifier"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        supply_channel: typing.Optional["ChannelResourceIdentifier"] = None
    ) -> None:
        self.supply_channel = supply_channel
        super().__init__(action="setSupplyChannel")

    def __repr__(self) -> str:
        return "InventorySetSupplyChannelAction(action=%r, supply_channel=%r)" % (
            self.action,
            self.supply_channel,
        )
