import unittest
from datetime import datetime, timedelta
from parking2 import ParkingLot, Vehicle, FeeCalculator, MallFeeCalculator, StadiumFeeCalculator, ParkingTicket, ParkingSpot, Receipt, AirportFeeCalculator

class TestParkingSpot(unittest.TestCase):
    def test_parking_spot_creation(self):
        spot = ParkingSpot("car-1", "car")
        self.assertEqual(spot.spot_id, "car-1")
        self.assertEqual(spot.spot_type, "car")
        self.assertTrue(spot.is_free)

class TestVehicle(unittest.TestCase):
    def test_vehicle_creation(self):
        vehicle = Vehicle("ABC123", "car")
        self.assertEqual(vehicle.license_plate, "ABC123")
        self.assertEqual(vehicle.vehicle_type, "car")

class TestParkingTicket(unittest.TestCase):
    def setUp(self):
        # Reset the ticket ID counter before each test
        ParkingTicket._id_counter = 1

    def test_ticket_creation(self):
        vehicle = Vehicle("DEF456", "motorcycle")
        ticket = ParkingTicket(vehicle, "motorcycle-1", datetime(2025, 1, 8, 12, 0, 0))
        self.assertEqual(ticket.ticket_id, 1)  # Assert ticket ID is 1
        self.assertEqual(ticket.spot_id, "motorcycle-1")
        self.assertEqual(ticket.vehicle, vehicle)
        self.assertEqual(ticket.entry_time, datetime(2025, 1, 8, 12, 0, 0))

class TestReceipt(unittest.TestCase):
    def test_receipt_creation(self):
        vehicle = Vehicle("GHI789", "bus")
        ticket = ParkingTicket(vehicle, "bus-1", datetime(2025, 1, 8, 10, 0, 0))
        receipt = Receipt(ticket, datetime(2025, 1, 8, 15, 0, 0), 250)
        self.assertEqual(receipt.receipt_id, 1)
        self.assertEqual(receipt.ticket, ticket)
        self.assertEqual(receipt.exit_time, datetime(2025, 1, 8, 15, 0, 0))
        self.assertEqual(receipt.parking_fee, 250)

class TestFeeCalculators(unittest.TestCase):
    def test_fee_calculator(self):
        calculator = FeeCalculator()
        self.assertEqual(calculator.calculate_fee("car", 3), 60)

    def test_stadium_fee_calculator(self):
        calculator = StadiumFeeCalculator()
        self.assertEqual(calculator.calculate_fee("motorcycle", 4), 30)

    def test_mall_fee_calculator(self):
        calculator = MallFeeCalculator()
        self.assertEqual(calculator.calculate_fee("bus", 5), 250)

    def test_airport_fee_calculator(self):
        calculator = AirportFeeCalculator()
        self.assertEqual(calculator.calculate_fee("car", 6), 120)

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        # Initialize parking lot and add spots
        self.parking_lot = ParkingLot("mall")
        self.parking_lot.add_spots("car", 5)
        self.parking_lot.add_spots("motorcycle", 5)

    def test_add_spots(self):
        # Ensure 5 car spots and 5 motorcycle spots
        self.assertEqual(len(self.parking_lot.spots), 10)

    def test_park_vehicle(self):
        vehicle = Vehicle("JKL101", "car")
        ticket = self.parking_lot.park_vehicle(vehicle)
        self.assertEqual(ticket.vehicle, vehicle)
        self.assertEqual(ticket.spot_id, "car-1")

    def test_unpark_vehicle(self):
        vehicle = Vehicle("MNO102", "car")
        ticket = self.parking_lot.park_vehicle(vehicle)
        receipt = self.parking_lot.unpark_vehicle(ticket.ticket_id)
        self.assertEqual(receipt.ticket, ticket)
        self.assertTrue(any(spot.is_free for spot in self.parking_lot.spots if spot.spot_id == ticket.spot_id))

if __name__ == "__main__":
    unittest.main()
