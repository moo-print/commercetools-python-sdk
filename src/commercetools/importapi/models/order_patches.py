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

if typing.TYPE_CHECKING:
    from .common import Address
    from .orders import DeliveryItem, ParcelMeasurements, TrackingData

__all__ = [
    "DeliveryAddressDraft",
    "DeliveryDraft",
    "DeliveryParcel",
    "DeliveryParcelDraft",
    "OrderField",
    "OrderPatchImport",
    "ParcelItems",
    "ParcelMeasurementDraft",
    "ParcelTrackingData",
    "RemoveDeliveryDraft",
    "RemoveParcelFromDeliveryDraft",
    "ReturnInfo",
    "ReturnItemDraft",
    "ReturnShipmentState",
]


class ReturnShipmentState(enum.Enum):
    """Maps to `ReturnItem.shipmentState`"""

    ADVISED = "Advised"
    RETURNED = "Returned"
    BACK_IN_STOCK = "BackInStock"
    UNUSABLE = "Unusable"


class ReturnItemDraft(_BaseType):
    quantity: float
    line_item_id: typing.Optional[str]
    custom_line_item_id: typing.Optional[str]
    comment: typing.Optional[str]
    #: Maps to `ReturnItem.shipmentState`
    shipment_state: "ReturnShipmentState"

    def __init__(
        self,
        *,
        quantity: float,
        line_item_id: typing.Optional[str] = None,
        custom_line_item_id: typing.Optional[str] = None,
        comment: typing.Optional[str] = None,
        shipment_state: "ReturnShipmentState"
    ):
        self.quantity = quantity
        self.line_item_id = line_item_id
        self.custom_line_item_id = custom_line_item_id
        self.comment = comment
        self.shipment_state = shipment_state

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReturnItemDraft":
        from ._schemas.order_patches import ReturnItemDraftSchema

        return ReturnItemDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import ReturnItemDraftSchema

        return ReturnItemDraftSchema().dump(self)


class ReturnInfo(_BaseType):
    items: typing.List["ReturnItemDraft"]
    #: Maps to `ReturnInfo.returnTrackingId`
    return_tracking_id: typing.Optional[str]
    #: Maps to `ReturnInfo.returnDate`
    return_date: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        items: typing.List["ReturnItemDraft"],
        return_tracking_id: typing.Optional[str] = None,
        return_date: typing.Optional[datetime.datetime] = None
    ):
        self.items = items
        self.return_tracking_id = return_tracking_id
        self.return_date = return_date

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ReturnInfo":
        from ._schemas.order_patches import ReturnInfoSchema

        return ReturnInfoSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import ReturnInfoSchema

        return ReturnInfoSchema().dump(self)


class DeliveryParcel(_BaseType):
    delivery_id: str
    measurements: typing.Optional["ParcelMeasurements"]
    tracking_data: typing.Optional["TrackingData"]
    items: typing.Optional[typing.List["DeliveryItem"]]

    def __init__(
        self,
        *,
        delivery_id: str,
        measurements: typing.Optional["ParcelMeasurements"] = None,
        tracking_data: typing.Optional["TrackingData"] = None,
        items: typing.Optional[typing.List["DeliveryItem"]] = None
    ):
        self.delivery_id = delivery_id
        self.measurements = measurements
        self.tracking_data = tracking_data
        self.items = items

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DeliveryParcel":
        from ._schemas.order_patches import DeliveryParcelSchema

        return DeliveryParcelSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import DeliveryParcelSchema

        return DeliveryParcelSchema().dump(self)


class DeliveryParcelDraft(_BaseType):
    measurements: typing.Optional["ParcelMeasurements"]
    tracking_data: typing.Optional["TrackingData"]
    items: typing.Optional[typing.List["DeliveryItem"]]

    def __init__(
        self,
        *,
        measurements: typing.Optional["ParcelMeasurements"] = None,
        tracking_data: typing.Optional["TrackingData"] = None,
        items: typing.Optional[typing.List["DeliveryItem"]] = None
    ):
        self.measurements = measurements
        self.tracking_data = tracking_data
        self.items = items

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DeliveryParcelDraft":
        from ._schemas.order_patches import DeliveryParcelDraftSchema

        return DeliveryParcelDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import DeliveryParcelDraftSchema

        return DeliveryParcelDraftSchema().dump(self)


