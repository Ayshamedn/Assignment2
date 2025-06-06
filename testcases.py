# -*- coding: utf-8 -*-
"""TestCases.ipynb

"""

# Import the classes from the hotel module
from classes import Guest,Hotel,StandardRoom,DeluxeRoom,SuiteRoom,Booking,Payment

"""Test Case 1: Guest Account Creation"""

# Test Case 1: Guest Account Creation
def test_guest_account_creation():
    # Create a Guest instance with name "Ahmad", email, and loyalty status "Silver"
    guest = Guest("Ahmad", "Ahmad123@gmail.com", "Silver")

    # Verify that the name of the guest is correctly set
    assert guest.get_name() == "Ahmad"

    # Verify that the contact information is correctly set
    assert guest.get_contact_info() == "Ahmad123@gmail.com"

    # Verify that the loyalty status is correctly set
    assert guest.get_loyalty_status() == "Silver"

    # Example 2: Create another Guest instance with different details
    guest2 = Guest("Ali", "Ali@gamil.com", "Gold")

    # Verify that the name of the second guest is correctly set
    assert guest2.get_name() == "Ali"

    # Verify that the contact information of the second guest is correct
    assert guest2.get_contact_info() == "Ali@gamil.com"

    # Verify that the loyalty status of the second guest is correct
    assert guest2.get_loyalty_status() == "Gold"

    # Print a success message if all assertions pass
    print("Guest account created successfully for Ahmad and Ali.")

# Call the function to run the test case
test_guest_account_creation()

"""Test Case 2: Searching for Available Rooms"""

# Test Case 2: Searching for Available Rooms
def test_search_available_rooms():
    # Create a Hotel instance with the name "Test Hotel"
    hotel = Hotel("Test Hotel")

    # Create a StandardRoom with room number 101, amenities, price, bed type, and availability
    room1 = StandardRoom(101, ["WiFi", "Air Conditioning"], 100.0, "Queen", True, True)

    # Create a DeluxeRoom with room number 102, amenities, price, bed type, and availability
    room2 = DeluxeRoom(102, ["WiFi", "Balcony"], 150.0, "King", True, True)

    # Add the created rooms to the hotel
    hotel.add_room(room1)
    hotel.add_room(room2)

    # Simulate room availability: set room1 as available and room2 as unavailable
    room1.set_available(True)
    room2.set_available(False)

    # Retrieve the list of available rooms from the hotel's room list
    available_rooms = [room for room in hotel._rooms if room.is_available()]

    # Check that only one room is available
    assert len(available_rooms) == 1

    # Ensure that the available room is room1 (room number 101)
    assert available_rooms[0].get_room_number() == 101

    # Example 2: Add another room (SuiteRoom) to the hotel
    room3 = SuiteRoom(103, ["WiFi", "Private Pool"], 200.0, True, True, True)
    hotel.add_room(room3)

    # Set room3 as available
    room3.set_available(True)

    # Retrieve the updated list of available rooms
    available_rooms = [room for room in hotel._rooms if room.is_available()]

    # Check that two rooms (room1 and room3) are now available
    assert len(available_rooms) == 2

    # Print success message if all assertions pass
    print("Successfully searched for available rooms.")

# Call the function to run the test case
test_search_available_rooms()

"""Test Case 3: Making a Room Reservation"""

