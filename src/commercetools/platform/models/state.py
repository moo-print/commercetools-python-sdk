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

__all__ = [
    "State",
    "StateAddRolesAction",
    "StateChangeInitialAction",
    "StateChangeKeyAction",
    "StateChangeTypeAction",
    "StateDraft",
    "StatePagedQueryResponse",
    "StateReference",
    "StateRemoveRolesAction",
    "StateResourceIdentifier",
    "StateRoleEnum",
    "StateSetDescriptionAction",
    "StateSetNameAction",
    "StateSetRolesAction",
    "StateSetTransitionsAction",
    "StateTypeEnum",
    "StateUpdate",
    "StateUpdateAction",
]


class State(BaseResource):
    #: IDs and references that last modified the State.
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: IDs and references that created the State.
    created_by: typing.Optional["CreatedBy"]
    #: User-defined unique identifier of the State.
    key: str
    #: Indicates to which resource or object types the State is assigned to.
    type: "StateTypeEnum"
    #: Name of the State.
    name: typing.Optional["LocalizedString"]
    #: Description of the State.
    description: typing.Optional["LocalizedString"]
    #: `true` for an initial State, the first State in a workflow.
    initial: bool
    #: `true` for States that are an integral part of the [Project](ctp:api:type:Project). Those States cannot be deleted and their `key` cannot be changed.
    built_in: bool
    #: Roles the State can fulfill for [Reviews](ctp:api:type:Review) and [Line Items](ctp:api:type:LineItem).
    roles: typing.Optional[typing.List["StateRoleEnum"]]
    #: - list of States of the same `type` that the current State can be transitioned to. For example, when the current State is the _Initial_ State of [StateType](ctp:api:type:StateTypeEnum) `OrderState` and this list contains the reference to the _Shipped_ `OrderState`, the transition _Initial_ -> _Shipped_ is allowed.
    #: - if empty, no transitions are allowed from the current State, defining the current State as final for this workflow.
    #: - if not set, the validation is turned off and the current State can be transitioned to any other State of the same `type` as the current State.
    transitions: typing.Optional[typing.List["StateReference"]]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: str,
        type: "StateTypeEnum",
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        initial: bool,
        built_in: bool,
        roles: typing.Optional[typing.List["StateRoleEnum"]] = None,
        transitions: typing.Optional[typing.List["StateReference"]] = None
    ):
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.type = type
        self.name = name
        self.description = description
        self.initial = initial
        self.built_in = built_in
        self.roles = roles
        self.transitions = transitions

        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "State":
        from ._schemas.state import StateSchema

        return StateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSchema

        return StateSchema().dump(self)


class StateDraft(_BaseType):
    #: User-defined unique identifier for the State.
    key: str
    #: Specify to which resource or object type the State is assigned to.
    type: "StateTypeEnum"
    #: Name of the State.
    name: typing.Optional["LocalizedString"]
    #: Description of the State.
    description: typing.Optional["LocalizedString"]
    #: Set to `false` if the State is not the first step in a workflow.
    initial: typing.Optional[bool]
    #: If suitable, assign predifined roles the State can fulfill in case the State's `type` is `LineItemState` or `ReviewState`.
    roles: typing.Optional[typing.List["StateRoleEnum"]]
    #: Define the list of States of the same `type` to which the current State can be transitioned to.
    #:
    #: - If, for example, the current State is the _Initial_ State of [StateType](ctp:api:type:StateTypeEnum) `OrderState` and you want to allow the transition _Initial_ -> _Shipped_, then add the [StateResourceIdentifier](ctp:api:type:StateResourceIdentifier) to the _Shipped_ `OrderState` to this list.
    #: - Set to empty list for not allowing any transition from the current State and defining it as final State for a workflow.
    #: - Do not set this field at all to turn off validation and allowing transitions to any other State of the same `type` as the current State.
    transitions: typing.Optional[typing.List["StateResourceIdentifier"]]

    def __init__(
        self,
        *,
        key: str,
        type: "StateTypeEnum",
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        initial: typing.Optional[bool] = None,
        roles: typing.Optional[typing.List["StateRoleEnum"]] = None,
        transitions: typing.Optional[typing.List["StateResourceIdentifier"]] = None
    ):
        self.key = key
        self.type = type
        self.name = name
        self.description = description
        self.initial = initial
        self.roles = roles
        self.transitions = transitions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateDraft":
        from ._schemas.state import StateDraftSchema

        return StateDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateDraftSchema

        return StateDraftSchema().dump(self)