class DeliveryDraft(_BaseType):
    items: typing.List["DeliveryItem"]
    address: typing.Optional["Address"]
    parcels: typing.List["DeliveryParcelDraft"]

    def __init__(
        self,
        *,
        items: typing.List["DeliveryItem"],
        address: typing.Optional["Address"] = None,
        parcels: typing.List["DeliveryParcelDraft"]
    ):
        self.items = items
        self.address = address
        self.parcels = parcels

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DeliveryDraft":
        from ._schemas.order_patches import DeliveryDraftSchema

        return DeliveryDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import DeliveryDraftSchema

        return DeliveryDraftSchema().dump(self)


class DeliveryAddressDraft(_BaseType):
    delivery_id: str
    address: typing.Optional["Address"]

    def __init__(self, *, delivery_id: str, address: typing.Optional["Address"] = None):
        self.delivery_id = delivery_id
        self.address = address

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "DeliveryAddressDraft":
        from ._schemas.order_patches import DeliveryAddressDraftSchema

        return DeliveryAddressDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import DeliveryAddressDraftSchema

        return DeliveryAddressDraftSchema().dump(self)


class ParcelMeasurementDraft(_BaseType):
    parcel_id: str
    measurements: typing.Optional["ParcelMeasurements"]

    def __init__(
        self,
        *,
        parcel_id: str,
        measurements: typing.Optional["ParcelMeasurements"] = None
    ):
        self.parcel_id = parcel_id
        self.measurements = measurements

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "ParcelMeasurementDraft":
        from ._schemas.order_patches import ParcelMeasurementDraftSchema

        return ParcelMeasurementDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import ParcelMeasurementDraftSchema

        return ParcelMeasurementDraftSchema().dump(self)


class ParcelTrackingData(_BaseType):
    parcel_id: str
    tracking_data: typing.Optional["TrackingData"]

    def __init__(
        self, *, parcel_id: str, tracking_data: typing.Optional["TrackingData"] = None
    ):
        self.parcel_id = parcel_id
        self.tracking_data = tracking_data

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ParcelTrackingData":
        from ._schemas.order_patches import ParcelTrackingDataSchema

        return ParcelTrackingDataSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import ParcelTrackingDataSchema

        return ParcelTrackingDataSchema().dump(self)


class ParcelItems(_BaseType):
    parcel_id: str
    items: typing.Optional[typing.List["DeliveryItem"]]

    def __init__(
        self,
        *,
        parcel_id: str,
        items: typing.Optional[typing.List["DeliveryItem"]] = None
    ):
        self.parcel_id = parcel_id
        self.items = items

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "ParcelItems":
        from ._schemas.order_patches import ParcelItemsSchema

        return ParcelItemsSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import ParcelItemsSchema

        return ParcelItemsSchema().dump(self)


class RemoveDeliveryDraft(_BaseType):
    id: str

    def __init__(self, *, id: str):
        self.id = id

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "RemoveDeliveryDraft":
        from ._schemas.order_patches import RemoveDeliveryDraftSchema

        return RemoveDeliveryDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import RemoveDeliveryDraftSchema

        return RemoveDeliveryDraftSchema().dump(self)


class RemoveParcelFromDeliveryDraft(_BaseType):
    parcel_id: str

    def __init__(self, *, parcel_id: str):
        self.parcel_id = parcel_id

        super().__init__()

    @classmethod
    def deserialize(
        cls, data: typing.Dict[str, typing.Any]
    ) -> "RemoveParcelFromDeliveryDraft":
        from ._schemas.order_patches import RemoveParcelFromDeliveryDraftSchema

        return RemoveParcelFromDeliveryDraftSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import RemoveParcelFromDeliveryDraftSchema

        return RemoveParcelFromDeliveryDraftSchema().dump(self)


