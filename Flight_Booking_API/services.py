async def process_booking(booking):
    """
    Process the booking details, this is for the business logic
    """
    
    results = {
        "customer_name": booking.contact_details.name,
        "customer_age": booking.contact_details.age,
        "customer_email": booking.contact_details.email,
        "customer_phone": booking.contact_details.phone,
        "flight_origin": booking.flight_details.origin,
        "flight_destination": booking.flight_details.destination,
        "flight_date": booking.flight_details.flight_date.strftime("%Y-%m-%d"),
        "seat_preference": booking.seat_pref,
    }
    return results