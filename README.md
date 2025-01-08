# Parking-Lot
A Parking Lot Design system
This repository contains a Python implementation of a parking lot management system that supports different vehicle types and parking fee models. It includes functionalities to park vehicles, unpark them, generate parking tickets and receipts, and calculate parking fees based on different fee models (such as mall, stadium, and airport).

Design Overview
Classes

ParkingSpot
Represents an individual parking spot in the parking lot.
Attributes:
spot_id: Unique identifier for the parking spot.
spot_type: Type of the parking spot (e.g., "car", "motorcycle").
is_free: Boolean indicating if the spot is free or occupied.

Vehicle
Represents a vehicle that is trying to park in the parking lot.
Attributes:
license_plate: Unique identifier for the vehicle.
vehicle_type: Type of the vehicle (e.g., "car", "motorcycle", "bus").

ParkingTicket

Represents a parking ticket issued when a vehicle parks in the lot.
Attributes:
ticket_id: Unique identifier for the ticket (auto-incremented).
vehicle: The vehicle for which the ticket is issued.
spot_id: The ID of the parking spot assigned to the vehicle.
entry_time: The time when the vehicle parks.

Receipt

Represents the receipt generated when a vehicle unparks and the fee is calculated.
Attributes:
receipt_id: Unique identifier for the receipt (auto-incremented).
ticket: The parking ticket associated with this receipt.
exit_time: The time when the vehicle leaves the parking lot.
parking_fee: The calculated parking fee for the duration of the parking.

FeeCalculator (Base Class)

A base class for calculating parking fees based on the vehicle type and duration.
It defines rates for different vehicle types (e.g., "motorcycle", "car", "bus").
StadiumFeeCalculator, MallFeeCalculator, AirportFeeCalculator

These are subclasses of FeeCalculator that implement specific fee calculation logic for different scenarios:
StadiumFeeCalculator: Uses custom rates based on parking duration (e.g., minimum charges for short durations, regular charges for longer stays).
MallFeeCalculator: A flat-rate model.
AirportFeeCalculator: Charges a flat rate for the first 5 hours and a regular hourly rate for additional hours.

ParkingLot

Represents the parking lot that holds parking spots, parking tickets, and receipts.
Methods:
add_spots: Adds parking spots of a particular type (e.g., "car", "motorcycle").
park_vehicle: Parks a vehicle in the first available spot and generates a parking ticket.
unpark_vehicle: Unparks a vehicle, calculates the parking fee, and generates a receipt.
Design Choices
Object-Oriented Design: The system is designed using Object-Oriented Programming (OOP) principles to maintain clarity and scalability. Each key entity (e.g., vehicle, parking spot, ticket) is represented by a class.

Auto-incrementing IDs: Both ParkingTicket and Receipt classes use class-level counters to auto-increment IDs for tickets and receipts. This helps in assigning unique IDs without manual intervention.

Inheritance: The FeeCalculator class is extended by StadiumFeeCalculator, MallFeeCalculator, and AirportFeeCalculator to cater to different fee calculation strategies. This follows the Open/Closed principle (part of SOLID principles), where the system can be extended with new fee models without modifying existing code.

Duration-Based Fee Calculation: The fee is calculated based on the duration the vehicle is parked, and different fee models provide variations on how the fees are calculated (e.g., flat rate, hourly rate, and special rates for certain durations).

Setup Instructions
Prerequisites
Ensure you have Python 3.x installed on your machine. You can check your Python version by running:

bash
Copy code
python --version
If Python is not installed, download and install it from python.org.

Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/yourusername/parking-lot-system.git
cd parking-lot-system
Install required libraries (if any). For this implementation, no external libraries are required, as it only depends on Python's built-in libraries.
Running the Code
To run the main program:
bash
Copy code
python parking2.py
This will demonstrate the usage of the MallFeeCalculator, StadiumFeeCalculator, and AirportFeeCalculator classes by calculating fees for different vehicles over various durations.

To run the unit tests:
bash
Copy code
python -m unittest test_parking_lot.py
This will execute all the test cases in the test_parking_lot.py file and show the results of your unit tests.

Expected Outputs
The main program will print out the calculated parking fees for different vehicles using different fee models.

The unit tests will verify the functionality of the system, including the creation of parking spots, parking tickets, receipts, and fee calculations.



Conclusion
This parking lot system is designed to handle various parking scenarios with different fee models and provides flexibility to easily extend it for other types of parking fee calculations. The system is modular, with clear separation between components, making it scalable and easy to maintain.
