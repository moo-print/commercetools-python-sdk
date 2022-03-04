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
from .common import BaseResource, Reference, ReferenceTypeId, ResourceIdentifier

if typing.TYPE_CHECKING:
    from .common import CreatedBy, LastModifiedBy, LocalizedString, ReferenceTypeId
    from .product import ProductReference, ProductResourceIdentifier
    from .type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )

__all__ = [
    "AssignedProductReference",
    "AssignedProductSelection",
    "AssignedProductSelectionPagedQueryResponse",
    "IndividualProductSelectionType",
    "ProductSelection",
    "ProductSelectionAddProductAction",
    "ProductSelectionAssignment",
    "ProductSelectionChangeNameAction",
    "ProductSelectionDraft",
    "ProductSelectionPagedQueryResponse",
    "ProductSelectionProductPagedQueryResponse",
    "ProductSelectionReference",
    "ProductSelectionRemoveProductAction",
    "ProductSelectionResourceIdentifier",
    "ProductSelectionSetCustomFieldAction",
    "ProductSelectionSetCustomTypeAction",
    "ProductSelectionSetKeyAction",
    "ProductSelectionType",
    "ProductSelectionTypeEnum",
    "ProductSelectionUpdate",
    "ProductSelectionUpdateAction",
    "ProductsInStorePagedQueryResponse",
]


class AssignedProductReference(_BaseType):
    #: Reference to a Product that is assigned to the Product Selection.
    product: "ProductReference"

    def __init__(self, *, product: "ProductReference"):
        self.product = product

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssignedProductReference":
        from ._schemas.product_selection import AssignedProductReferenceSchema

        return AssignedProductReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import AssignedProductReferenceSchema

        return AssignedProductReferenceSchema().dump(self)


class AssignedProductSelection(_BaseType):
    #: Reference to the Product Selection that this assignment is part of.
    product_selection: "ProductSelectionReference"

    def __init__(self, *, product_selection: "ProductSelectionReference"):
        self.product_selection = product_selection

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "AssignedProductSelection":
        from ._schemas.product_selection import AssignedProductSelectionSchema

        return AssignedProductSelectionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import AssignedProductSelectionSchema

        return AssignedProductSelectionSchema().dump(self)


class AssignedProductSelectionPagedQueryResponse(_BaseType):
    """[PagedQueryResult](/general-concepts#pagedqueryresult) containing an array of [AssignedProductSelection](ctp:api:type:AssignedProductSelection)."""

    #: Number of results requested in the query request.
    limit: int
    #: Offset supplied by the client or the server default.
    #: It is the number of elements skipped, not a page number.
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/general-concepts#strong-consistency).
    #: Unlike other endpoints, the Product Selection endpoint does not return this field by default.
    #: To get `total`, pass the query parameter `withTotal` set to `true`.
    #: When the results are filtered with a [Query Predicate](/predicates/query), `total` is subject to a [limit](/limits#queries).
    total: typing.Optional[int]
    #: References to Product Selection that are assigned to the Product.
    results: typing.List["AssignedProductSelection"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["AssignedProductSelection"]
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
    ) -> "AssignedProductSelectionPagedQueryResponse":
        from ._schemas.product_selection import (
            AssignedProductSelectionPagedQueryResponseSchema,
        )

        return AssignedProductSelectionPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import (
            AssignedProductSelectionPagedQueryResponseSchema,
        )

        return AssignedProductSelectionPagedQueryResponseSchema().dump(self)


class ProductSelection(BaseResource):
    #: Present on resources updated after 1/02/2019 except for events not
    #: tracked.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Present on resources created after 1/02/2019 except for events not
    #: tracked.
    created_by: typing.Optional["CreatedBy"]
    #: User-defined unique identifier for the Product Selection.
    key: typing.Optional[str]
    #: Name of the Product Selection.
    name: "LocalizedString"
    #: Number of Products that are currently assigned to this Product Selection.
    product_count: int
    #: Specifies in which way the Products are assigned to the Product Selection. Currently, the only way of doing this is to specify each Product individually. Hence, the type is fixed to `individual` for now, but we have plans to add other types in the future.
    type: "ProductSelectionTypeEnum"
    #: Custom Fields of this Product Selection.
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        name: "LocalizedString",
        product_count: int,
        type: "ProductSelectionTypeEnum",
        custom: typing.Optional["CustomFields"] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.product_count = product_count
        self.type = type
        self.custom = custom

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductSelection":
        from ._schemas.product_selection import ProductSelectionSchema

        return ProductSelectionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionSchema

        return ProductSelectionSchema().dump(self)


