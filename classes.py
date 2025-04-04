# -*- coding: utf-8 -*-
"""classes.ipynb

"""

from typing import List

# Parent class for Room Types
class Room:
    def __init__(self, room_number: int, room_type: str, amenities: List[str], price_per_night: float):
        # Initialize room attributes
        self._room_number = room_number  # Room number
        self._type = room_type            # Type of room (Standard, Deluxe, Suite)
        self._amenities = amenities        # List of amenities available in the room
        self._price_per_night = price_per_night  # Price per night for the room
        self._is_available = True          # Availability status of the room

    def get_room_number(self) -> int:
        return self._room_number  # Return the room number

    def set_room_number(self, room_number: int):
        self._room_number = room_number  # Set the room number

    def get_type(self) -> str:
        return self._type  # Return the type of room

    def set_type(self, room_type: str):
        self._type = room_type  # Set the type of room

    def get_amenities(self) -> List[str]:
        return self._amenities  # Return the list of amenities

    def set_amenities(self, amenities: List[str]):
        self._amenities = amenities  # Set the list of amenities

    def get_price_per_night(self) -> float:
        return self._price_per_night  # Return the price per night

    def set_price_per_night(self, price_per_night: float):
        self._price_per_night = price_per_night  # Set the price per night

    def is_available(self) -> bool:
        return self._is_available  # Return the availability status

    def set_available(self, is_available: bool):
        self._is_available = is_available  # Set the availability status

    def book_room(self) -> bool:
        # Book the room if available
        if self._is_available:
            self._is_available = False  # Mark room as booked
            return True
        return False  # Room is not available

    def check_out(self):
        self._is_available = True  # Mark room as available upon checkout

    def get_room_details(self) -> str:
        # Return a string with room details
        return f"Room Number: {self._room_number}, Type: {self._type}, Amenities: {', '.join(self._amenities)}, Price per Night: {self._price_per_night}"


class StandardRoom(Room):
    def __init__(self, room_number: int, amenities: List[str], price_per_night: float, bed_size: str, has_tv: bool, has_mini_fridge: bool):
        # Initialize StandardRoom attributes
        super().__init__(room_number, "Standard", amenities, price_per_night)  # Call parent constructor
        self._bed_size = bed_size  # Size of the bed
        self._has_tv = has_tv  # TV availability
        self._has_mini_fridge = has_mini_fridge  # Mini fridge availability

    def get_bed_size(self) -> str:
        return self._bed_size  # Return bed size

    def set_bed_size(self, bed_size: str):
        self._bed_size = bed_size  # Set bed size

    def has_tv(self) -> bool:
        return self._has_tv  # Return TV availability

    def set_has_tv(self, has_tv: bool):
        self._has_tv = has_tv  # Set TV availability

    def has_mini_fridge(self) -> bool:
        return self._has_mini_fridge  # Return mini fridge availability

    def set_has_mini_fridge(self, has_mini_fridge: bool):
        self._has_mini_fridge = has_mini_fridge  # Set mini fridge availability


class DeluxeRoom(Room):
    def __init__(self, room_number: int, amenities: List[str], price_per_night: float, bed_size: str, has_balcony: bool, has_jacuzzi: bool):
        # Initialize DeluxeRoom attributes
        super().__init__(room_number, "Deluxe", amenities, price_per_night)  # Call parent constructor
        self._bed_size = bed_size  # Size of the bed
        self._has_balcony = has_balcony  # Balcony availability
        self._has_jacuzzi = has_jacuzzi  # Jacuzzi availability

    def get_bed_size(self) -> str:
        return self._bed_size  # Return bed size

    def set_bed_size(self, bed_size: str):
        self._bed_size = bed_size  # Set bed size

    def has_balcony(self) -> bool:
        return self._has_balcony  # Return balcony availability

    def set_has_balcony(self, has_balcony: bool):
        self._has_balcony = has_balcony  # Set balcony availability

    def has_jacuzzi(self) -> bool:
        return self._has_jacuzzi  # Return jacuzzi availability

    def set_has_jacuzzi(self, has_jacuzzi: bool):
        self._has_jacuzzi = has_jacuzzi  # Set jacuzzi availability