class StatePagedQueryResponse(_BaseType):
    """[PagedQueryResult](/../api/general-concepts#pagedqueryresult) with `results` containing an array of [State](ctp:api:type:State)."""

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
    #: [States](ctp:api:type:State) matching the query.
    results: typing.List["State"]

    def __init__(
        self,
        *,
        limit: int,
        offset: int,
        count: int,
        total: typing.Optional[int] = None,
        results: typing.List["State"]
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
    ) -> "StatePagedQueryResponse":
        from ._schemas.state import StatePagedQueryResponseSchema

        return StatePagedQueryResponseSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StatePagedQueryResponseSchema

        return StatePagedQueryResponseSchema().dump(self)


class StateReference(Reference):
    """[Reference](ctp:api:type:Reference) to a [State](ctp:api:type:State)."""

    #: Contains the representation of the expanded State. Only present in responses to requests with [Reference Expansion](/../api/general-concepts#reference-expansion) for States.
    obj: typing.Optional["State"]

    def __init__(self, *, id: str, obj: typing.Optional["State"] = None):
        self.obj = obj

        super().__init__(id=id, type_id=ReferenceTypeId.STATE)

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateReference":
        from ._schemas.state import StateReferenceSchema

        return StateReferenceSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateReferenceSchema

        return StateReferenceSchema().dump(self)


class StateResourceIdentifier(ResourceIdentifier):
    """[ResourceIdentifier](ctp:api:type:ResourceIdentifier) to a [State](ctp:api:type:State). Either `id` or `key` is required. If both are set, an [InvalidJsonInput](/../api/errors#invalidjsoninput) error is returned."""

    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ):

        super().__init__(id=id, key=key, type_id=ReferenceTypeId.STATE)

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateResourceIdentifier":
        from ._schemas.state import StateResourceIdentifierSchema

        return StateResourceIdentifierSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateResourceIdentifierSchema

        return StateResourceIdentifierSchema().dump(self)


class StateRoleEnum(enum.Enum):
    """For some resource types, a State can fulfill the following predefined roles:"""

    REVIEW_INCLUDED_IN_STATISTICS = "ReviewIncludedInStatistics"
    RETURN = "Return"


class StateTypeEnum(enum.Enum):
    """Resource or object type the State can be assigned to."""

    ORDER_STATE = "OrderState"
    LINE_ITEM_STATE = "LineItemState"
    PRODUCT_STATE = "ProductState"
    REVIEW_STATE = "ReviewState"
    PAYMENT_STATE = "PaymentState"
    QUOTE_REQUEST_STATE = "QuoteRequestState"
    STAGED_QUOTE_STATE = "StagedQuoteState"
    QUOTE_STATE = "QuoteState"


class StateUpdate(_BaseType):
    #: Expected version of the State on which the changes should be applied.
    #: If the expected version does not match the actual version, a [ConcurrentModification](ctp:api:type:ConcurrentModificationError) error will be returned.
    version: int
    #: Update actions to be performed on the State.
    actions: typing.List["StateUpdateAction"]

    def __init__(self, *, version: int, actions: typing.List["StateUpdateAction"]):
        self.version = version
        self.actions = actions

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateUpdate":
        from ._schemas.state import StateUpdateSchema

        return StateUpdateSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateUpdateSchema

        return StateUpdateSchema().dump(self)


class StateUpdateAction(_BaseType):
    action: str

    def __init__(self, *, action: str):
        self.action = action

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateUpdateAction":
        if data["action"] == "addRoles":
            from ._schemas.state import StateAddRolesActionSchema

            return StateAddRolesActionSchema().load(data)
        if data["action"] == "changeInitial":
            from ._schemas.state import StateChangeInitialActionSchema

            return StateChangeInitialActionSchema().load(data)
        if data["action"] == "changeKey":
            from ._schemas.state import StateChangeKeyActionSchema

            return StateChangeKeyActionSchema().load(data)
        if data["action"] == "changeType":
            from ._schemas.state import StateChangeTypeActionSchema

            return StateChangeTypeActionSchema().load(data)
        if data["action"] == "removeRoles":
            from ._schemas.state import StateRemoveRolesActionSchema

            return StateRemoveRolesActionSchema().load(data)
        if data["action"] == "setDescription":
            from ._schemas.state import StateSetDescriptionActionSchema

            return StateSetDescriptionActionSchema().load(data)
        if data["action"] == "setName":
            from ._schemas.state import StateSetNameActionSchema

            return StateSetNameActionSchema().load(data)
        if data["action"] == "setRoles":
            from ._schemas.state import StateSetRolesActionSchema

            return StateSetRolesActionSchema().load(data)
        if data["action"] == "setTransitions":
            from ._schemas.state import StateSetTransitionsActionSchema

            return StateSetTransitionsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateUpdateActionSchema

        return StateUpdateActionSchema().dump(self)