class ProductSelectionAssignment(_BaseType):
    """Specifies which Product is assigned to which Product Selection."""

    #: Reference to a Product that is assigned to the Product Selection.
    product: "ProductReference"
    #: Reference to the Product Selection that this assignment is part of.
    product_selection: "ProductSelectionReference"

    def __init__(
        self,
        *,
        product: "ProductReference",
        product_selection: "ProductSelectionReference"
    ):
        self.product = product
        self.product_selection = product_selection

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionAssignment":
        from ._schemas.product_selection import ProductSelectionAssignmentSchema

        return ProductSelectionAssignmentSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionAssignmentSchema

        return ProductSelectionAssignmentSchema().dump(self)


class ProductSelectionDraft(_BaseType):
    #: User-defined unique identifier for the Product Selection. You can use `key` besides `ID` to reference the Product Selection.
    key: typing.Optional[str]
    #: Name of the Product Selection. Not checked for uniqueness, but distinct names are recommended.
    name: "LocalizedString"
    #: Custom Fields of this Product Selection.
    custom: typing.Optional["CustomFieldsDraft"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        name: "LocalizedString",
        custom: typing.Optional["CustomFieldsDraft"] = None
    ):
        self.key = key
        self.name = name
        self.custom = custom

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductSelectionDraft":
        from ._schemas.product_selection import ProductSelectionDraftSchema

        return ProductSelectionDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionDraftSchema

        return ProductSelectionDraftSchema().dump(self)


class ProductSelectionPagedQueryResponse(_BaseType):
    """[PagedQueryResult](/general-concepts#pagedqueryresult) containing an array of [ProductSelection](ctp:api:type:ProductSelection)."""

    #: Number of results requested in the query request.
    limit: int
    #: Offset supplied by the client or the server default.
    #: It is the number of elements skipped, not a page number.
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/general-concepts#strong-consistency).
    #: Unlike other endpoints, the Product Selection endpoint does not return this field by default.
    #: To get `total`, pass the query parameter `withTotal` set to `true`.
    #: When the results are filtered with a [Query Predicate](/predicates/query), `total` is subject to a [limit](/limits#queries).
    total: typing.Optional[int]
    #: The Product Selections matching the query.
    results: typing.List["ProductSelection"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["ProductSelection"]
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
    ) -> "ProductSelectionPagedQueryResponse":
        from ._schemas.product_selection import ProductSelectionPagedQueryResponseSchema

        return ProductSelectionPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionPagedQueryResponseSchema

        return ProductSelectionPagedQueryResponseSchema().dump(self)


class ProductSelectionProductPagedQueryResponse(_BaseType):
    """[PagedQueryResult](/general-concepts#pagedqueryresult) containing an array of [AssignedProductReference](ctp:api:type:AssignedProductReference)."""

    #: Number of results requested in the query request.
    limit: int
    #: Offset supplied by the client or the server default.
    #: It is the number of elements skipped, not a page number.
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/general-concepts#strong-consistency).
    #: Unlike other endpoints, the Product Selection endpoint does not return this field by default.
    #: To get `total`, pass the query parameter `withTotal` set to `true`.
    #: When the results are filtered with a [Query Predicate](/predicates/query), `total` is subject to a [limit](/limits#queries).
    total: typing.Optional[int]
    #: References to Products that are assigned to the Product Selection.
    results: typing.List["AssignedProductReference"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["AssignedProductReference"]
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
    ) -> "ProductSelectionProductPagedQueryResponse":
        from ._schemas.product_selection import (
            ProductSelectionProductPagedQueryResponseSchema,
        )

        return ProductSelectionProductPagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import (
            ProductSelectionProductPagedQueryResponseSchema,
        )

        return ProductSelectionProductPagedQueryResponseSchema().dump(self)


