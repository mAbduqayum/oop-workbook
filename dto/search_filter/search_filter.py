from typing import Literal

from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self


class SearchFilter(BaseModel):
    query: str | None = None
    min_price: float | None = Field(default=None, gt=0, multiple_of=0.01)
    max_price: float | None = Field(default=None, gt=0, multiple_of=0.01)
    categories: list[str] | None = None
    in_stock: bool | None = None
    sort_by: Literal["price", "name", "date"] | None = None
    sort_order: Literal["asc", "desc"] | None = None

    @model_validator(mode="after")
    def validate_price_range(self) -> Self:
        if self.min_price is not None and self.max_price is not None:
            if self.min_price > self.max_price:
                raise ValueError("min_price must be less than or equal to max_price")
        return self

    @property
    def has_filters(self) -> bool:
        return any(
            v is not None
            for v in [
                self.query,
                self.min_price,
                self.max_price,
                self.categories,
                self.in_stock,
                self.sort_by,
                self.sort_order,
            ]
        )

    def to_query_params(self) -> dict:
        return self.model_dump(exclude_none=True)
