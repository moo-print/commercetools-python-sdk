# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    BaseResource,
    KeyReference,
    PagedQueryResponse,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import LocalizedString
__all__ = [
    "Store",
    "StoreDraft",
    "StoreKeyReference",
    "StorePagedQueryResponse",
    "StoreReference",
    "StoreResourceIdentifier",
    "StoreSetNameAction",
    "StoreUpdate",
    "StoreUpdateAction",
]


class Store(BaseResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        key: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.key = key
        self.name = name
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "Store(id=%r, version=%r, created_at=%r, last_modified_at=%r, key=%r, name=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.key,
                self.name,
            )
        )


class StoreDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreDraftSchema`."
    #: :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.key = key
        self.name = name
        super().__init__()

    def __repr__(self) -> str:
        return "StoreDraft(key=%r, name=%r)" % (self.key, self.name)


class StoreKeyReference(KeyReference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreKeyReferenceSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.STORE, key=key)

    def __repr__(self) -> str:
        return "StoreKeyReference(type_id=%r, key=%r)" % (self.type_id, self.key)


class StorePagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StorePagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.Store`
    results: typing.Optional[typing.Sequence["Store"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["Store"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return "StorePagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)" % (
            self.count,
            self.total,
            self.offset,
            self.results,
        )


class StoreReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreReferenceSchema`."
    #: Optional :class:`commercetools.types.Store`
    obj: typing.Optional["Store"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        obj: typing.Optional["Store"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.STORE, id=id)

    def __repr__(self) -> str:
        return "StoreReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class StoreResourceIdentifier(ResourceIdentifier):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreResourceIdentifierSchema`."

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.STORE, id=id, key=key)

    def __repr__(self) -> str:
        return "StoreResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class StoreUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreUpdateSchema`."
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
        return "StoreUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class StoreUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "StoreUpdateAction(action=%r)" % (self.action,)


class StoreSetNameAction(StoreUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.StoreSetNameActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.name = name
        super().__init__(action="setName")

    def __repr__(self) -> str:
        return "StoreSetNameAction(action=%r, name=%r)" % (self.action, self.name)
