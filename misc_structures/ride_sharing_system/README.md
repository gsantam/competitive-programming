# CodeSignal Interview Preparation - Ride Sharing System

A practice project simulating the CodeSignal coding assessment format. This project involves implementing a ride sharing system (like Uber/Lyft) across 4 levels of increasing complexity, focusing on refactoring and adapting to new requirements.

## Overview

- **Time Target:** 90 minutes for all 4 levels
- **Language:** Python (standard library only)
- **Testing:** pytest
- **Focus:** Quick, correct implementation; code quality is not evaluated

## How to Use

1. Implement the methods in `ride_sharing.py`
2. Run tests for each level: `pytest test_ride_sharing.py -v -k "level1"`
3. Progress to the next level only after passing all tests in the current level
4. Later levels build on earlier ones and may require refactoring

## Running Tests

```bash
# Run all tests
pytest test_ride_sharing.py -v

# Run tests for a specific level
pytest test_ride_sharing.py -v -k "level1"
pytest test_ride_sharing.py -v -k "level2"
pytest test_ride_sharing.py -v -k "level3"
pytest test_ride_sharing.py -v -k "level4"
```

---

## Level 1: Drivers and Riders (Estimated: 15 minutes)

Implement basic driver and rider registration, plus driver availability.

### Requirements

1. **Register drivers** with unique `driver_id`, `name`, and `vehicle_type` ("standard", "premium", "xl")
2. **Register riders** with unique `rider_id` and `name`
3. **Set driver availability** - drivers can go online/offline
4. **Get available drivers** - return list of online drivers by vehicle type

### Methods to Implement

- `register_driver(driver_id: str, name: str, vehicle_type: str) -> bool`
- `register_rider(rider_id: str, name: str) -> bool`
- `set_driver_availability(driver_id: str, is_available: bool) -> bool`
- `get_available_drivers(vehicle_type: str = None) -> list[str]` (returns driver names, sorted)

---

## Level 2: Ride Requests and Matching (Estimated: 20 minutes)

Add ride request and completion workflow with driver matching.

### New Requirements

1. **Request a ride** - rider requests a ride with a pickup and dropoff location
2. **Match driver** - assign an available driver to a ride (first available by driver_id order)
3. **Start ride** - driver begins the trip
4. **Complete ride** - driver ends the trip with distance traveled
5. **Drivers become unavailable** when matched, available again after completing

### Methods to Implement

- `request_ride(rider_id: str, pickup: str, dropoff: str, vehicle_type: str = "standard") -> str | None` (returns ride_id or None)
- `start_ride(ride_id: str) -> bool`
- `complete_ride(ride_id: str, distance_km: float) -> bool`
- `get_ride_status(ride_id: str) -> str | None` (returns "requested", "in_progress", "completed", or None)

### Constraints

- Ride request fails if rider doesn't exist or no drivers available for that vehicle type
- A rider can only have one active ride at a time
- Start fails if ride doesn't exist or isn't in "requested" status
- Complete fails if ride doesn't exist or isn't "in_progress"

---

## Level 3: Pricing and Ratings (Estimated: 25 minutes)

Add fare calculation, surge pricing, and driver ratings.

### New Requirements

1. **Base fare calculation:**
   - Standard: $2.50 base + $1.50/km
   - Premium: $5.00 base + $2.50/km
   - XL: $4.00 base + $2.00/km
2. **Surge pricing** - set a surge multiplier (1.0 = normal, 2.0 = double)
3. **Fare is locked in** at ride request time (based on current surge)
4. **Rate driver** - riders can rate drivers 1-5 stars after ride completes
5. **Get driver rating** - average rating for a driver

### Methods to Implement/Modify

- `set_surge_multiplier(multiplier: float) -> bool` (must be >= 1.0)
- `request_ride(...)` - now locks in fare based on surge at request time
- `complete_ride(...)` - now calculates and stores final fare
- `get_ride_fare(ride_id: str) -> float | None`
- `rate_driver(ride_id: str, rating: int) -> bool` (1-5 stars, only for completed rides, once per ride)
- `get_driver_rating(driver_id: str) -> float | None` (average rating, None if no ratings)

---

## Level 4: Ride History and Cancellations (Estimated: 30 minutes)

Add ride cancellation, history tracking, and driver earnings.

### New Requirements

1. **Cancel ride** - riders can cancel before ride starts ($5 fee if driver already matched)
2. **Driver earnings** - track total earnings per driver (fare minus 25% platform fee)
3. **Rider history** - list all rides for a rider with details
4. **Driver history** - list all rides for a driver with details
5. **Top drivers** - get top N drivers by average rating (min 3 rides)

### Methods to Implement

- `cancel_ride(ride_id: str) -> bool` (fails if ride already started or completed)
- `get_driver_earnings(driver_id: str) -> float`
- `get_rider_history(rider_id: str) -> list[dict]` (ride_id, pickup, dropoff, status, fare, driver_name)
- `get_driver_history(driver_id: str) -> list[dict]` (ride_id, pickup, dropoff, status, fare, rider_name, rating)
- `get_top_drivers(n: int) -> list[str]` (driver names sorted by rating desc, then by name asc)

### Constraints

- Cancellation fees count toward driver earnings
- History ordered by ride request time (oldest first)
- Only include drivers with 3+ completed rides in top drivers

---

## Tips

1. **Start simple** - get Level 1 working before adding complexity
2. **Refactor as needed** - later levels may require restructuring your data
3. **Read requirements carefully** - edge cases matter
4. **Generate unique ride IDs** - use a counter or UUID
5. **Track ride state** - requested → in_progress → completed (or cancelled)
6. **Don't over-engineer** - focus on passing tests, not perfect code

Good luck! 🚗
