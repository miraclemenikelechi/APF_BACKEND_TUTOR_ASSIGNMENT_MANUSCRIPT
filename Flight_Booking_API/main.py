
from fastapi import FastAPI
from FastAPi_Tutorial.routes import booking_router

app = FastAPI()
app.include_router(booking_router)
