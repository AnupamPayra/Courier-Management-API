from sqlmodel import SQLModel, Field

# Customer request
class Customer(SQLModel):
    id: int | None
    name: str = Field(default="XXXXX", min_length=2, max_length=100)
    phone_no: str = Field(min_length=10, max_length=10)

# Customer Shipment tracking
class Shipment(SQLModel):
    parcel_id: int
    customer_id: int
    name: str = Field(max_length=100, min_length=2)
    phone_no: str = Field(min_length=10, max_length=10)
    city: str
    state: str
    pin: str = Field(min_length=6, max_length=10)
    location: str = Field(max_length=500, min_length=2)
    status: list[list[str, str]]

# Creating a new fresh order
class NewOrder(SQLModel):
    item: str = Field(max_length=100, min_length=2)
    quantity: int = Field(min_length=1, max_length=1000)
    city: str
    state: str
    pin: str = Field(min_length=6, max_length=10)
    location: str = Field(max_length=500, min_length=2)

