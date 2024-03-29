from fastapi import APIRouter, JSONResponse
from FastAPi_Tutorial.models import Booking
from FastAPi_Tutorial.services import process_booking
booking_router = APIRouter(prefix="/booking", tags=["users"])


@booking_router.post("/")
async def create_booking(booking: Booking):
    results = await process_booking(booking)
    return JSONResponse(status_code=201, content={"data": results, "message": "Booking successful"})
# 