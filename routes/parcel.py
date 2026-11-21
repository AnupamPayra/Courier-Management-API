from fastapi import FastAPI, APIRouter, Depends
from sqlmodel import SQLModel, Field, Session, select
from database import get_session
from models import NewOrder, OrderView, Shipment
from scheema import Order, Destiantion, Shipment, Customer
from execption import CustomerNotfound

route = APIRouter(prefix="/parcel", tags=["Parcel management"])


@route.post("/oder", response_model=OrderView)
def create_order(data: NewOrder, session: Session = Depends(get_session)):
    customer_detail = session.exec(
        select(Customer).where(Customer.id==data.customer_id)
    ).first()

    if not customer_detail:
        raise CustomerNotfound

    alternative_phone_no: str | None = Field(default=None, min_length=10, max_length=10)
    customer_id=data.customer_id
    item_id=data.item_id
    item_name = data.item
    quantity=data.quantity
    name= data.name
    city=data.city
    state=data.state
    pin=data.pin
    location=data.location

    order_data = Order(
        quantity=quantity, 
        item_id=item_id, 
        item_name=item_name,
        alternative_ph_no=alternative_phone_no,
        customer_name=name,
        primary_no=customer_detail.phone_no,
        
    )

    session.add(order_data)
    session.commit()
    session.refresh(order_data)

    shipment_data = Shipment(
        customer_id=customer_id
    )
    session.add(shipment_data)
    session.commit()
    session.refresh(shipment_data)


    destination_data = Destiantion(
        shipment_id=shipment_data.shipment_id,
        location=location,
        city=city,
        pin=pin,
        state=state,
    )
    session.add(destination_data)
    session.commit()
    session.refresh(destination_data)
    return shipment_data.shipment_id

@route.get("/order{order_id}", response_model=Shipment)
def get_shipment_details(id: int, session: Session = Depends(get_session)):
    details = session.get()