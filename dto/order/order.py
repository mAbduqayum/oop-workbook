from __future__ import annotations

from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field

from ..product.product import Product
from ..user.user import User


class OrderItem(BaseModel):
    product: Product
    quantity: int = Field(ge=1)

    @property
    def subtotal(self) -> float:
        return round(self.product.price * self.quantity, 2)


class Order(BaseModel):
    id: UUID
    customer: User
    items: list[OrderItem] = Field(min_length=1)
    status: Literal["pending", "processing", "shipped", "delivered"] = "pending"

    @property
    def total(self) -> float:
        return round(sum(item.subtotal for item in self.items), 2)

    @property
    def item_count(self) -> int:
        return sum(item.quantity for item in self.items)