class SuiteRoom(Room):
    def __init__(self, room_number: int, amenities: List[str], price_per_night: float, has_living_area: bool, has_kitchen: bool, has_private_pool: bool):
        # Initialize SuiteRoom attributes
        super().__init__(room_number, "Suite", amenities, price_per_night)  # Call parent constructor
        self._has_living_area = has_living_area  # Living area availability
        self._has_kitchen = has_kitchen  # Kitchen availability
        self._has_private_pool = has_private_pool  # Private pool availability

    def has_living_area(self) -> bool:
        return self._has_living_area  # Return living area availability

    def set_has_living_area(self, has_living_area: bool):
        self._has_living_area = has_living_area  # Set living area availability

    def has_kitchen(self) -> bool:
        return self._has_kitchen  # Return kitchen availability

    def set_has_kitchen(self, has_kitchen: bool):
        self._has_kitchen = has_kitchen  # Set kitchen availability

    def has_private_pool(self) -> bool:
        return self._has_private_pool  # Return private pool availability

    def set_has_private_pool(self, has_private_pool: bool):
        self._has_private_pool = has_private_pool  # Set private pool availability


class Guest:
    def __init__(self, name: str, email:str, contact_info: str, loyalty_status: str):
        # Initialize guest attributes
        self._name = name  # Guest's name
        self._contact_info = contact_info  # Guest's contact information
        self._loyalty_status = loyalty_status  # Guest's loyalty status
        self._booking_history = []  # List to store booking history
        self._loyalty_points = 0  # Loyalty points

    def get_name(self) -> str:
        return self._name  # Return guest's name

    def set_name(self, name: str):
        self._name = name  # Set guest's name

    def get_contact_info(self) -> str:
        return self._contact_info  # Return guest's contact information

    def set_contact_info(self, contact_info: str):
        self._contact_info = contact_info  # Set guest's contact information

    def get_loyalty_status(self) -> str:
        return self._loyalty_status  # Return guest's loyalty status

    def set_loyalty_status(self, loyalty_status: str):
        self._loyalty_status = loyalty_status  # Set guest's loyalty status

    def add_booking(self, booking: 'Booking'):
        self._booking_history.append(booking)  # Add booking to history

    def get_booking_history(self) -> List['Booking']:
        return self._booking_history  # Return booking history

    def get_loyalty_points(self) -> int:
        return self._loyalty_points  # Return loyalty points

    def set_loyalty_points(self, loyalty_points: int):
        self._loyalty_points = loyalty_points  # Set loyalty points

    def redeem_loyalty_points(self, points: int) -> bool:
        # Redeem loyalty points if sufficient points are available
        if points <= self._loyalty_points:
            self._loyalty_points -= points  # Deduct points
            return True
        return False  # Not enough points


class Booking:
    def __init__(self, booking_id: int, room: Room, guest: Guest, check_in_date: str, check_out_date: str):
        # Initialize booking attributes
        self._booking_id = booking_id  # Unique identifier for the booking
        self._room = room  # The room being booked
        self._guest = guest  # The guest making the booking
        self._check_in_date = check_in_date  # Check-in date for the booking
        self._check_out_date = check_out_date  # Check-out date for the booking
        self._total_price = self.calculate_total_price()  # Calculate total price based on stay duration

    def get_booking_id(self) -> int:
        return self._booking_id  # Return the booking ID

    def set_booking_id(self, booking_id: int):
        self._booking_id = booking_id  # Set the booking ID

    def get_room(self) -> Room:
        return self._room  # Return the room associated with the booking

    def set_room(self, room: Room):
        self._room = room  # Set the room for the booking

    def get_guest(self) -> Guest:
        return self._guest  # Return the guest associated with the booking

    def set_guest(self, guest: Guest):
        self._guest = guest  # Set the guest for the booking

    def get_check_in_date(self) -> str:
        return self._check_in_date  # Return the check-in date

    def set_check_in_date(self, check_in_date: str):
        self._check_in_date = check_in_date  # Set the check-in date

    def get_check_out_date(self) -> str:
        return self._check_out_date  # Return the check-out date

    def set_check_out_date(self, check_out_date: str):
        self._check_out_date = check_out_date  # Set the check-out date

    def get_total_price(self) -> float:
        return self._total_price  # Return the total price for the booking

    def calculate_total_price(self) -> float:
        from datetime import datetime  # Import datetime for date calculations
        check_in = datetime.strptime(self._check_in_date, '%Y-%m-%d')  # Convert check-in date string to datetime
        check_out = datetime.strptime(self._check_out_date, '%Y-%m-%d')  # Convert check-out date string to datetime
        days = (check_out - check_in).days  # Calculate the number of days between check-in and check-out
        return days * self._room.get_price_per_night()  # Calculate total price based on room price per night