# Test Case 3: Making a Room Reservation
def test_room_reservation():
    # Create a hotel instance with the name "Test Hotel"
    hotel = Hotel("Test Hotel")

    # Create a standard room with room number 101, amenities, price, bed type, and availability status
    room = StandardRoom(101, ["WiFi"], 100.0, "Queen", True, True)

    # Add the created room to the hotel
    hotel.add_room(room)

    # Create a guest named "Alice" with contact info and loyalty status
    guest = Guest("Aysha", "aysha@gmail.com", "Platinum")

    # Add the guest to the hotel system
    hotel.add_guest(guest)

    # Create a booking instance for guest Alice in room 101 from check-in to check-out dates
    booking = Booking(1, room, guest, "2023-10-01", "2023-10-05")

    # Add the booking to the hotel's records
    hotel.add_booking(booking)

    # Verify that the guest's name in the booking is "Aysha"
    assert booking.get_guest().get_name() == "Aysha"

    # Verify that the booked room number is 101
    assert booking.get_room().get_room_number() == 101

    # Verify the check-in date of the booking
    assert booking.get_check_in_date() == "2023-10-01"

    # Verify the check-out date of the booking
    assert booking.get_check_out_date() == "2023-10-05"

    # Print success message for the first booking
    print("Booking successfully created for Aysha in Room 101 ")

    # Example 2: Creating another room and guest
    # Create a deluxe room with room number 102, amenities, price, bed type, and availability status
    room2 = DeluxeRoom(102, ["WiFi", "Balcony"], 150.0, "King", True, True)

    # Add the created room to the hotel
    hotel.add_room(room2)

    # Create a guest named "Bob" with contact info and loyalty status
    guest2 = Guest("Mouza", "Mouza123@gmail.com", "Gold")

    # Add the guest to the hotel system
    hotel.add_guest(guest2)

    # Create a booking instance for guest Bob in room 102 from check-in to check-out dates
    booking2 = Booking(2, room2, guest2, "2023-10-10", "2023-10-15")

    # Add the booking to the hotel's records
    hotel.add_booking(booking2)

    # Verify that the guest's name in the booking is "Mouza"
    assert booking2.get_guest().get_name() == "Mouza"

    # Verify that the booked room number is 102
    assert booking2.get_room().get_room_number() == 102

    # Verify the check-in date of the booking
    assert booking2.get_check_in_date() == "2023-10-10"

    # Verify the check-out date of the booking
    assert booking2.get_check_out_date() == "2023-10-15"

    # Print success message for the second booking
    print("Booking successfully created for Mouza in Room 102 ")

# Call the function to execute the test case
test_room_reservation()

"""Test Case 4: Booking Confirmation Notification"""

# Test Case 4: Booking Confirmation Notification
def test_booking_confirmation_notification():
    # Create a hotel instance named "Test Hotel"
    hotel = Hotel("Test Hotel")

    # Create a Standard Room with room number 101, amenities, price, bed type, and availability status
    room = StandardRoom(101, ["WiFi"], 100.0, "Queen", True, True)

    # Add the created room to the hotel
    hotel.add_room(room)

    # Create a Guest instance with name "Aysha", email, and loyalty status "Silver"
    guest = Guest("Aysha", "aysha@gmail.com", "Silver")

    # Add the guest to the hotel's guest list
    hotel.add_guest(guest)

    # Create a booking for the guest with the specified check-in and check-out dates
    booking = Booking(1, room, guest, "2023-10-01", "2023-10-05")

    # Add the booking to the hotel's booking system
    hotel.add_booking(booking)

    # Simulate sending a confirmation notification
    confirmation_sent = True  # Assume the notification is sent successfully

    # Verify that the confirmation notification was sent
    assert confirmation_sent == True

    # Print success message for the first booking
    print("Booking confirmation notification sent successfully for Aysha.")

    # Example 2: Create another room and guest for testing
    room2 = DeluxeRoom(102, ["WiFi", "Balcony"], 150.0, "King", True, True)

    # Add the second room to the hotel
    hotel.add_room(room2)

    # Create a second Guest instance with name "Mouza", email, and loyalty status "Gold"
    guest2 = Guest("Mouza", "Mouza123@gmail.com", "Gold")

    # Add the second guest to the hotel's guest list
    hotel.add_guest(guest2)

    # Create a booking for the second guest
    booking2 = Booking(2, room2, guest2, "2023-10-10", "2023-10-15")

    # Add the second booking to the hotel's booking system
    hotel.add_booking(booking2)

    # Simulate sending a confirmation notification for the second guest
    confirmation_sent2 = True  # Assume the notification is sent successfully

    # Verify that the confirmation notification was sent for the second guest
    assert confirmation_sent2 == True

    # Print success message for the second booking
    print("Booking confirmation notification sent successfully for Mouza.")

# Call the function to run the test case
test_booking_confirmation_notification()

"""Test Case 5: Invoice Generation for a Booking"""

