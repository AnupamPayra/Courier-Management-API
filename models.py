from sqlmodel import SQLModel, Field
from enum import Enum 
from datetime import datetime

class ShipmentStatus(str, Enum):
    PACKING = "PACKING"
    PICKED_UP = "PICKED_UP"
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    FAILED_DELIVERY="FAILED_DELIVERY"

# Customer create
class Customer(SQLModel):
    id: int | None
    name: str = Field(default="XXXXX", min_length=2, max_length=100)
    phone_no: str = Field(min_length=10, max_length=10)

# Customer update
class Customer_update(SQLModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    phone_no: str | None = Field(default=None, min_length=10, max_length=10)

# Customer view
class Customer_view(SQLModel):
    id: int
    name: str | None = Field(default=None, min_length=2, max_length=100)
    phone_no: str | None = Field(default=None, min_length=10, max_length=10)

#Order ------------------------------------------------------------------------------------------------ 
# Creating a new fresh order
class NewOrder(SQLModel):
    customer_id: int
    name: str
    alternative_phone_no: str | None = Field(default=None, max_length=10, min_length=10)
    item: str = Field(max_length=100, min_items=2)
    item_id: int
    quantity: int = Field(ge=1, le=1000)
    name: str
    city: str
    state: str
    pin: str = Field(min_length=6, max_length=10)
    location: str = Field(max_length=500, min_length=2)

# Order view as response model
class OrderView(SQLModel):
    shipment_id_track: int
    item: str = Field(max_length=100, min_length=2)
    quantity: int = Field(ge=1, le=1000)
    name: str
    phone_no: str = Field(min_length=10, max_length=10)
    alternative_phone_no: str | None = Field(default=None, max_length=10, min_length=10)
    city: str
    state: str
    pin: str = Field(min_length=6, max_length=10)
    location: str = Field(max_length=500, min_length=2)

#Shipment ------------------------------------------------------------------------------------------------
# All order records view to get shipment_id
class OrderTrack(SQLModel):
    shipment_id_track: int
    order_id: int
    item: str = Field(max_length=100, min_length=2)
    quantity: int = Field(ge=1, le=1000)
    name: str
    status: ShipmentStatus

# Shipment history view
class ShipmentRecordStatus(SQLModel):
    shipment_id: int
    order_date: datetime
    status: list[ShipmentStatus]

# Employee --------------------------------------------------------
# All employee details
class EmployeeDetailsView(SQLModel):
    id: int
    name: str

# Employees checking
class EmployeeShipmentDetailsView(SQLModel):
    parcel_id: int
    customer_id: int

    item: str 
    quantity: int

    r_city: str
    r_state: str
    r_pin: str = Field(min_length=6, max_length=10)
    r_location: str = Field(max_length=500, min_length=2)

    s_status: list[list[str, str]]

# Employee shipment status update
class ShipmentStatusUpdate(SQLModel):
    shipment_id: int
    status: ShipmentStatus
