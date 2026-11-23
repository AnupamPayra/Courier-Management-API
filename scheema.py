from fastapi import Depends
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone
from models import ShipmentStatus
from datetime import date, time

class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    phone_no: str
    orders: list["Order"] = Relationship(back_populates="customer")

class Order(SQLModel, table=True):
    order_id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    item_id: int
    item_name: str = Field(min_length=2, max_length=100)
    quantity: int = Field(ge=1, le=100)
    alternative_ph_no: str | None = Field(default=None, min_length=10, max_length=10)

    shipment: "Shipment" = Relationship(back_populates="order")
    customer: "Customer" = Relationship(back_populates="orders")

class Shipment(SQLModel, table=True):
    shipment_id: int | None = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.order_id", unique=True)
    order_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: "ShipmentStatus" = Field(default=ShipmentStatus.PACKING)

    order: "Order" = Relationship(back_populates="shipment")
    destination: "Destiantion" = Relationship(back_populates="shipment")

class ShipmentHistory(SQLModel, table=True):
    history_id: int | None = Field(default=None, primary_key=True)
    shipment_id: int = Field(foreign_key="shipment.shipment_id")
    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    employee_id: int | None = Field(default=None, foreign_key="employee.id")
    status: "ShipmentStatus" = Field(default=ShipmentStatus.PACKING)


class Employee(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


class Destiantion(SQLModel, table=True):
    destination_id: int | None = Field(default=None, primary_key=True)
    shipment_id: int = Field(foreign_key="shipment.shipment_id", unique=True)
    location: str = Field(description="Sender's location")
    city: str
    pin: str
    state: str

    shipment: "Shipment" = Relationship(back_populates="destination")