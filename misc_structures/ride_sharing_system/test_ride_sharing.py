"""
Test suite for Ride Sharing System.

Run with: pytest test_ride_sharing.py -v
Run specific level: pytest test_ride_sharing.py -v -k "level1"
"""

import pytest
from ride_sharing import RideSharingSystem


# ==================== LEVEL 1: Drivers and Riders ====================

class TestLevel1RegisterDriver:
    """Tests for register_driver functionality."""

    def test_level1_register_single_driver(self):
        system = RideSharingSystem()
        assert system.register_driver("D001", "Alice", "standard") is True

    def test_level1_register_multiple_drivers(self):
        system = RideSharingSystem()
        assert system.register_driver("D001", "Alice", "standard") is True
        assert system.register_driver("D002", "Bob", "premium") is True
        assert system.register_driver("D003", "Charlie", "xl") is True

    def test_level1_register_duplicate_driver_id(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        assert system.register_driver("D001", "Bob", "premium") is False

    def test_level1_register_invalid_vehicle_type(self):
        system = RideSharingSystem()
        assert system.register_driver("D001", "Alice", "luxury") is False
        assert system.register_driver("D002", "Bob", "STANDARD") is False


class TestLevel1RegisterRider:
    """Tests for register_rider functionality."""

    def test_level1_register_single_rider(self):
        system = RideSharingSystem()
        assert system.register_rider("R001", "John") is True

    def test_level1_register_multiple_riders(self):
        system = RideSharingSystem()
        assert system.register_rider("R001", "John") is True
        assert system.register_rider("R002", "Jane") is True

    def test_level1_register_duplicate_rider_id(self):
        system = RideSharingSystem()
        system.register_rider("R001", "John")
        assert system.register_rider("R001", "Jane") is False


class TestLevel1DriverAvailability:
    """Tests for set_driver_availability functionality."""

    def test_level1_set_driver_available(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        assert system.set_driver_availability("D001", True) is True

    def test_level1_set_driver_unavailable(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.set_driver_availability("D001", True)
        assert system.set_driver_availability("D001", False) is True

    def test_level1_set_availability_nonexistent_driver(self):
        system = RideSharingSystem()
        assert system.set_driver_availability("D999", True) is False


class TestLevel1GetAvailableDrivers:
    """Tests for get_available_drivers functionality."""

    def test_level1_no_available_drivers(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        assert system.get_available_drivers() == []

    def test_level1_all_available_drivers(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_driver("D002", "Bob", "premium")
        system.set_driver_availability("D001", True)
        system.set_driver_availability("D002", True)
        assert system.get_available_drivers() == ["Alice", "Bob"]

    def test_level1_available_drivers_by_type(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_driver("D002", "Bob", "premium")
        system.register_driver("D003", "Charlie", "standard")
        system.set_driver_availability("D001", True)
        system.set_driver_availability("D002", True)
        system.set_driver_availability("D003", True)
        assert system.get_available_drivers("standard") == ["Alice", "Charlie"]
        assert system.get_available_drivers("premium") == ["Bob"]

    def test_level1_available_drivers_sorted(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Zoe", "standard")
        system.register_driver("D002", "Alice", "standard")
        system.set_driver_availability("D001", True)
        system.set_driver_availability("D002", True)
        assert system.get_available_drivers() == ["Alice", "Zoe"]


# ==================== LEVEL 2: Ride Requests and Matching ====================

class TestLevel2RequestRide:
    """Tests for request_ride functionality."""

    def test_level2_request_ride_success(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        assert ride_id is not None

    def test_level2_request_ride_nonexistent_rider(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.set_driver_availability("D001", True)
        assert system.request_ride("R999", "Downtown", "Airport") is None

    def test_level2_request_ride_no_available_drivers(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        # Driver not set to available
        assert system.request_ride("R001", "Downtown", "Airport") is None

    def test_level2_request_ride_wrong_vehicle_type(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        assert system.request_ride(
            "R001", "Downtown", "Airport", "premium") is None

    def test_level2_request_ride_driver_becomes_unavailable(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        system.request_ride("R001", "Downtown", "Airport")
        assert system.get_available_drivers("standard") == []

    def test_level2_rider_one_active_ride(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_driver("D002", "Bob", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        system.set_driver_availability("D002", True)
        system.request_ride("R001", "Downtown", "Airport")
        assert system.request_ride("R001", "Mall", "Home") is None


class TestLevel2StartRide:
    """Tests for start_ride functionality."""

    def test_level2_start_ride_success(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        assert system.start_ride(ride_id) is True

    def test_level2_start_nonexistent_ride(self):
        system = RideSharingSystem()
        assert system.start_ride("RIDE999") is False

    def test_level2_start_already_started_ride(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        assert system.start_ride(ride_id) is False


class TestLevel2CompleteRide:
    """Tests for complete_ride functionality."""

    def test_level2_complete_ride_success(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        assert system.complete_ride(ride_id, 15.5) is True

    def test_level2_complete_nonexistent_ride(self):
        system = RideSharingSystem()
        assert system.complete_ride("RIDE999", 10.0) is False

    def test_level2_complete_not_started_ride(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        assert system.complete_ride(ride_id, 10.0) is False

    def test_level2_driver_available_after_complete(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        assert system.get_available_drivers("standard") == ["Alice"]


class TestLevel2GetRideStatus:
    """Tests for get_ride_status functionality."""

    def test_level2_ride_status_requested(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        assert system.get_ride_status(ride_id) == "requested"

    def test_level2_ride_status_in_progress(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        assert system.get_ride_status(ride_id) == "in_progress"

    def test_level2_ride_status_completed(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        assert system.get_ride_status(ride_id) == "completed"

    def test_level2_ride_status_nonexistent(self):
        system = RideSharingSystem()
        assert system.get_ride_status("RIDE999") is None

    def test_level2_rider_can_request_after_complete(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id1 = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id1)
        system.complete_ride(ride_id1, 10.0)
        ride_id2 = system.request_ride("R001", "Home", "Office")
        assert ride_id2 is not None
        assert ride_id2 != ride_id1


# ==================== LEVEL 3: Pricing and Ratings ====================

class TestLevel3SurgePricing:
    """Tests for set_surge_multiplier functionality."""

    def test_level3_set_surge_valid(self):
        system = RideSharingSystem()
        assert system.set_surge_multiplier(1.5) is True

    def test_level3_set_surge_invalid(self):
        system = RideSharingSystem()
        assert system.set_surge_multiplier(0.5) is False

    def test_level3_set_surge_one(self):
        system = RideSharingSystem()
        assert system.set_surge_multiplier(1.0) is True


class TestLevel3Fare:
    """Tests for fare calculation."""

    def test_level3_fare_standard(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride(
            "R001", "Downtown", "Airport", "standard")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        # $2.50 base + $1.50 * 10km = $17.50
        assert system.get_ride_fare(ride_id) == 17.50

    def test_level3_fare_premium(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "premium")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport", "premium")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        # $5.00 base + $2.50 * 10km = $30.00
        assert system.get_ride_fare(ride_id) == 30.00

    def test_level3_fare_xl(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "xl")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport", "xl")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        # $4.00 base + $2.00 * 10km = $24.00
        assert system.get_ride_fare(ride_id) == 24.00

    def test_level3_fare_with_surge(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        system.set_surge_multiplier(2.0)
        ride_id = system.request_ride(
            "R001", "Downtown", "Airport", "standard")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        # ($2.50 base + $1.50 * 10km) * 2.0 = $35.00
        assert system.get_ride_fare(ride_id) == 35.00

    def test_level3_fare_locked_at_request(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        system.set_surge_multiplier(2.0)
        ride_id = system.request_ride(
            "R001", "Downtown", "Airport", "standard")
        system.set_surge_multiplier(1.0)  # Surge ends
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        # Fare should still use 2.0 surge from request time
        assert system.get_ride_fare(ride_id) == 35.00

    def test_level3_fare_not_completed(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        assert system.get_ride_fare(ride_id) is None


class TestLevel3Rating:
    """Tests for driver rating functionality."""

    def test_level3_rate_driver_success(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        assert system.rate_driver(ride_id, 5) is True

    def test_level3_rate_driver_invalid_rating(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        assert system.rate_driver(ride_id, 0) is False
        assert system.rate_driver(ride_id, 6) is False

    def test_level3_rate_driver_not_completed(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        assert system.rate_driver(ride_id, 5) is False

    def test_level3_rate_driver_already_rated(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        system.rate_driver(ride_id, 5)
        assert system.rate_driver(ride_id, 4) is False

    def test_level3_get_driver_rating(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.register_rider("R002", "Jane")
        system.set_driver_availability("D001", True)

        ride1 = system.request_ride("R001", "A", "B")
        system.start_ride(ride1)
        system.complete_ride(ride1, 10.0)
        system.rate_driver(ride1, 5)

        ride2 = system.request_ride("R002", "C", "D")
        system.start_ride(ride2)
        system.complete_ride(ride2, 10.0)
        system.rate_driver(ride2, 3)

        assert system.get_driver_rating("D001") == 4.0

    def test_level3_get_driver_rating_no_ratings(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        assert system.get_driver_rating("D001") is None

    def test_level3_get_driver_rating_nonexistent(self):
        system = RideSharingSystem()
        assert system.get_driver_rating("D999") is None


# ==================== LEVEL 4: Ride History and Cancellations ====================

class TestLevel4CancelRide:
    """Tests for cancel_ride functionality."""

    def test_level4_cancel_requested_ride(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        assert system.cancel_ride(ride_id) is True
        assert system.get_ride_status(ride_id) == "cancelled"

    def test_level4_cancel_driver_becomes_available(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.cancel_ride(ride_id)
        assert system.get_available_drivers("standard") == ["Alice"]

    def test_level4_cancel_in_progress_fails(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        assert system.cancel_ride(ride_id) is False

    def test_level4_cancel_completed_fails(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        assert system.cancel_ride(ride_id) is False

    def test_level4_rider_can_request_after_cancel(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id1 = system.request_ride("R001", "Downtown", "Airport")
        system.cancel_ride(ride_id1)
        ride_id2 = system.request_ride("R001", "Home", "Office")
        assert ride_id2 is not None


class TestLevel4DriverEarnings:
    """Tests for get_driver_earnings functionality."""

    def test_level4_earnings_completed_ride(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        # Fare = $17.50, driver gets 75% = $13.125
        assert system.get_driver_earnings("D001") == pytest.approx(13.125)

    def test_level4_earnings_multiple_rides(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.register_rider("R002", "Jane")
        system.set_driver_availability("D001", True)

        ride1 = system.request_ride("R001", "A", "B")
        system.start_ride(ride1)
        system.complete_ride(ride1, 10.0)  # $17.50 fare

        ride2 = system.request_ride("R002", "C", "D")
        system.start_ride(ride2)
        system.complete_ride(ride2, 10.0)  # $17.50 fare

        # Total: $35.00 * 0.75 = $26.25
        assert system.get_driver_earnings("D001") == pytest.approx(26.25)

    def test_level4_earnings_with_cancellation_fee(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.cancel_ride(ride_id)
        # $5 cancellation fee goes to driver
        assert system.get_driver_earnings("D001") == 5.0

    def test_level4_earnings_no_rides(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        assert system.get_driver_earnings("D001") == 0.0

    def test_level4_earnings_nonexistent_driver(self):
        system = RideSharingSystem()
        assert system.get_driver_earnings("D999") == 0.0


class TestLevel4RiderHistory:
    """Tests for get_rider_history functionality."""

    def test_level4_rider_history_empty(self):
        system = RideSharingSystem()
        system.register_rider("R001", "John")
        assert system.get_rider_history("R001") == []

    def test_level4_rider_history_single_ride(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)

        history = system.get_rider_history("R001")
        assert len(history) == 1
        assert history[0]["ride_id"] == ride_id
        assert history[0]["pickup"] == "Downtown"
        assert history[0]["dropoff"] == "Airport"
        assert history[0]["status"] == "completed"
        assert history[0]["fare"] == 17.50
        assert history[0]["driver_name"] == "Alice"

    def test_level4_rider_history_multiple_ordered(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)

        ride1 = system.request_ride("R001", "A", "B")
        system.start_ride(ride1)
        system.complete_ride(ride1, 5.0)

        ride2 = system.request_ride("R001", "C", "D")
        system.start_ride(ride2)
        system.complete_ride(ride2, 10.0)

        history = system.get_rider_history("R001")
        assert len(history) == 2
        assert history[0]["ride_id"] == ride1
        assert history[1]["ride_id"] == ride2

    def test_level4_rider_history_cancelled(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.cancel_ride(ride_id)

        history = system.get_rider_history("R001")
        assert len(history) == 1
        assert history[0]["status"] == "cancelled"
        assert history[0]["fare"] is None

    def test_level4_rider_history_nonexistent(self):
        system = RideSharingSystem()
        assert system.get_rider_history("R999") == []


class TestLevel4DriverHistory:
    """Tests for get_driver_history functionality."""

    def test_level4_driver_history_empty(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        assert system.get_driver_history("D001") == []

    def test_level4_driver_history_with_rating(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)
        system.rate_driver(ride_id, 5)

        history = system.get_driver_history("D001")
        assert len(history) == 1
        assert history[0]["rider_name"] == "John"
        assert history[0]["rating"] == 5

    def test_level4_driver_history_no_rating(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_rider("R001", "John")
        system.set_driver_availability("D001", True)
        ride_id = system.request_ride("R001", "Downtown", "Airport")
        system.start_ride(ride_id)
        system.complete_ride(ride_id, 10.0)

        history = system.get_driver_history("D001")
        assert history[0]["rating"] is None

    def test_level4_driver_history_nonexistent(self):
        system = RideSharingSystem()
        assert system.get_driver_history("D999") == []


class TestLevel4TopDrivers:
    """Tests for get_top_drivers functionality."""

    def test_level4_top_drivers_basic(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")
        system.register_driver("D002", "Bob", "standard")

        # Give Alice 3 rides with ratings
        for i in range(3):
            system.register_rider(f"R{i}", f"Rider{i}")
            system.set_driver_availability("D001", True)
            ride = system.request_ride(f"R{i}", "A", "B")
            system.start_ride(ride)
            system.complete_ride(ride, 10.0)
            system.rate_driver(ride, 5)

        # Make Alice unavailable so Bob can get rides
        system.set_driver_availability("D001", False)

        # Give Bob 3 rides with lower ratings
        for i in range(3, 6):
            system.register_rider(f"R{i}", f"Rider{i}")
            system.set_driver_availability("D002", True)
            ride = system.request_ride(f"R{i}", "A", "B")
            system.start_ride(ride)
            system.complete_ride(ride, 10.0)
            system.rate_driver(ride, 4)

        assert system.get_top_drivers(2) == ["Alice", "Bob"]

    def test_level4_top_drivers_min_rides(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Alice", "standard")

        # Give Alice only 2 rides (not enough)
        for i in range(2):
            system.register_rider(f"R{i}", f"Rider{i}")
            system.set_driver_availability("D001", True)
            ride = system.request_ride(f"R{i}", "A", "B")
            system.start_ride(ride)
            system.complete_ride(ride, 10.0)
            system.rate_driver(ride, 5)

        assert system.get_top_drivers(1) == []

    def test_level4_top_drivers_tie_breaker(self):
        system = RideSharingSystem()
        system.register_driver("D001", "Zoe", "standard")
        system.register_driver("D002", "Alice", "standard")

        # Give both drivers same rating
        for driver_id, driver_num in [("D001", 0), ("D002", 10)]:
            for i in range(3):
                rider_id = f"R{driver_num + i}"
                system.register_rider(rider_id, f"Rider{driver_num + i}")
                system.set_driver_availability(driver_id, True)
                ride = system.request_ride(rider_id, "A", "B")
                system.start_ride(ride)
                system.complete_ride(ride, 10.0)
                system.rate_driver(ride, 5)

        # Same rating, Alice comes before Zoe alphabetically
        assert system.get_top_drivers(2) == ["Alice", "Zoe"]

    def test_level4_top_drivers_empty(self):
        system = RideSharingSystem()
        assert system.get_top_drivers(5) == []


class TestLevel4Integration:
    """Integration tests combining multiple Level 4 features."""

    def test_level4_full_scenario(self):
        system = RideSharingSystem()

        # Setup
        system.register_driver("D001", "Alice", "standard")
        system.register_driver("D002", "Bob", "premium")
        system.register_rider("R001", "John")
        system.register_rider("R002", "Jane")

        # John's first ride with Alice
        system.set_driver_availability("D001", True)
        ride1 = system.request_ride("R001", "Home", "Work")
        system.start_ride(ride1)
        system.complete_ride(ride1, 10.0)
        system.rate_driver(ride1, 5)

        # John cancels a ride (after driver matched)
        ride2 = system.request_ride("R001", "Work", "Gym")
        system.cancel_ride(ride2)

        # Jane's ride with Bob (premium)
        system.set_driver_availability("D002", True)
        system.set_surge_multiplier(1.5)
        ride3 = system.request_ride("R002", "Mall", "Airport", "premium")
        system.start_ride(ride3)
        system.complete_ride(ride3, 20.0)
        system.rate_driver(ride3, 4)

        # Check histories
        john_history = system.get_rider_history("R001")
        assert len(john_history) == 2
        assert john_history[0]["status"] == "completed"
        assert john_history[1]["status"] == "cancelled"

        # Check earnings
        # Alice: $17.50 * 0.75 (completed) + $5 (cancellation) = $18.125
        assert system.get_driver_earnings("D001") == pytest.approx(18.125)

        # Bob: ($5 + $2.50 * 20) * 1.5 = $82.50 fare, 75% = $61.875
        assert system.get_driver_earnings("D002") == pytest.approx(61.875)
