
from fastapi import FastAPI
from routes import booking_router

app = FastAPI()
app.include_router(booking_router)
