import pytest
from contact import Contact
from pydantic import ValidationError


def test_contact_basic():
    contact = Contact(name="John Doe", email="john@example.com", phone="555-123-4567")
    assert contact.name == "John Doe"
    assert contact.email == "john@example.com"
    assert contact.phone == "555-123-4567"
    assert contact.website is None
    assert contact.notes is None


def test_contact_with_parentheses_phone():
    contact = Contact(
        name="Jane Smith", email="jane@example.com", phone="(555) 987-6543"
    )
    assert contact.phone == "(555) 987-6543"


def test_contact_with_website():
    contact = Contact(
        name="Jane Smith",
        email="jane@example.com",
        phone="(555) 987-6543",
        website="https://example.com",
    )
    assert str(contact.website) == "https://example.com/"


def test_contact_with_notes():
    contact = Contact(
        name="Jane Smith",
        email="jane@example.com",
        phone="(555) 987-6543",
        website="https://example.com",
        notes="Met at conference",
    )
    assert contact.notes == "Met at conference"


def test_contact_all_fields():
    contact = Contact(
        name="Jane Smith",
        email="jane@example.com",
        phone="(555) 987-6543",
        website="https://example.com",
        notes="Met at conference",
    )
    assert contact.name == "Jane Smith"
    assert contact.email == "jane@example.com"
    assert contact.phone == "(555) 987-6543"
    assert str(contact.website) == "https://example.com/"
    assert contact.notes == "Met at conference"


def test_invalid_phone_dots():
    with pytest.raises(ValidationError):
        Contact(name="Bob", email="bob@example.com", phone="555.123.4567")


def test_invalid_phone_no_separator():
    with pytest.raises(ValidationError):
        Contact(name="Bob", email="bob@example.com", phone="5551234567")


def test_invalid_phone_wrong_format():
    with pytest.raises(ValidationError):
        Contact(name="Bob", email="bob@example.com", phone="123-45-6789")


def test_invalid_email():
    with pytest.raises(ValidationError):
        Contact(name="Bob", email="not-an-email", phone="555-123-4567")


def test_invalid_website():
    with pytest.raises(ValidationError):
        Contact(
            name="Bob",
            email="bob@example.com",
            phone="555-123-4567",
            website="not-a-url",
        )


def test_empty_name():
    with pytest.raises(ValidationError):
        Contact(name="", email="bob@example.com", phone="555-123-4567")


def test_name_too_long():
    with pytest.raises(ValidationError):
        Contact(name="x" * 51, email="bob@example.com", phone="555-123-4567")


def test_serialization():
    contact = Contact(name="John Doe", email="john@example.com", phone="555-123-4567")
    data = contact.model_dump()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert data["phone"] == "555-123-4567"
    assert data["website"] is None
    assert data["notes"] is None
