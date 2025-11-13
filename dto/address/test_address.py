import pytest
from address import Address
from pydantic import ValidationError


def test_address_basic():
    address = Address(
        street="123 Main St", city="Springfield", state="IL", zip_code="62701"
    )
    assert address.street == "123 Main St"
    assert address.city == "Springfield"
    assert address.state == "IL"
    assert address.zip_code == "62701"
    assert address.country == "US"
    assert address.apartment is None


def test_address_with_apartment():
    address = Address(
        street="456 Oak Ave",
        apartment="Apt 3B",
        city="Chicago",
        state="IL",
        zip_code="60601-1234",
    )
    assert address.apartment == "Apt 3B"


def test_full_address_without_apartment():
    address = Address(
        street="123 Main St", city="Springfield", state="IL", zip_code="62701"
    )
    assert address.full_address == "123 Main St Springfield, IL 62701, US"


def test_full_address_with_apartment():
    address = Address(
        street="456 Oak Ave",
        apartment="Apt 3B",
        city="Chicago",
        state="IL",
        zip_code="60601-1234",
    )
    assert address.full_address == "456 Oak Ave Apt 3B Chicago, IL 60601-1234, US"


def test_zip_code_extended_format():
    address = Address(
        street="123 Main St", city="Springfield", state="IL", zip_code="62701-1234"
    )
    assert address.zip_code == "62701-1234"


def test_custom_country():
    address = Address(
        street="123 Main St", city="Toronto", state="ON", zip_code="12345", country="CA"
    )
    assert address.country == "CA"


def test_invalid_state_lowercase():
    with pytest.raises(ValidationError):
        Address(street="123 Main St", city="Springfield", state="il", zip_code="62701")


def test_invalid_state_full_name():
    with pytest.raises(ValidationError):
        Address(
            street="123 Main St", city="Springfield", state="Illinois", zip_code="62701"
        )


def test_invalid_zip_code_too_short():
    with pytest.raises(ValidationError):
        Address(street="123 Main St", city="Springfield", state="IL", zip_code="1234")


def test_invalid_zip_code_letters():
    with pytest.raises(ValidationError):
        Address(street="123 Main St", city="Springfield", state="IL", zip_code="ABCDE")


def test_invalid_zip_code_wrong_format():
    with pytest.raises(ValidationError):
        Address(
            street="123 Main St", city="Springfield", state="IL", zip_code="12345-67"
        )


def test_empty_street():
    with pytest.raises(ValidationError):
        Address(street="", city="Springfield", state="IL", zip_code="62701")


def test_empty_city():
    with pytest.raises(ValidationError):
        Address(street="123 Main St", city="", state="IL", zip_code="62701")


def test_serialization():
    address = Address(
        street="123 Main St", city="Springfield", state="IL", zip_code="62701"
    )
    data = address.model_dump()
    assert data["street"] == "123 Main St"
    assert data["city"] == "Springfield"
    assert data["state"] == "IL"
    assert data["zip_code"] == "62701"
    assert data["country"] == "US"
    assert data["apartment"] is None
