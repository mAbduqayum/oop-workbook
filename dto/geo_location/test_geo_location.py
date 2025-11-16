import pytest
from geo_location import GeoLocation, distance_to
from pydantic import ValidationError


def test_geo_location_basic():
    location = GeoLocation(latitude=40.7128, longitude=-74.0060, name="New York City")
    assert location.latitude == 40.7128
    assert location.longitude == -74.0060
    assert location.name == "New York City"


def test_distance_to_same_location():
    location = GeoLocation(latitude=40.7128, longitude=-74.0060, name="New York City")
    distance = distance_to(location, location)
    assert distance == 0.0


def test_distance_new_york_to_los_angeles():
    new_york = GeoLocation(latitude=40.7128, longitude=-74.0060, name="New York City")
    los_angeles = GeoLocation(latitude=34.0522, longitude=-118.2437, name="Los Angeles")
    distance = distance_to(new_york, los_angeles)
    assert 3900 < distance < 4000


def test_distance_is_symmetric():
    new_york = GeoLocation(latitude=40.7128, longitude=-74.0060, name="New York City")
    los_angeles = GeoLocation(latitude=34.0522, longitude=-118.2437, name="Los Angeles")
    distance1 = distance_to(new_york, los_angeles)
    distance2 = distance_to(los_angeles, new_york)
    assert distance1 == distance2


def test_distance_london_to_paris():
    london = GeoLocation(latitude=51.5074, longitude=-0.1278, name="London")
    paris = GeoLocation(latitude=48.8566, longitude=2.3522, name="Paris")
    distance = distance_to(london, paris)
    assert 330 < distance < 350


def test_invalid_latitude_too_high():
    with pytest.raises(ValidationError):
        GeoLocation(latitude=100.0, longitude=0.0, name="Invalid")


def test_invalid_latitude_too_low():
    with pytest.raises(ValidationError):
        GeoLocation(latitude=-100.0, longitude=0.0, name="Invalid")


def test_invalid_longitude_too_high():
    with pytest.raises(ValidationError):
        GeoLocation(latitude=0.0, longitude=200.0, name="Invalid")


def test_invalid_longitude_too_low():
    with pytest.raises(ValidationError):
        GeoLocation(latitude=0.0, longitude=-200.0, name="Invalid")


def test_valid_latitude_boundaries():
    north_pole = GeoLocation(latitude=90.0, longitude=0.0, name="North Pole")
    south_pole = GeoLocation(latitude=-90.0, longitude=0.0, name="South Pole")
    assert north_pole.latitude == 90.0
    assert south_pole.latitude == -90.0


def test_valid_longitude_boundaries():
    east = GeoLocation(latitude=0.0, longitude=180.0, name="East")
    west = GeoLocation(latitude=0.0, longitude=-180.0, name="West")
    assert east.longitude == 180.0
    assert west.longitude == -180.0


def test_empty_name():
    with pytest.raises(ValidationError):
        GeoLocation(latitude=0.0, longitude=0.0, name="")


def test_name_too_long():
    with pytest.raises(ValidationError):
        GeoLocation(latitude=0.0, longitude=0.0, name="x" * 51)


def test_serialization():
    location = GeoLocation(latitude=40.7128, longitude=-74.0060, name="New York City")
    data = location.model_dump()
    assert data["latitude"] == 40.7128
    assert data["longitude"] == -74.0060
    assert data["name"] == "New York City"
