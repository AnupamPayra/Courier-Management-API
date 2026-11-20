from fastapi import Depends
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class Customer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    phone_no: str
    shipment : list["Shipment"] = Relationship(back_populates="customer")


class Order(SQLModel, table=True):
    order_id: int | None = Field(default=None, primary_key=True)
    quantity: int = Field(le=1, gt=100)
    item_id: int
    item: str = Field(min_length=2, max_length=100)

class Pickup(SQLModel, table=True):
    pickup_id: int | None = Field(default=None, primary_key=True)
    shipment_id: int | None = Field(foreign_key="shipment.shipment_id", unique=True)
    location: str = Field(description="Sender's location")
    city: str
    pin: str
    state: str
    shipment: "Shipment" = Relationship(back_populates="pickup")


class Destiantion(SQLModel, table=True):
    destination_id: int | None = Field(default=None, primary_key=True)
    shipment_id: int | None = Field(foreign_key="shipment.shipment_id", unique=True)
    location: str = Field(description="Sender's location")
    city: str
    pin: str
    state: str
    shipment: "Shipment" = Relationship(back_populates="destination")


class Shipment(SQLModel, table=True):
    customer_id: int = Field(foreign_key="customer.id")
    customer: "Customer" = Relationship(back_populates="shipment")

    pickup: "Pickup" = Relationship(back_populates="shipment")
    destination: "Destiantion" = Relationship(back_populates="shipment")

    shipment_id: int | None = Field(default=None, primary_key=True)
    order_date: datetime = Field(default_factory=datetime.now)
    shipmentHistory: list["ShipmentHistory"] = Relationship(back_populates="shipment")


class ShipmentHistory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    shipment_id: int = Field(foreign_key="shipment.shipment_id")
    status: str
    timestamp: datetime = Field(default_factory=datetime.now)
    shipment: "Shipment" = Relationship(back_populates="shipmentHistory")