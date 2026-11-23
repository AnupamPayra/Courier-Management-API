from fastapi import Depends, APIRouter
from sqlmodel import SQLModel, Field, Relationship, Session
from database import get_session
from sqlmodel import select
from scheema import Employee, Customer
from models import EmployeeDetailsView, EmployeeShipmentDetailsView

route = APIRouter(prefix="/employees", tags=["Employee management"])

@route.post("/")
def create_employee(name: str, session: Session = Depends(get_session)):
    new_employee = Employee(name=name)
    session.add(new_employee)
    session.commit()
    session.refresh(new_employee)
    return {
        "message": "Employee created successfully", 
        "employee_id": new_employee.id,
        "employee_name": new_employee.name
        }

@route.get("/", response_model=list[EmployeeDetailsView])
def get_employees(session: Session = Depends(get_session)):
    employees = session.exec(select(Employee)).all()
    return employees

@route.get("/customers", response_model=list[Customer])
def get_all_customers(session: Session = Depends(get_session)):
    customers = session.exec(select(Customer)).all()
    if not customers:
        return [{"message": "No customers found"}]
    return customers