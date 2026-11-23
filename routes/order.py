from fastapi import FastAPI, APIRouter, Depends
from sqlmodel import SQLModel, Field, Session, select
from database import get_session
from models import NewOrder, OrderView, OrderTrack
from scheema import Order, Destiantion, Shipment, Customer, ShipmentHistory
from execption import CustomerNotfound
from execption import ShipmentNotfound

route = APIRouter(prefix="/Order", tags=["Order management by customer"])


@route.post("/oder", response_model=OrderView)
def create_order(data: NewOrder, session: Session = Depends(get_session)):
    customer_detail = session.exec(
        select(Customer).where(Customer.id==data.customer_id)
    ).first()

    if not customer_detail:
        raise CustomerNotfound

    alternative_phone_no= data.alternative_phone_no
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
        customer_id=customer_detail.id,
        item_id=item_id, 
        item_name=item_name,
        alternative_ph_no=alternative_phone_no,
        customer_name=name,
        primary_no=customer_detail.phone_no
        
    )
    session.add(order_data)
    session.commit()
    session.refresh(order_data)


    shipment_data = Shipment(
        customer_id=customer_id,
        order_id=order_data.order_id
    )

    session.add(shipment_data)
    session.commit()
    session.refresh(shipment_data)

    shipment_history_data = ShipmentHistory(
        shipment_id=shipment_data.shipment_id,
        status=shipment_data.status,
        employee_id=None
    )
    session.add(shipment_history_data)
    session.commit()
    session.refresh(shipment_history_data)


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
    return {
        "shipment_id_track": shipment_data.shipment_id,
        "item": order_data.item_name,
        "quantity": order_data.quantity,
        "name": data.name,
        "phone_no": customer_detail.phone_no,
        "alternative_phone_no": order_data.alternative_ph_no,
        "city": destination_data.city,
        "state": destination_data.state,
        "pin": destination_data.pin,
        "location": destination_data.location
    }

@route.get("/{customer_id}", response_model=list[OrderTrack])    
def get_all_order_details(customer_id: int, session: Session = Depends(get_session)):
    if not session.get(Customer, customer_id):
        raise CustomerNotfound(id=customer_id)

    statement = select(
        Customer, Order, Shipment
        ).join(
            Order, Customer.id == Order.customer_id
            ).join(
                Shipment, Order.order_id == Shipment.order_id
                ).where(
                    Customer.id == customer_id
                    )

    shipment_details = session.exec(statement).all()

    result = []

    for customer, order, shipment in shipment_details:
        result.append(
            OrderTrack(
                shipment_id_track=shipment.shipment_id,
                order_id=order.order_id,
                item=order.item_name,
                quantity=order.quantity,
                name=customer.name,
                status=shipment.status
            )
        )
    return result