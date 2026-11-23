from sqlmodel import SQLModel, Field, Session, select
from database import get_session
from models import ShipmentStatusUpdate, ShipmentRecordStatus
from scheema import Shipment, ShipmentHistory, Employee
from fastapi import APIRouter, Depends
from execption import EmployeeNotfound, ShipmentNotfound

route = APIRouter(prefix="/shipment", tags=["shipment management"])

@route.get("/{shipment_id}", response_model=ShipmentRecordStatus)
def get_shipment_details(shipment_id: int, session: Session = Depends(get_session)):
    shipment_data = session.exec(select(Shipment).where(Shipment.shipment_id == shipment_id)).first()
    shipment_history_data = session.exec(select(ShipmentHistory).where(ShipmentHistory.shipment_id == shipment_id)).all()
    return {
        "shipment_id": shipment_data.shipment_id,
        "order_date": shipment_data.order_date,
        "status": [record.status for record in shipment_history_data]
    }

@route.patch("/status")
def update_shipment_status(employee_id: int, data: ShipmentStatusUpdate, session: Session = Depends(get_session)):
    employee_data = session.get(Employee, employee_id)
    if not employee_data:
        raise EmployeeNotfound(id=employee_id)

    shipment_data = session.get(Shipment, data.shipment_id)
    if not shipment_data:
        raise ShipmentNotfound(id=data.shipment_id)

    shipment_status_data= ShipmentHistory(

        shipment_id = data.shipment_id,
        status = data.status,
        employee_id = employee_id
    )
    session.add(shipment_status_data)
    session.commit()

    shipment_data.status = data.status
    session.add(shipment_data)
    session.commit()

    return {
        "message": f"Shipment status updated successfully by {employee_data.name}",
        "shipment_id": shipment_status_data.shipment_id,
        "status": shipment_status_data.status
    }