from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models import Booking
from services import process_booking
booking_router = APIRouter(prefix="/booking", tags=["users"])


@booking_router.post("/")
async def create_booking(booking: Booking):
    results = await process_booking(booking)
    return JSONResponse(status_code=201, content={"data": results, "message": "Booking successful"})
# 