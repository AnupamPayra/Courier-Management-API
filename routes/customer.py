from fastapi import FastAPI, APIRouter, Depends
from sqlmodel import SQLModel, Session
from models import Customer, Customer_update, Customer_view
from scheema import Customer as customer_table
from database import get_session
from execption import (CustomerNotfound, customer_id_not_found_handler)

route = APIRouter(prefix="/customer", tags=["customer management"])


# Adding new customer
@route.post("/", response_model=Customer_view)
def add_new_customer(data: Customer, session: Session = Depends(get_session)):
    new_data = customer_table(**data.model_dump())
    session.add(new_data)
    session.commit()
    session.refresh(new_data)
    return new_data

# Checking customer details
@route.get("/{id}", response_model=Customer_view)
def view_details(id: int, session: Session = Depends(get_session)):
    customer_details = session.get(customer_table, id)

    if not customer_details:
        raise CustomerNotfound(id=id)
    return customer_details

@route.patch("/{id}", response_model=Customer_view)
def update_details(id: int, updated_data: Customer_update, session: Session = Depends(get_session)):
    customer_info = session.get(customer_table, id)
    if not customer_info:
        raise CustomerNotfound(id=id)

    new_data = updated_data.model_dump(exclude_unset=True)
    for key, values in new_data.items():
        setattr(customer_info, key, values)
    session.add(customer_info)
    session.commit()
    session.refresh(customer_info)
    return customer_info

@route.delete("/{id}")
def delete_customer(id: int, session: Session = Depends(get_session)):
    customer_info = session.get(customer_table, id)
    if not customer_info:
        raise CustomerNotfound(id=id)

    session.delete(customer_info)
    session.commit()
    return {
        "message": "Your customer information is succesfuly deleted"
    }
    