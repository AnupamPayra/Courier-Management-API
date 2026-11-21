from sqlmodel import SQLModel, Field

# Customer request
class Customer(SQLModel):
    id: int | None
    name: str = Field(default="XXXXX", min_length=2, max_length=100)
    phone_no: str = Field(min_length=10, max_length=10)

# Customer update
class Customer_update(SQLModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    phone_no: str | None = Field(min_length=10, max_length=10)

# Customer view
class Customer_view(SQLModel):
    id: int
    name: str | None = Field(default=None, min_length=2, max_length=100)
    phone_no: str | None = Field(min_length=10, max_length=10)


# Customer Shipment tracking
class Shipment(SQLModel):
    shipment_id: int
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
    customer_id: int
    name: str
    alternative_phone_no: str | None = Field(default=None, max_length=10, min_length=10)
    item: str = Field(max_length=100, min_length=2)
    item_id: int
    quantity: int = Field(min_length=1, max_length=1000)
    name: str
    phone_no: str = Field(min_length=10, max_length=10)
    city: str
    state: str
    pin: str = Field(min_length=6, max_length=10)
    location: str = Field(max_length=500, min_length=2)

# Order view
class OrderView(SQLModel):
    item: str = Field(max_length=100, min_length=2)
    quantity: int = Field(min_length=1, max_length=1000)
    name: str
    phone_no: str = Field(min_length=10, max_length=10)
    alternative_phone_no: str | None = Field(default=None, max_length=10, min_length=10)
    city: str
    state: str
    pin: str = Field(min_length=6, max_length=10)
    location: str = Field(max_length=500, min_length=2)

# Employees
class ShipmentDetails(SQLModel):
    parcel_id: int
    customer_id: int

    item: str
    quantity: int

    r_city: str
    r_state: str
    r_pin: str = Field(min_length=6, max_length=10)
    r_location: str = Field(max_length=500, min_length=2)
    
    s_city: str
    s_state: str
    s_pin: str = Field(min_length=6, max_length=10)
    s_location: str = Field(max_length=500, min_length=2)
    s_status: list[list[str, str]]