class Payment:
    def __init__(self, payment_id: int, booking: Booking, amount: float, payment_method: str):
        # Initialize payment attributes
        self._payment_id = payment_id  # Unique identifier for the payment
        self._booking = booking  # The booking associated with this payment
        self._amount = amount  # Amount to be paid
        self._payment_method = payment_method  # Method of payment (e.g., Credit Card, Cash)
        self._payment_status = "Pending"  # Initial payment status

    def get_payment_id(self) -> int:
        return self._payment_id  # Return the payment ID

    def set_payment_id(self, payment_id: int):
        self._payment_id = payment_id  # Set the payment ID

    def get_booking(self) -> Booking:
        return self._booking  # Return the booking associated with this payment

    def set_booking(self, booking: Booking):
        self._booking = booking  # Set the booking for this payment

    def get_amount(self) -> float:
        return self._amount  # Return the amount to be paid

    def set_amount(self, amount: float):
        self._amount = amount  # Set the amount to be paid

    def get_payment_method(self) -> str:
        return self._payment_method  # Return the payment method

    def set_payment_method(self, payment_method: str):
        self._payment_method = payment_method  # Set the payment method

    def get_payment_status(self) -> str:
        return self._payment_status  # Return the payment status

    def set_payment_status(self, payment_status: str):
        self._payment_status = payment_status  # Set the payment status

    def process_payment(self) -> bool:
        self._payment_status = "Completed"  # Mark the payment as completed
        return True  # Indicate that the payment was processed successfully


class LoyaltyProgram:
    def __init__(self, program_id: int, guest: Guest, points_earned: int, reward: str):
        # Initialize loyalty program attributes
        self._program_id = program_id  # Unique identifier for the loyalty program
        self._guest = guest  # Guest enrolled in the program
        self._points_earned = points_earned  # Points accumulated by the guest
        self._reward = reward  # Loyalty tier level (e.g., Silver, Gold, Platinum)
        self._discount_percentage = 0.0  # Discount percentage based on the tier level
        self._expiry_date = None  # Expiry date for loyalty points

    def get_program_id(self) -> int:
        # Retrieve the program ID
        return self._program_id

    def set_program_id(self, program_id: int):
        # Set a new program ID
        self._program_id = program_id

    def get_guest(self) -> Guest:
        # Retrieve the guest enrolled in the program
        return self._guest

    def set_guest(self, guest: Guest):
        # Set a new guest for the loyalty program
        self._guest = guest

    def get_points_earned(self) -> int:
        # Retrieve the number of points earned by the guest
        return self._points_earned

    def set_points_earned(self, points: int):
        # Update the points earned by the guest
        self._points_earned = points

    def get_Rewards(self) -> str:
        # Retrieve the guest's tier level in the loyalty program
        return self._tier_level

    def set_Rewards(self, reward: str):
        # Update the guest's tier level
        self._tier_level = reward

    def get_discount_percentage(self) -> float:
        # Retrieve the discount percentage based on the guest's tier level
        return self._discount_percentage

    def set_discount_percentage(self, discount: float):
        # Set a new discount percentage for the guest's tier level
        self._discount_percentage = discount

    def get_expiry_date(self):
        # Retrieve the expiry date of the loyalty points
        return self._expiry_date

    def set_expiry_date(self, expiry_date: str):
        # Set a new expiry date for the loyalty points
        self._expiry_date = expiry_date

class GuestServiceRequest:
    def __init__(self, request_id: int, guest: Guest, service_type: str):
        # Initialize guest service request attributes
        self._request_id = request_id  # Unique identifier for the service request
        self._guest = guest  # The guest making the request
        self._service_type = service_type  # Type of service requested
        self._status = "Pending"  # Initial status of the request

    def get_request_id(self) -> int:
        return self._request_id  # Return the request ID

    def set_request_id(self, request_id: int):
        self._request_id = request_id  # Set the request ID

    def get_guest(self) -> Guest:
        return self._guest  # Return the guest associated with this request

    def set_guest(self, guest: Guest):
        self._guest = guest  # Set the guest for this request

    def get_service_type(self) -> str:
        return self._service_type  # Return the type of service requested

    def set_service_type(self, service_type: str):
        self._service_type = service_type  # Set the type of service requested

    def get_status(self) -> str:
        return self._status  # Return the status of the request

    def set_status(self, status: str):
        self._status = status  # Set the status of the request

    def update_status(self, status: str):
        self._status = status  # Update the status of the request