class OrderField(_BaseType):
    """Order fields that needs to be added or updated."""

    #: Maps to `Order.returnInfo`
    add_return_info: typing.Optional["ReturnInfo"]
    #: Maps to `Order.delivery`
    add_parcel_to_delivery: typing.Optional["DeliveryParcel"]
    #: Maps to `Order.delivery`
    add_deliveries: typing.Optional[typing.List["DeliveryDraft"]]
    #: Maps to `Order.removeDelivery`
    remove_delivery: typing.Optional["RemoveDeliveryDraft"]
    #: Maps to `Order.removeParcelFromDelivery`
    remove_parcel_from_delivery: typing.Optional["RemoveParcelFromDeliveryDraft"]
    #: Maps to `Order.addressDraft`
    set_delivery_address: typing.Optional["DeliveryAddressDraft"]
    #: Maps to `Order.parcelMeasurements`
    set_parcel_measurements: typing.Optional["ParcelMeasurementDraft"]
    #: Maps to `Order.parcelTrackingData`
    set_parcel_tracking_data: typing.Optional["ParcelTrackingData"]
    #: Maps to `Order.parcelItems`
    set_parcel_items: typing.Optional[typing.List["ParcelItems"]]

    def __init__(
        self,
        *,
        add_return_info: typing.Optional["ReturnInfo"] = None,
        add_parcel_to_delivery: typing.Optional["DeliveryParcel"] = None,
        add_deliveries: typing.Optional[typing.List["DeliveryDraft"]] = None,
        remove_delivery: typing.Optional["RemoveDeliveryDraft"] = None,
        remove_parcel_from_delivery: typing.Optional[
            "RemoveParcelFromDeliveryDraft"
        ] = None,
        set_delivery_address: typing.Optional["DeliveryAddressDraft"] = None,
        set_parcel_measurements: typing.Optional["ParcelMeasurementDraft"] = None,
        set_parcel_tracking_data: typing.Optional["ParcelTrackingData"] = None,
        set_parcel_items: typing.Optional[typing.List["ParcelItems"]] = None
    ):
        self.add_return_info = add_return_info
        self.add_parcel_to_delivery = add_parcel_to_delivery
        self.add_deliveries = add_deliveries
        self.remove_delivery = remove_delivery
        self.remove_parcel_from_delivery = remove_parcel_from_delivery
        self.set_delivery_address = set_delivery_address
        self.set_parcel_measurements = set_parcel_measurements
        self.set_parcel_tracking_data = set_parcel_tracking_data
        self.set_parcel_items = set_parcel_items

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderField":
        from ._schemas.order_patches import OrderFieldSchema

        return OrderFieldSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import OrderFieldSchema

        return OrderFieldSchema().dump(self)


class OrderPatchImport(_BaseType):
    """Representation for an update of an [Order](/../api/projects/orders#order). Use this type to import updates for existing
    [Orders](/../api/projects/orders#order) in a Project.

    """

    #: Maps to `Order.orderNumber`, String that uniquely identifies an order, unique across a project.
    order_number: str
    #: Each field referenced must be defined in an already existing order in the project or the import operation state is set to `validationFailed`.
    fields: "OrderField"

    def __init__(self, *, order_number: str, fields: "OrderField"):
        self.order_number = order_number
        self.fields = fields

        super().__init__()

    @classmethod
    def deserialize(cls, data: typing.Dict[str, typing.Any]) -> "OrderPatchImport":
        from ._schemas.order_patches import OrderPatchImportSchema

        return OrderPatchImportSchema().load(data)

    def serialize(self) -> typing.Dict[str, typing.Any]:
        from ._schemas.order_patches import OrderPatchImportSchema

        return OrderPatchImportSchema().dump(self)