# import fastapi test client
from fastapi.testclient import TestClient
from main import app

# Create a test client using the TestClient class
client = TestClient(app)


# Test the create_booking route
def test_create_booking():
    response = client.post(
        "/booking/",
        json={
            "contact_details": {
                "name": "John Doe",
                "age": 25,
                "email": "user@example.com",
                "phone": "+2348123456789",
                "next_of_kin": "Jane Doe",
            },
            "flight_details": {
                "origin": "Lagos",
                "destination": "Abuja",
                "flight_date": "2021-12-25",
            },
            "seat_pref": "A1",
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        "data": {
            "customer_name": "John Doe",
            "customer_age": 25,
            "customer_email": "user@example.com",
            "customer_phone": "tel:+234-812-345-6789",
            "flight_origin": "Lagos",
            "flight_destination": "Abuja",
            "flight_date": "2021-12-25",
            "seat_preference": "A1",
        },
        "message": "Booking successful",
    }
