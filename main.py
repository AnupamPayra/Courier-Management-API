from fastapi import FastAPI
from contextlib import asynccontextmanager


async def lifespan(app: FastAPI):
    pass


app = FastAPI(
    title="Curior Company management system",
    description="A Curior company management automation - Customer, shiping, parcel management.",
    lifespan=lifespan
)