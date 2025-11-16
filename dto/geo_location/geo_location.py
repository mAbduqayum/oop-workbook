from math import atan2, cos, radians, sin, sqrt

from pydantic import BaseModel, Field


class GeoLocation(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    name: str = Field(min_length=1, max_length=50)


def distance_to(location1: GeoLocation, location2: GeoLocation) -> float:
    R = 6371

    lat1 = radians(location1.latitude)
    lat2 = radians(location2.latitude)
    delta_lat = radians(location2.latitude - location1.latitude)
    delta_lon = radians(location2.longitude - location1.longitude)

    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return round(distance, 2)