class StateAddRolesAction(StateUpdateAction):
    #: Value to append to the array.
    roles: typing.List["StateRoleEnum"]

    def __init__(self, *, roles: typing.List["StateRoleEnum"]):
        self.roles = roles

        super().__init__(action="addRoles")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateAddRolesAction":
        from ._schemas.state import StateAddRolesActionSchema

        return StateAddRolesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateAddRolesActionSchema

        return StateAddRolesActionSchema().dump(self)


class StateChangeInitialAction(StateUpdateAction):
    #: Set to `true` for defining the State as initial State in a state machine and making it the first step in a workflow.
    initial: bool

    def __init__(self, *, initial: bool):
        self.initial = initial

        super().__init__(action="changeInitial")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateChangeInitialAction":
        from ._schemas.state import StateChangeInitialActionSchema

        return StateChangeInitialActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateChangeInitialActionSchema

        return StateChangeInitialActionSchema().dump(self)


class StateChangeKeyAction(StateUpdateAction):
    #: New value to set.
    #: Must not be empty.
    key: str

    def __init__(self, *, key: str):
        self.key = key

        super().__init__(action="changeKey")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateChangeKeyAction":
        from ._schemas.state import StateChangeKeyActionSchema

        return StateChangeKeyActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateChangeKeyActionSchema

        return StateChangeKeyActionSchema().dump(self)


class StateChangeTypeAction(StateUpdateAction):
    #: Resource or object types the State shall be assigned to.
    #: Must not be empty.
    type: "StateTypeEnum"

    def __init__(self, *, type: "StateTypeEnum"):
        self.type = type

        super().__init__(action="changeType")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateChangeTypeAction":
        from ._schemas.state import StateChangeTypeActionSchema

        return StateChangeTypeActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateChangeTypeActionSchema

        return StateChangeTypeActionSchema().dump(self)


class StateRemoveRolesAction(StateUpdateAction):
    #: Roles to remove from the State.
    roles: typing.List["StateRoleEnum"]

    def __init__(self, *, roles: typing.List["StateRoleEnum"]):
        self.roles = roles

        super().__init__(action="removeRoles")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateRemoveRolesAction":
        from ._schemas.state import StateRemoveRolesActionSchema

        return StateRemoveRolesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateRemoveRolesActionSchema

        return StateRemoveRolesActionSchema().dump(self)


class StateSetDescriptionAction(StateUpdateAction):
    #: Value to set.
    #: If empty, any existing value will be removed.
    description: "LocalizedString"

    def __init__(self, *, description: "LocalizedString"):
        self.description = description

        super().__init__(action="setDescription")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateSetDescriptionAction":
        from ._schemas.state import StateSetDescriptionActionSchema

        return StateSetDescriptionActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSetDescriptionActionSchema

        return StateSetDescriptionActionSchema().dump(self)


class StateSetNameAction(StateUpdateAction):
    #: Value to set.
    #: If empty, any existing value will be removed.
    name: "LocalizedString"

    def __init__(self, *, name: "LocalizedString"):
        self.name = name

        super().__init__(action="setName")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateSetNameAction":
        from ._schemas.state import StateSetNameActionSchema

        return StateSetNameActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSetNameActionSchema

        return StateSetNameActionSchema().dump(self)


class StateSetRolesAction(StateUpdateAction):
    #: Value to set.
    #: If empty, any existing value will be removed.
    roles: typing.List["StateRoleEnum"]

    def __init__(self, *, roles: typing.List["StateRoleEnum"]):
        self.roles = roles

        super().__init__(action="setRoles")

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "StateSetRolesAction":
        from ._schemas.state import StateSetRolesActionSchema

        return StateSetRolesActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSetRolesActionSchema

        return StateSetRolesActionSchema().dump(self)


class StateSetTransitionsAction(StateUpdateAction):
    #: Value to set.
    #: If empty, any existing value will be removed.
    #:
    #: Possible transformations of the current State to other States of the same `type` (for example, _Initial_ -> _Shipped_).
    #: When performing a `transitionState` update action and `transitions` is set, the currently referenced State must have a transition to the new State.
    #:
    #: If `transitions` is an empty list, it means the current State is a final State and no further transitions are allowed.
    #: If `transitions` is not set, the validation is turned off.
    #:
    #: When performing a `transitionState` update action, any other State of the same `type` can be transitioned to.
    transitions: typing.Optional[typing.List["StateResourceIdentifier"]]

    def __init__(
        self,
        *,
        transitions: typing.Optional[typing.List["StateResourceIdentifier"]] = None
    ):
        self.transitions = transitions

        super().__init__(action="setTransitions")

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "StateSetTransitionsAction":
        from ._schemas.state import StateSetTransitionsActionSchema

        return StateSetTransitionsActionSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.state import StateSetTransitionsActionSchema

        return StateSetTransitionsActionSchema().dump(self)
