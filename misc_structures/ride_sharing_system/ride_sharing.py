"""
Ride Sharing System

Implement the methods below to pass all tests across 4 levels.
See README.md for detailed requirements for each level.

Tips:
- Start with Level 1 and progress sequentially
- Later levels may require refactoring earlier code
- Use Python's standard library
- Focus on correctness over code quality
"""


class RideSharingSystem:
    """
    A ride sharing system that handles drivers, riders, ride requests,
    pricing, ratings, and ride history.
    """

    def __init__(self):
        """Initialize the ride sharing system."""
        self.drivers = {}
        self.riders = {}
        self.rides = {}
        self.available = set()
        self.surge_multiplier = 1
        self.ride_id = 0

    # ==================== LEVEL 1: Drivers and Riders ====================

    def register_driver(self, driver_id: str, name: str, vehicle_type: str) -> bool:
        """
        Register a new driver in the system.

        Args:
            driver_id: Unique identifier for the driver
            name: Name of the driver
            vehicle_type: Type of vehicle ("standard", "premium", "xl")

        Returns:
            True if driver was registered, False if driver_id already exists
            or invalid vehicle_type
        """
        if driver_id in self.drivers:
            return False
        if vehicle_type not in ("standard", "premium", "xl"):
            return False
        self.drivers[driver_id] = {"name": name,
                                   "vehicle_type": vehicle_type, "ratings": [], "ride_ids": []}
        return True

    def register_rider(self, rider_id: str, name: str) -> bool:
        """
        Register a new rider in the system.

        Args:
            rider_id: Unique identifier for the rider
            name: Name of the rider

        Returns:
            True if rider was registered, False if rider_id already exists
        """
        if rider_id in self.riders:
            return False
        self.riders[rider_id] = {"name": name,
                                 "current_ride_id": None, "ride_ids": []}
        return True

    def set_driver_availability(self, driver_id: str, is_available: bool) -> bool:
        """
        Set a driver's availability status.

        Args:
            driver_id: Unique identifier for the driver
            is_available: True if driver is going online, False if offline

        Returns:
            True if status was updated, False if driver doesn't exist
        """
        if driver_id not in self.drivers:
            return False
        self.drivers[driver_id]["available"] = is_available
        if is_available:
            self.available.add(driver_id)
        else:
            self.available.discard(driver_id)
        return True

    def get_available_driver_ids(self, vehicle_type: str = None) -> list:
        return sorted([(self.drivers[driver_id]["name"], driver_id) for driver_id in self.available if vehicle_type is None or self.drivers[driver_id]["vehicle_type"] == vehicle_type])

    def get_available_drivers(self, vehicle_type: str = None) -> list:
        """
        Get all available (online) drivers.

        Args:
            vehicle_type: Optional filter by vehicle type

        Returns:
            List of driver names sorted alphabetically
        """
        return [driver_info[0] for driver_info in self.get_available_driver_ids(vehicle_type)]

    # ==================== LEVEL 2: Ride Requests and Matching ====================

    def request_ride(self, rider_id: str, pickup: str, dropoff: str,
                     vehicle_type: str = "standard") -> str:
        """
        Request a new ride.

        Args:
            rider_id: Unique identifier for the rider
            pickup: Pickup location
            dropoff: Dropoff location
            vehicle_type: Type of vehicle requested (default: "standard")

        Returns:
            ride_id if successful, None if failed

        Failure conditions:
            - Rider doesn't exist
            - No available drivers for the vehicle type
            - Rider already has an active ride
        """
        if rider_id not in self.riders:
            return None
        if self.riders[rider_id]["current_ride_id"] is not None:
            return None
        self.ride_id += 1
        ride_id = self.ride_id
        self.riders[rider_id]["ride_ids"].append(ride_id)
        self.riders[rider_id]["current_ride_id"] = ride_id
        self.rides[ride_id] = {
            "rider_id": rider_id, "pickup": pickup, "dropoff": dropoff, "vehicle_type": vehicle_type, "status": "requested", "surge_multiplier": self.surge_multiplier}
        available_drivers = self.get_available_driver_ids(vehicle_type)
        success = False
        for _, driver_id in available_drivers:
            success = self.set_driver_availability(driver_id, False)
            if success:
                break
        if not success:
            # No driver available - mark ride as cancelled and unblock rider
            self.rides[ride_id]["status"] = "cancelled"
            self.riders[rider_id]["current_ride_id"] = None
            return None
        self.drivers[driver_id]["ride_ids"].append(ride_id)
        self.rides[ride_id].update({"driver_id": driver_id, })
        return ride_id

    def start_ride(self, ride_id: str) -> bool:
        """
        Start a ride (driver picked up the rider).

        Args:
            ride_id: Unique identifier for the ride

        Returns:
            True if successful, False otherwise

        Failure conditions:
            - Ride doesn't exist
            - Ride is not in "requested" status
        """
        if ride_id not in self.rides:
            return False
        if self.rides[ride_id]["status"] != "requested":
            return False
        self.rides[ride_id]["status"] = "in_progress"
        return True

    def free_parties_from_ride_id(self, ride_id):
        if "driver_id" in self.rides[ride_id]:
            driver_id = self.rides[ride_id]["driver_id"]
            self.set_driver_availability(driver_id, True)
        if "rider_id" in self.rides[ride_id]:
            rider_id = self.rides[ride_id]["rider_id"]
            self.riders[rider_id]["current_ride_id"] = None

    def complete_ride(self, ride_id: str, distance_km: float) -> bool:
        """
        Complete a ride.

        Args:
            ride_id: Unique identifier for the ride
            distance_km: Distance traveled in kilometers

        Returns:
            True if successful, False otherwise

        Failure conditions:
            - Ride doesn't exist
            - Ride is not in "in_progress" status
        """
        if ride_id not in self.rides:
            return False
        if self.rides[ride_id]["status"] != "in_progress":
            return False
        self.rides[ride_id]["status"] = "completed"
        self.rides[ride_id]["distance_km"] = distance_km
        self.free_parties_from_ride_id(ride_id)
        return True

    def get_ride_status(self, ride_id: str) -> str:
        """
        Get the status of a ride.

        Args:
            ride_id: Unique identifier for the ride

        Returns:
            Status string ("requested", "in_progress", "completed", "cancelled")
            or None if ride doesn't exist
        """
        if ride_id not in self.rides:
            return None
        return self.rides[ride_id]["status"]

    # ==================== LEVEL 3: Pricing and Ratings ====================

    def set_surge_multiplier(self, multiplier: float) -> bool:
        """
        Set the current surge pricing multiplier.

        Args:
            multiplier: Surge multiplier (must be >= 1.0)

        Returns:
            True if set successfully, False if multiplier < 1.0
        """
        if multiplier < 1:
            return False
        self.surge_multiplier = multiplier
        return True

    def get_ride_fare(self, ride_id: str, driver_fare=False) -> float:
        """
        Get the fare for a completed ride.

        Args:
            ride_id: Unique identifier for the ride

        Returns:
            Fare amount as float, or None if ride doesn't exist or not completed
        """
        if ride_id not in self.rides:
            return None
        status = self.rides[ride_id]["status"]
        if status == "completed":
            vehicle_type = self.rides[ride_id]["vehicle_type"]
            distance_km = self.rides[ride_id]["distance_km"]
            if vehicle_type == "standard":
                fare = 2.5+1.5*distance_km
            elif vehicle_type == "premium":
                fare = 5+2.5*distance_km
            elif vehicle_type == "xl":
                fare = 4+2*distance_km
            else:
                print(f"Vehicle type {vehicle_type} not identified")
                return None
            fare *= self.rides[ride_id]["surge_multiplier"]
            if driver_fare:
                fare *= 0.75
        elif status == "cancelled":
            if "driver_id" in self.rides[ride_id] and driver_fare:
                fare = 5
            else:
                return None
        else:
            return None
        return fare

    def rate_driver(self, ride_id: str, rating: int) -> bool:
        """
        Rate a driver after a completed ride.

        Args:
            ride_id: Unique identifier for the ride
            rating: Rating from 1 to 5 stars

        Returns:
            True if rating was recorded, False otherwise

        Failure conditions:
            - Ride doesn't exist
            - Ride is not completed
            - Rating is not 1-5
            - Ride has already been rated
        """
        if ride_id not in self.rides or self.rides[ride_id]["status"] != "completed":
            return False
        if "rating" in self.rides[ride_id]:
            return False
        if rating < 1 or rating > 5:
            return False
        self.rides[ride_id]["rating"] = rating
        driver_id = self.rides[ride_id]["driver_id"]
        self.drivers[driver_id]["ratings"].append(rating)
        return True

    def get_driver_rating(self, driver_id: str) -> float:
        """
        Get the average rating for a driver.

        Args:
            driver_id: Unique identifier for the driver

        Returns:
            Average rating as float, or None if driver doesn't exist
            or has no ratings
        """
        if driver_id not in self.drivers:
            return None
        ratings = self.drivers[driver_id]["ratings"]
        if len(ratings) == 0:
            return None
        return sum(ratings) / len(ratings)

    # ==================== LEVEL 4: Ride History and Cancellations ====================

    def cancel_ride(self, ride_id: str) -> bool:
        """
        Cancel a ride.

        Args:
            ride_id: Unique identifier for the ride

        Returns:
            True if cancelled successfully, False otherwise

        Failure conditions:
            - Ride doesn't exist
            - Ride is already in_progress or completed

        Notes:
            - $5 cancellation fee applies if driver was already matched
            - Driver becomes available again after cancellation
        """
        if ride_id not in self.rides:
            return False
        if self.rides[ride_id]["status"] in ["in_progress", "completed", "cancelled"]:
            return False
        self.free_parties_from_ride_id(ride_id)
        self.rides[ride_id]["status"] = "cancelled"
        return True

    def get_driver_earnings(self, driver_id: str) -> float:
        """
        Get total earnings for a driver.

        Args:
            driver_id: Unique identifier for the driver

        Returns:
            Total earnings (fare * 0.75 for completed rides + cancellation fees)
            Returns 0.0 if driver doesn't exist or has no earnings
        """
        if driver_id not in self.drivers:
            return 0
        total_earnings = 0
        for ride_id in self.drivers[driver_id]["ride_ids"]:
            ride_fare = self.get_ride_fare(ride_id, driver_fare=True)
            if ride_fare:
                total_earnings += ride_fare
        return total_earnings

    def get_rider_history(self, rider_id: str) -> list:
        """
        Get ride history for a rider.

        Args:
            rider_id: Unique identifier for the rider

        Returns:
            List of dicts with keys: ride_id, pickup, dropoff, status, fare, driver_name
            (fare is None if not completed, driver_name is None if no driver matched)
            Ordered by request time (oldest first)
            Returns empty list if rider doesn't exist
        """
        if rider_id not in self.riders:
            return []
        history = []

        for ride_id in self.riders[rider_id]["ride_ids"]:
            ride = self.rides[ride_id]
            fare = self.get_ride_fare(ride_id)
            history.append(
                {"ride_id": ride_id, "pickup": ride["pickup"], "dropoff": ride["dropoff"], "status": ride["status"], "fare": fare, "driver_name": self.drivers[ride["driver_id"]]["name"] if "driver_id" in ride else None})

        return history

    def get_driver_history(self, driver_id: str) -> list:
        """
        Get ride history for a driver.

        Args:
            driver_id: Unique identifier for the driver

        Returns:
            List of dicts with keys: ride_id, pickup, dropoff, status, fare, rider_name, rating
            (fare is None if not completed, rating is None if not rated)
            Ordered by request time (oldest first)
            Returns empty list if driver doesn't exist
        """
        if driver_id not in self.drivers:
            return []
        history = []

        for ride_id in self.drivers[driver_id]["ride_ids"]:
            ride = self.rides[ride_id]
            fare = self.get_ride_fare(ride_id, driver_fare=True)
            history.append(
                {"ride_id": ride_id, "pickup": ride["pickup"], "dropoff": ride["dropoff"], "status": ride["status"], "fare": fare, "rider_name": self.riders[ride["rider_id"]]["name"], "rating": ride["rating"] if "rating" in ride else None})

        return history

    def get_top_drivers(self, n: int) -> list:
        """
        Get top N drivers by average rating.

        Args:
            n: Number of top drivers to return

        Returns:
            List of driver names sorted by:
            1. Average rating (descending)
            2. Name alphabetically (ascending) for ties
            Only includes drivers with 3+ completed rides
        """
        all_drivers_rating = {driver_id: self.get_driver_rating(
            driver_id) for driver_id in self.drivers}
        all_drivers_to_sort = sorted([[-all_drivers_rating[driver_id] if all_drivers_rating[driver_id] != None else 0,
                                       self.drivers[driver_id]["name"]]for driver_id in all_drivers_rating if len(self.get_driver_history(driver_id)) >= 3])
        return [driver[1] for driver in all_drivers_to_sort][:n]
