# GeoLocation - Coordinate Validation and Distance Calculation

## Exercise: GeoLocation Model with Distance Function

Create a `GeoLocation` class using Pydantic's `BaseModel` with coordinate validation and a separate distance calculation function.

**Task:**

1. Create a `GeoLocation` class using `BaseModel` with the following fields:
    - `latitude: float` - Latitude coordinate (-90 to 90)
    - `longitude: float` - Longitude coordinate (-180 to 180)
    - `name: str` - Location name (1-50 characters)
2. Create a `distance_to(location1: GeoLocation, location2: GeoLocation)` function that calculates distance in kilometers using the Haversine formula
3. Round the distance to 2 decimal places

**Example:**

```python
from math import radians, sin, cos, sqrt, atan2

new_york = GeoLocation(
    latitude=40.7128,
    longitude=-74.0060,
    name="New York City"
)

los_angeles = GeoLocation(
    latitude=34.0522,
    longitude=-118.2437,
    name="Los Angeles"
)

print(new_york.name)  # New York City
distance = distance_to(new_york, los_angeles)
print(distance)  # ~3935.75 km

# Invalid latitude raises ValidationError
GeoLocation(latitude=100.0, longitude=0.0, name="Invalid")  # ValidationError

# Invalid longitude raises ValidationError
GeoLocation(latitude=0.0, longitude=200.0, name="Invalid")  # ValidationError
```

**Haversine Formula:**

```
R = 6371  # Earth radius in kilometers
Δlat = lat2 - lat1
Δlon = lon2 - lon1
a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)
c = 2 * atan2(√a, √(1-a))
distance = R * c
```