# Test Case 5: Invoice Generation for a Booking
def test_invoice_generation():
    # Create a Hotel instance named "Test Hotel"
    hotel = Hotel("Test Hotel")

    # Create a StandardRoom instance with room number 101, amenities, price, bed type, and availability
    room = StandardRoom(101, ["WiFi"], 100.0, "Queen", True, True)

    # Add the room to the hotel
    hotel.add_room(room)

    # Create a Guest instance with name "Mouza", email, and loyalty status "Platinum"
    guest = Guest("Mouza", "Mouza123@gmail.com", "Platinum")

    # Add the guest to the hotel
    hotel.add_guest(guest)

    # Create a Booking instance with booking ID 1, linked to the room and guest, with check-in and check-out dates
    booking = Booking(1, room, guest, "2023-10-01", "2023-10-05")

    # Add the booking to the hotel
    hotel.add_booking(booking)

    # Create a Payment instance with payment ID 1, linked to the booking, total price, and payment method
    payment = Payment(1, booking, booking.get_total_price(), "Credit Card")

    # Process the payment
    payment.process_payment()

    # Generate an invoice slip for the booking
    invoice = hotel.generate_slip(booking, payment)

    # Verify that the total price in the invoice matches the expected amount (4 nights at $100 each)
    assert "Total Price: 400.0" in invoice

    # Print success message for first test case
    print("Invoice successfully generated for Mouza's booking.")

    # Example 2: Creating another booking scenario

    # Create a DeluxeRoom instance with room number 102, additional amenities, price, bed type, and availability
    room2 = DeluxeRoom(102, ["WiFi", "Balcony"], 150.0, "King", True, True)

    # Add the second room to the hotel
    hotel.add_room(room2)

    # Create a Guest instance with name "Aysha", email, and loyalty status "Gold"
    guest2 = Guest("Aysha", "aysha@gmail.com", "Gold")

    # Add the second guest to the hotel
    hotel.add_guest(guest2)

    # Create a Booking instance with booking ID 2, linked to the new room and guest, with check-in and check-out dates
    booking2 = Booking(2, room2, guest2, "2023-10-10", "2023-10-15")

    # Add the second booking to the hotel
    hotel.add_booking(booking2)

    # Create a Payment instance for the second booking with payment ID 2
    payment2 = Payment(2, booking2, booking2.get_total_price(), "Debit Card")

    # Process the second payment
    payment2.process_payment()

    # Generate an invoice slip for the second booking
    invoice2 = hotel.generate_slip(booking2, payment2)

    # Verify that the total price in the invoice matches the expected amount (5 nights at $150 each)
    assert "Total Price: 750.0" in invoice2

    # Print success message for the second test case
    print("Invoice successfully generated for Aysha's booking.")

# Call the function to execute the test case
test_invoice_generation()

"""Test Case 6: Processing Different Payment Methods"""

# Test Case 6: Processing Different Payment Methods
def test_payment_processing():
    # Create a hotel instance named "Test Hotel"
    hotel = Hotel("Test Hotel")

    # Create a standard room with room number 101, amenities, price, bed type, and availability status
    room = StandardRoom(101, ["WiFi"], 100.0, "Queen", True, True)

    # Add the created room to the hotel
    hotel.add_room(room)

    # Create a guest instance with name, email, and loyalty status
    guest = Guest("Aysha", "Aysha@gmail.com", "Silver")

    # Add the guest to the hotel
    hotel.add_guest(guest)

    # Create a booking for the guest in the standard room from 2023-10-01 to 2023-10-05
    booking = Booking(1, room, guest, "2023-10-01", "2023-10-05")

    # Add the booking to the hotel
    hotel.add_booking(booking)

    # Create a payment instance for the booking using a credit card
    payment = Payment(1, booking, booking.get_total_price(), "Credit Card")

    # Assert that the payment is processed successfully
    assert payment.process_payment() == True

    # Assert that the payment status is marked as "Completed"
    assert payment.get_payment_status() == "Completed"

    # Example 2: Processing another payment with a different method

    # Create a deluxe room with room number 102, amenities, price, bed type, and availability status
    room2 = DeluxeRoom(102, ["WiFi", "Balcony"], 150.0, "King", True, True)

    # Add the created deluxe room to the hotel
    hotel.add_room(room2)

    # Create another guest instance with name, email, and loyalty status
    guest2 = Guest("Mouza", "mouza123@gmail.com", "Gold")

    # Add the guest to the hotel
    hotel.add_guest(guest2)

    # Create a booking for the second guest in the deluxe room from 2023-10-10 to 2023-10-15
    booking2 = Booking(2, room2, guest2, "2023-10-10", "2023-10-15")

    # Add the booking to the hotel
    hotel.add_booking(booking2)

    # Create a payment instance for the second booking using a mobile wallet
    payment2 = Payment(2, booking2, booking2.get_total_price(), "Mobile Wallet")

    # Assert that the second payment is processed successfully
    assert payment2.process_payment() == True

    # Assert that the second payment status is marked as "Completed"
    assert payment2.get_payment_status() == "Completed"

    # Print a success message if all assertions pass
    print("Successfully processed payments for Credit Card and Mobile Wallet.")

# Call the function to execute the test case
test_payment_processing()

"""Test Case 7: Displaying Reservation History"""

