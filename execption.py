from fastapi import Request
from fastapi.responses import JSONResponse

class CustomerNotfound(Exception):
    def __init__(self, id = None):
        self.id = id

def customer_id_not_found_handler(request: Request, exc: CustomerNotfound):
    return JSONResponse(
        status_code=404,
        content={
            "reason": f"The customer {exc.id} never exist",
            "result": "You have to register your credentials",
            "id": exc.id
        }
    )

class ShipmentNotfound(Exception):
    def __init__(self, id = None):
        self.id = id

def shipment_id_not_found_handler(request: Request, exc: ShipmentNotfound):
    return JSONResponse(
        status_code=404,
        content={
            "reason": f"The shipment {exc.id} never exist",
            "result": "You have to register your credentials",
            "id": exc.id
        }
    )

class EmployeeNotfound(Exception):
    def __init__(self, id = None):
        self.id = id
def employee_id_not_found_handler(request: Request, exc: EmployeeNotfound):
    return JSONResponse(
      status_code=404,
        content={
            "reason": f"The employee {exc.id} never exist",
            "result": "You have to register your credentials",
            "id": exc.id
        }
    )