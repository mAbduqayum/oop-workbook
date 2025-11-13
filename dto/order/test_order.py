from uuid import uuid4

import pytest
from pydantic import ValidationError

from dto.category.category import Category
from dto.order.order import Order, OrderItem
from dto.product.product import Product
from dto.user.user import User


@pytest.fixture
def laptop():
    return Product(
        id=uuid4(),
        name="Laptop",
        price=999.99,
        quantity=10,
        categories=[Category(id=1, name="Electronics")],
    )


@pytest.fixture
def mouse():
    return Product(
        id=uuid4(),
        name="Mouse",
        price=29.99,
        quantity=50,
        categories=[Category(id=1, name="Electronics")],
    )


@pytest.fixture
def customer():
    return User(id=uuid4(), username="john_doe", email="john@example.com", age=25)


def test_order_item_basic(laptop):
    item = OrderItem(product=laptop, quantity=2)
    assert item.product.name == "Laptop"
    assert item.quantity == 2


def test_order_item_subtotal(laptop):
    item = OrderItem(product=laptop, quantity=2)
    assert item.subtotal == 1999.98


def test_order_item_single_quantity(mouse):
    item = OrderItem(product=mouse, quantity=1)
    assert item.subtotal == 29.99


def test_order_item_multiple_quantity(mouse):
    item = OrderItem(product=mouse, quantity=3)
    assert item.subtotal == 89.97


def test_order_item_zero_quantity(laptop):
    with pytest.raises(ValidationError):
        OrderItem(product=laptop, quantity=0)


def test_order_item_negative_quantity(laptop):
    with pytest.raises(ValidationError):
        OrderItem(product=laptop, quantity=-1)


def test_order_basic(laptop, customer):
    item = OrderItem(product=laptop, quantity=1)
    order_id = uuid4()
    order = Order(id=order_id, customer=customer, items=[item])
    assert order.id == order_id
    assert order.customer.username == "john_doe"
    assert len(order.items) == 1
    assert order.status == "pending"


def test_order_total_single_item(laptop, customer):
    item = OrderItem(product=laptop, quantity=2)
    order = Order(id=uuid4(), customer=customer, items=[item])
    assert order.total == 1999.98


def test_order_total_multiple_items(laptop, mouse, customer):
    item1 = OrderItem(product=laptop, quantity=2)
    item2 = OrderItem(product=mouse, quantity=3)
    order = Order(id=uuid4(), customer=customer, items=[item1, item2])
    assert order.total == 2089.95


def test_order_item_count(laptop, mouse, customer):
    item1 = OrderItem(product=laptop, quantity=2)
    item2 = OrderItem(product=mouse, quantity=3)
    order = Order(id=uuid4(), customer=customer, items=[item1, item2])
    assert order.item_count == 5


def test_order_status_pending(laptop, customer):
    item = OrderItem(product=laptop, quantity=1)
    order = Order(id=uuid4(), customer=customer, items=[item])
    assert order.status == "pending"


def test_order_status_processing(laptop, customer):
    item = OrderItem(product=laptop, quantity=1)
    order = Order(id=uuid4(), customer=customer, items=[item], status="processing")
    assert order.status == "processing"


def test_order_status_shipped(laptop, customer):
    item = OrderItem(product=laptop, quantity=1)
    order = Order(id=uuid4(), customer=customer, items=[item], status="shipped")
    assert order.status == "shipped"


def test_order_status_delivered(laptop, customer):
    item = OrderItem(product=laptop, quantity=1)
    order = Order(id=uuid4(), customer=customer, items=[item], status="delivered")
    assert order.status == "delivered"


def test_order_empty_items(customer):
    with pytest.raises(ValidationError):
        Order(id=uuid4(), customer=customer, items=[])


def test_order_invalid_status(laptop, customer):
    item = OrderItem(product=laptop, quantity=1)
    with pytest.raises(ValidationError):
        Order(id=uuid4(), customer=customer, items=[item], status="invalid")


def test_order_serialization(laptop, customer):
    item = OrderItem(product=laptop, quantity=2)
    order_id = uuid4()
    order = Order(id=order_id, customer=customer, items=[item])
    data = order.model_dump()
    assert data["id"] == order_id
    assert data["customer"]["username"] == "john_doe"
    assert len(data["items"]) == 1
    assert data["status"] == "pending"