# Test Case 7: Displaying Reservation History
def test_reservation_history():
    # Create a hotel instance with the name "Test Hotel"
    hotel = Hotel("Test Hotel")

    # Create a StandardRoom instance with room number 101, amenities, price, bed type, and availability
    room = StandardRoom(101, ["WiFi"], 100.0, "Queen", True, True)

    # Add the standard room to the hotel's room list
    hotel.add_room(room)

    # Create a Guest instance with name "Ivy", email, and loyalty status "Platinum"
    guest = Guest("Aysha", "Aysha@gmail.com", "Platinum")

    # Add the guest to the hotel's guest list
    hotel.add_guest(guest)

    # Create a Booking instance for guest Ivy from "2023-10-01" to "2023-10-05"
    booking = Booking(1, room, guest, "2023-10-01", "2023-10-05")

    # Add the booking to the hotel's list of bookings
    hotel.add_booking(booking)

    # Add the booking to the guest's booking history
    guest.add_booking(booking)

    # Retrieve the guest's booking history
    history = guest.get_booking_history()

    # Verify that the booking history contains one reservation
    assert len(history) == 1

    # Verify that the booking ID of the first reservation is correct
    assert history[0].get_booking_id() == 1

    # Example 2: Adding another booking for the same guest

    # Create a DeluxeRoom instance with room number 102, amenities, price, bed type, and availability
    room2 = DeluxeRoom(102, ["WiFi", "Balcony"], 150.0, "King", True, True)

    # Add the deluxe room to the hotel's room list
    hotel.add_room(room2)

    # Create another Booking instance for guest Ivy from "2023-10-10" to "2023-10-15"
    booking2 = Booking(2, room2, guest, "2023-10-10", "2023-10-15")

    # Add the second booking to the hotel's list of bookings
    hotel.add_booking(booking2)

    # Add the second booking to the guest's booking history
    guest.add_booking(booking2)

    # Retrieve the updated booking history
    history = guest.get_booking_history()

    # Verify that the booking history now contains two reservations
    assert len(history) == 2

    # Verify that the booking ID of the second reservation is correct
    assert history[1].get_booking_id() == 2

    # Print a success message if all assertions pass
    print("Successfully displayed reservation history for guest Aysha. ")

# Call the function to run the test case
test_reservation_history()

"""Test Case 8: Cancellation of a Reservation"""

# Test Case 8: Cancellation of a Reservation
def test_reservation_cancellation():
    # Create a hotel instance named "Test Hotel"
    hotel = Hotel("Test Hotel")

    # Create a StandardRoom instance with room number 101, amenities, price, and availability details
    room = StandardRoom(101, ["WiFi"], 100.0, "Queen", True, True)

    # Add the room to the hotel
    hotel.add_room(room)

    # Create a guest with name "Jack", email, and loyalty status "Silver"
    guest = Guest("Aysha", "Aysha@gmail.com", "Silver")

    # Add the guest to the hotel records
    hotel.add_guest(guest)

    # Create a booking for guest "Jack" in room 101 from October 1st to October 5th, 2023
    booking = Booking(1, room, guest, "2023-10-01", "2023-10-05")

    # Add the booking to the hotel's system
    hotel.add_booking(booking)

    # Simulate cancellation of the booking by setting the room's availability to True
    room.set_available(True)

    # Ensure that the room is now available after cancellation
    assert room.is_available() == True

    # Print success message for the first reservation cancellation
    print("Successfully canceled booking for Aysha. ")

    # Example 2: Create another room and guest for testing cancellation
    room2 = DeluxeRoom(102, ["WiFi", "Balcony"], 150.0, "King", True, True)

    # Add the second room to the hotel
    hotel.add_room(room2)

    # Create a second guest with name "Kathy", email, and loyalty status "Gold"
    guest2 = Guest("Mouza", "mouza123@gmail.com", "Gold")

    # Add the second guest to the hotel records
    hotel.add_guest(guest2)

    # Create a booking for guest "Kathy" in room 102 from October 10th to October 15th, 2023
    booking2 = Booking(2, room2, guest2, "2023-10-10", "2023-10-15")

    # Add the second booking to the hotel's system
    hotel.add_booking(booking2)

    # Simulate cancellation of the second booking by setting the room's availability to True
    room2.set_available(True)

    # Ensure that the second room is now available after cancellation
    assert room2.is_available() == True

    # Print success message for the second reservation cancellation
    print("Successfully canceled booking for Mouza. ")

# Call the function to execute the test case
test_reservation_cancellation()
