from pydantic import BaseModel, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import date


class ContactDetails(BaseModel):
    name: str = Field(min_length=3, max_length=50, description="Name of the passenger", examples=["John Doe"], title="Name",pattern="^[a-zA-Z ]+$")  # noqa
    age: int = Field(gt=0, lt=120, description="Age of the passenger", examples=[25], title="Age") # noqa
    email: EmailStr
    phone: PhoneNumber = Field(description="Phone number of the passenger", examples=["+2348123456789"], title="Phone Number")  # noqa
    next_of_kin: str = Field(min_length=3, max_length=50, description="Name of the next of kin", examples=["Jane Doe"], title="Next of Kin",pattern="^[a-zA-Z ]+$")  # noqa


class FlightDetails(BaseModel):
    origin: str = Field(min_length=3, max_length=50, description="Origin of the flight", examples=["Lagos"], title="Origin",pattern="^[a-zA-Z ]+$")  # noqa
    destination: str = Field(min_length=3, max_length=50, description="Destination of the flight", examples=["Abuja"], title="Destination",pattern="^[a-zA-Z ]+$")  # noqa
    flight_date: date = Field(description="Date of the flight", examples=["2021-12-25"], title="Flight Date")


class Booking(BaseModel):
    contact_details: ContactDetails
    flight_details: FlightDetails
    seat_pref: str = Field(min_length=2, max_length=2, description="Seat preference of the passenger", examples=["A1"], title="Seat Preference",pattern="^[A-Z][1-4]$")  # noqa  