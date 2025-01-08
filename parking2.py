from datetime import datetime, timedelta

# Class for ParkingSpot
class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_free = True

# Class for Vehicle
class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

# Class for ParkingTicket
class ParkingTicket:
    _id_counter = 1  # Class-level attribute for auto-incrementing ID

    def __init__(self, vehicle, spot_id, entry_time):
        self.ticket_id = ParkingTicket._id_counter  # Assign the current counter value
        ParkingTicket._id_counter += 1  # Increment the counter
        self.vehicle = vehicle
        self.spot_id = spot_id
        self.entry_time = entry_time

    def __str__(self):
        return (f"Ticket Number: {self.ticket_id}\n"
                f"Spot Number: {self.spot_id}\n"
                f"Entry Date-Time: {self.entry_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

# Class for Receipt
class Receipt:
    _id_counter = 1  # Class-level counter for auto-incrementing IDs

    def __init__(self, ticket, exit_time, parking_fee):
        self.receipt_id = Receipt._id_counter  # Assign the current counter value
        Receipt._id_counter += 1  # Increment the counter
        self.ticket = ticket  # The associated parking ticket
        self.exit_time = exit_time
        self.parking_fee = parking_fee

    def __str__(self):
        return (f"Receipt Number: {self.receipt_id}\n"
                f"Entry Date-Time: {self.ticket.entry_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Exit Date-Time: {self.exit_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Parking Fees: ₹{self.parking_fee}")

# Class for Fee Calculation
class FeeCalculator:
    def __init__(self):
        self.rates = {
            "motorcycle": 10,  # ₹10 per hour
            "car": 20,         # ₹20 per hour
            "bus": 50          # ₹50 per hour
        }

    def calculate_fee(self, vehicle_type, duration_hours):
        rate = self.rates.get(vehicle_type, 0)  # Default rate is ₹0 for unknown types
        return rate * duration_hours

class StadiumFeeCalculator(FeeCalculator):
    def calculate_fee(self, vehicle_type, duration_hours):
        rate = self.rates.get(vehicle_type, 0)  # Default rate is ₹0 for unknown types
        if duration_hours <= 2:
            return rate * 2  # Minimum charge for 2 hours
        elif duration_hours <= 5:
            return rate * 3  # Fixed rate for 3-5 hours
        else:
            return rate * (duration_hours - 2)  # Normal rate after first 2 hours

class MallFeeCalculator(FeeCalculator):
    pass  # Inherits everything from FeeCalculator without changes

class AirportFeeCalculator(FeeCalculator):
    def calculate_fee(self, vehicle_type, duration_hours):
        rate = self.rates.get(vehicle_type, 0)  # Default rate is ₹0 for unknown types
        if duration_hours <= 5:
            return rate * 5  # Flat rate for up to 5 hours
        else:
            remaining_hours = duration_hours - 5
            return (rate * 5) + (rate * remaining_hours)

# Class for ParkingLot
class ParkingLot:
    _receipt_id_counter = 1  # Class-level counter for receipts

    def __init__(self, location):
        self.location = location
        self.spots = []
        self.tickets = {}
        self.receipts = {}

    def add_spots(self, spot_type, count):
        for i in range(1, count + 1):
            self.spots.append(ParkingSpot(f"{spot_type}-{i}", spot_type))

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.is_free and spot.spot_type == vehicle.vehicle_type:
                spot.is_free = False
                ticket = ParkingTicket(vehicle, spot.spot_id, datetime.now())
                self.tickets[ticket.ticket_id] = ticket
                return ticket
        raise Exception("No available spots for this vehicle type.")

    def unpark_vehicle(self, ticket_id):
        if ticket_id not in self.tickets:
            raise Exception("Invalid ticket.")
        ticket = self.tickets.pop(ticket_id)

        # Free the parking spot
        spot = next(spot for spot in self.spots if spot.spot_id == ticket.spot_id)
        spot.is_free = True

        # Calculate fees
        exit_time = datetime.now()
        duration = (exit_time - ticket.entry_time).seconds // 3600
        fees = FeeCalculator().calculate_fee(ticket.vehicle.vehicle_type, duration)

        # Generate receipt
        receipt = Receipt(ticket, exit_time, fees)

        self.receipts[receipt.receipt_id] = receipt
        return receipt

# Main Program
if __name__ == "__main__":
    # Mall Fee Model
    mall_fee_model = MallFeeCalculator()
    print("Mall Fee (Car, 6 hours): ₹", mall_fee_model.calculate_fee("car", 6))

    # Stadium Fee Model
    stadium_fee_model = StadiumFeeCalculator()
    print("Stadium Fee (Motorcycle, 4 hours): ₹", stadium_fee_model.calculate_fee("motorcycle", 4))

    # Airport Fee Model
    airport_fee_model = AirportFeeCalculator()
    print("Airport Fee (Bus, 28 hours): ₹", airport_fee_model.calculate_fee("bus", 28))