class Feedback:
    def __init__(self, feedback_id: int, guest: Guest, booking: Booking, rating: int, comments: str):
        # Initialize feedback attributes
        self._feedback_id = feedback_id  # Unique identifier for the feedback
        self._guest = guest  # Guest who provided the feedback
        self._booking = booking  # Booking associated with the feedback
        self._rating = rating  # Rating given by the guest (e.g., 1-5 stars)
        self._comments = comments  # Comments or feedback provided by the guest
        self._feedback_date = None  # Date when the feedback was submitted
        self._response_from_hotel = None  # Response from the hotel regarding the feedback
        self._resolved_status = "Unresolved"  # Status indicating whether the feedback is resolved or not

    def get_feedback_id(self) -> int:
        # Returns the unique feedback ID
        return self._feedback_id

    def set_feedback_id(self, feedback_id: int):
        # Sets a new feedback ID
        self._feedback_id = feedback_id

    def get_guest(self) -> Guest:
        # Returns the guest who provided the feedback
        return self._guest

    def set_guest(self, guest: Guest):
        # Updates the guest associated with the feedback
        self._guest = guest

    def get_booking(self) -> Booking:
        # Returns the booking related to the feedback
        return self._booking

    def set_booking(self, booking: Booking):
        # Sets a new booking reference for the feedback
        self._booking = booking

    def get_rating(self) -> int:
        # Returns the rating given in the feedback
        return self._rating

    def set_rating(self, rating: int):
        # Updates the rating given by the guest
        self._rating = rating

    def get_comments(self) -> str:
        # Returns the feedback comments
        return self._comments

    def set_comments(self, comments: str):
        # Updates the feedback comments
        self._comments = comments

    def get_feedback_date(self):
        # Returns the date the feedback was submitted
        return self._feedback_date

    def set_feedback_date(self, date: str):
        # Sets the date the feedback was provided
        self._feedback_date = date

    def get_response_from_hotel(self):
        # Returns the hotel's response to the feedback
        return self._response_from_hotel

    def set_response_from_hotel(self, response: str):
        # Sets a response from the hotel
        self._response_from_hotel = response

    def get_resolved_status(self):
        # Returns the resolution status of the feedback
        return self._resolved_status

    def set_resolved_status(self, status: str):
        # Updates the resolution status (e.g., "Resolved" or "Unresolved")
        self._resolved_status = status

from typing import List

class Hotel:
    def __init__(self, hotel_id: int, name: str, address: str, phone_number: str):
        # Initialize hotel attributes
        self._hotel_id = hotel_id  # Unique ID for the hotel
        self._name = name  # Name of the hotel
        self._address = address  # Address of the hotel
        self._phone_number = phone_number  # Contact number of the hotel
        self._rooms = []  # List to store rooms in the hotel

    # --- Getter and Setter Methods ---

    def get_hotel_id(self) -> int:
        # Get the hotel ID
        return self._hotel_id

    def get_name(self) -> str:
        # Get the hotel's name
        return self._name

    def set_name(self, name: str):
        # Set the hotel's name
        self._name = name

    def get_address(self) -> str:
        # Get the hotel's address
        return self._address

    def set_address(self, address: str):
        # Set the hotel's address
        self._address = address

    def get_phone_number(self) -> str:
        # Get the hotel's phone number
        return self._phone_number

    def set_phone_number(self, phone_number: str):
        # Set the hotel's phone number
        self._phone_number = phone_number

    # --- Room Management Methods ---

    def add_room(self, room: 'Room'):
        # Add a room to the hotel's room list
        self._rooms.append(room)

    def remove_room(self, room: 'Room'):
        # Remove a room from the hotel's room list, if it exists
        if room in self._rooms:
            self._rooms.remove(room)

    def get_rooms(self) -> List['Room']:
        # Return the list of rooms in the hotel
        return self._rooms