class ProductSelectionReference(Reference):
    #: Contains the representation of the expanded Product Selection. Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for Product Selection.
    obj: typing.Optional["ProductSelection"]

    def __init__(self, *, id: str, obj: typing.Optional["ProductSelection"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.PRODUCT_SELECTION)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionReference":
        from ._schemas.product_selection import ProductSelectionReferenceSchema

        return ProductSelectionReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionReferenceSchema

        return ProductSelectionReferenceSchema().dump(self)


class ProductSelectionResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.PRODUCT_SELECTION)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionResourceIdentifier":
        from ._schemas.product_selection import ProductSelectionResourceIdentifierSchema

        return ProductSelectionResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionResourceIdentifierSchema

        return ProductSelectionResourceIdentifierSchema().dump(self)


class ProductSelectionType(_BaseType):
    #: The following type of Product Selections is supported:
    type: "ProductSelectionTypeEnum"

    def __init__(self, *, type: "ProductSelectionTypeEnum"):
        self.type = type

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ProductSelectionType":
        if data["type"] == "individual":
            from ._schemas.product_selection import IndividualProductSelectionTypeSchema

            return IndividualProductSelectionTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionTypeSchema

        return ProductSelectionTypeSchema().dump(self)


class IndividualProductSelectionType(ProductSelectionType):
    #: The name of the Product Selection which is recommended to be unique.
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name

        super().__init__(type=ProductSelectionTypeEnum.INDIVIDUAL)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "IndividualProductSelectionType":
        from ._schemas.product_selection import IndividualProductSelectionTypeSchema

        return IndividualProductSelectionTypeSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import IndividualProductSelectionTypeSchema

        return IndividualProductSelectionTypeSchema().dump(self)


class ProductSelectionTypeEnum(enum.Enum):
    """The following type of Product Selections is supported:"""

    INDIVIDUAL = "individual"


class ProductSelectionUpdate(_BaseType):
    version: int
    actions: typing.List["ProductSelectionUpdateAction"]

    def __init__(
        self, *, version: int, actions: typing.List["ProductSelectionUpdateAction"]
    ):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionUpdate":
        from ._schemas.product_selection import ProductSelectionUpdateSchema

        return ProductSelectionUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionUpdateSchema

        return ProductSelectionUpdateSchema().dump(self)


class ProductSelectionUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionUpdateAction":
        if data["action"] == "addProduct":
            from ._schemas.product_selection import (
                ProductSelectionAddProductActionSchema,
            )

            return ProductSelectionAddProductActionSchema().load(data)
        if data["action"] == "changeName":
            from ._schemas.product_selection import (
                ProductSelectionChangeNameActionSchema,
            )

            return ProductSelectionChangeNameActionSchema().load(data)
        if data["action"] == "removeProduct":
            from ._schemas.product_selection import (
                ProductSelectionRemoveProductActionSchema,
            )

            return ProductSelectionRemoveProductActionSchema().load(data)
        if data["action"] == "setCustomField":
            from ._schemas.product_selection import (
                ProductSelectionSetCustomFieldActionSchema,
            )

            return ProductSelectionSetCustomFieldActionSchema().load(data)
        if data["action"] == "setCustomType":
            from ._schemas.product_selection import (
                ProductSelectionSetCustomTypeActionSchema,
            )

            return ProductSelectionSetCustomTypeActionSchema().load(data)
        if data["action"] == "setKey":
            from ._schemas.product_selection import ProductSelectionSetKeyActionSchema

            return ProductSelectionSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionUpdateActionSchema

        return ProductSelectionUpdateActionSchema().dump(self)


class ProductsInStorePagedQueryResponse(_BaseType):
    """[PagedQueryResult](/general-concepts#pagedqueryresult) containing an array of [ProductSelectionAssignment](ctp:api:type:ProductSelectionAssignment)."""

    #: Number of results requested in the query request.
    limit: int
    #: Offset supplied by the client or the server default.
    #: It is the number of elements skipped, not a page number.
    offset: int
    #: Actual number of results returned.
    count: int
    #: Total number of results matching the query.
    #: This number is an estimation that is not [strongly consistent](/general-concepts#strong-consistency).
    #: Unlike other endpoints, the Product Selection endpoint does not return this field by default.
    #: To get `total`, pass the query parameter `withTotal` set to `true`.
    #: When the results are filtered with a [Query Predicate](/predicates/query), `total` is subject to a [limit](/limits#queries).
    total: typing.Optional[int]
    #: Product Selection Assignments.
    results: typing.List["ProductSelectionAssignment"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["ProductSelectionAssignment"]
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
    ) -> "ProductsInStorePagedQueryResponse":
        from ._schemas.product_selection import ProductsInStorePagedQueryResponseSchema

        return ProductsInStorePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductsInStorePagedQueryResponseSchema

        return ProductsInStorePagedQueryResponseSchema().dump(self)


