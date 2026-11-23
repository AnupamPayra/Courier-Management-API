from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_table, get_session
from routes.customer import route as customer_route
from routes.order import route as orderl_route
from routes.shipment_route import route as shipment_route
from routes.Employees import route as employee_route

from execption import (CustomerNotfound, customer_id_not_found_handler)
from execption import (ShipmentNotfound, shipment_id_not_found_handler)
from execption import (EmployeeNotfound, employee_id_not_found_handler)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    print("database table are created")
    yield
    print("stop all execution")




app = FastAPI(
    title="Curior Company management system",
    description="A Curior company management automation - Customer, shiping, parcel management.",
    lifespan=lifespan
)

app.include_router(customer_route)
app.include_router(orderl_route)
app.include_router(shipment_route)
app.include_router(employee_route)
app.add_exception_handler(CustomerNotfound, customer_id_not_found_handler)
app.add_exception_handler(ShipmentNotfound, shipment_id_not_found_handler)
app.add_exception_handler(EmployeeNotfound, employee_id_not_found_handler)