class ProductSelectionAddProductAction(ProductSelectionUpdateAction):
    #: ResourceIdentifier to Product
    product: "ProductResourceIdentifier"

    def __init__(self, *, product: "ProductResourceIdentifier"):
        self.product = product

        super().__init__(action="addProduct")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionAddProductAction":
        from ._schemas.product_selection import ProductSelectionAddProductActionSchema

        return ProductSelectionAddProductActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionAddProductActionSchema

        return ProductSelectionAddProductActionSchema().dump(self)


class ProductSelectionChangeNameAction(ProductSelectionUpdateAction):
    #: The new name to be set for the Product Selection.
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name

        super().__init__(action="changeName")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionChangeNameAction":
        from ._schemas.product_selection import ProductSelectionChangeNameActionSchema

        return ProductSelectionChangeNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionChangeNameActionSchema

        return ProductSelectionChangeNameActionSchema().dump(self)


class ProductSelectionRemoveProductAction(ProductSelectionUpdateAction):
    #: ResourceIdentifier to Product
    product: "ProductResourceIdentifier"

    def __init__(self, *, product: "ProductResourceIdentifier"):
        self.product = product

        super().__init__(action="removeProduct")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionRemoveProductAction":
        from ._schemas.product_selection import (
            ProductSelectionRemoveProductActionSchema,
        )

        return ProductSelectionRemoveProductActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import (
            ProductSelectionRemoveProductActionSchema,
        )

        return ProductSelectionRemoveProductActionSchema().dump(self)


class ProductSelectionSetCustomFieldAction(ProductSelectionUpdateAction):
    #: Name of the [Custom Field](/../api/projects/custom-fields).
    name: str
    #: If `value` is absent or `null`, this field will be removed if it exists.
    #: Trying to remove a field that does not exist will fail with an [InvalidOperation](/../api/errors#general-400-invalid-operation) error.
    #: If `value` is provided, it is set for the field defined by `name`.
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None):
        self.name = name
        self.value = value

        super().__init__(action="setCustomField")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionSetCustomFieldAction":
        from ._schemas.product_selection import (
            ProductSelectionSetCustomFieldActionSchema,
        )

        return ProductSelectionSetCustomFieldActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import (
            ProductSelectionSetCustomFieldActionSchema,
        )

        return ProductSelectionSetCustomFieldActionSchema().dump(self)


class ProductSelectionSetCustomTypeAction(ProductSelectionUpdateAction):
    #: Defines the [Type](ctp:api:type:Type) that extends the ProductSelection with [Custom Fields](/../api/projects/custom-fields).
    #: If absent, any existing Type and Custom Fields are removed from the ProductSelection.
    type: typing.Optional["TypeResourceIdentifier"]
    #: Sets the [Custom Fields](/../api/projects/custom-fields) fields for the ProductSelection.
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
    ) -> "ProductSelectionSetCustomTypeAction":
        from ._schemas.product_selection import (
            ProductSelectionSetCustomTypeActionSchema,
        )

        return ProductSelectionSetCustomTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import (
            ProductSelectionSetCustomTypeActionSchema,
        )

        return ProductSelectionSetCustomTypeActionSchema().dump(self)


class ProductSelectionSetKeyAction(ProductSelectionUpdateAction):
    #: If `key` is absent or `null`, the existing key, if any, will be removed.
    key: typing.Optional[str]

    def __init__(self, *, key: typing.Optional[str] = None):
        self.key = key

        super().__init__(action="setKey")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ProductSelectionSetKeyAction":
        from ._schemas.product_selection import ProductSelectionSetKeyActionSchema

        return ProductSelectionSetKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.product_selection import ProductSelectionSetKeyActionSchema

        return ProductSelectionSetKeyActionSchema().dump(self)
