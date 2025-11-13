import pytest
from pydantic import ValidationError
from search_filter import SearchFilter


def test_empty_filter():
    filter1 = SearchFilter()
    assert filter1.query is None
    assert filter1.min_price is None
    assert filter1.max_price is None
    assert filter1.categories is None
    assert filter1.in_stock is None
    assert filter1.sort_by is None
    assert filter1.sort_order is None


def test_empty_filter_has_no_filters():
    filter1 = SearchFilter()
    assert filter1.has_filters is False


def test_empty_filter_to_query_params():
    filter1 = SearchFilter()
    assert filter1.to_query_params() == {}


def test_price_range_filter():
    filter2 = SearchFilter(min_price=10.0, max_price=100.0)
    assert filter2.min_price == 10.0
    assert filter2.max_price == 100.0


def test_price_range_has_filters():
    filter2 = SearchFilter(min_price=10.0, max_price=100.0)
    assert filter2.has_filters is True


def test_price_range_to_query_params():
    filter2 = SearchFilter(min_price=10.0, max_price=100.0)
    params = filter2.to_query_params()
    assert params == {"min_price": 10.0, "max_price": 100.0}


def test_complex_filter():
    filter3 = SearchFilter(
        query="laptop",
        min_price=500.0,
        max_price=2000.0,
        categories=["Electronics", "Computers"],
        in_stock=True,
        sort_by="price",
        sort_order="asc",
    )
    assert filter3.query == "laptop"
    assert filter3.min_price == 500.0
    assert filter3.max_price == 2000.0
    assert filter3.categories == ["Electronics", "Computers"]
    assert filter3.in_stock is True
    assert filter3.sort_by == "price"
    assert filter3.sort_order == "asc"


def test_complex_filter_has_filters():
    filter3 = SearchFilter(
        query="laptop",
        min_price=500.0,
        max_price=2000.0,
        categories=["Electronics", "Computers"],
        in_stock=True,
        sort_by="price",
        sort_order="asc",
    )
    assert filter3.has_filters is True


def test_complex_filter_to_query_params():
    filter3 = SearchFilter(
        query="laptop",
        min_price=500.0,
        max_price=2000.0,
        categories=["Electronics", "Computers"],
        in_stock=True,
        sort_by="price",
        sort_order="asc",
    )
    params = filter3.to_query_params()
    assert params["query"] == "laptop"
    assert params["min_price"] == 500.0
    assert params["max_price"] == 2000.0
    assert params["categories"] == ["Electronics", "Computers"]
    assert params["in_stock"] is True
    assert params["sort_by"] == "price"
    assert params["sort_order"] == "asc"


def test_query_only_filter():
    filter4 = SearchFilter(query="laptop")
    assert filter4.has_filters is True
    assert filter4.to_query_params() == {"query": "laptop"}


def test_categories_filter():
    filter5 = SearchFilter(categories=["Electronics", "Computers"])
    assert filter5.has_filters is True
    assert filter5.to_query_params() == {"categories": ["Electronics", "Computers"]}


def test_in_stock_filter():
    filter6 = SearchFilter(in_stock=True)
    assert filter6.has_filters is True
    assert filter6.to_query_params() == {"in_stock": True}


def test_sort_filter():
    filter7 = SearchFilter(sort_by="price", sort_order="desc")
    assert filter7.has_filters is True
    params = filter7.to_query_params()
    assert params == {"sort_by": "price", "sort_order": "desc"}


def test_invalid_price_range():
    with pytest.raises(ValidationError):
        SearchFilter(min_price=100.0, max_price=50.0)


def test_zero_min_price():
    with pytest.raises(ValidationError):
        SearchFilter(min_price=0.0)


def test_zero_max_price():
    with pytest.raises(ValidationError):
        SearchFilter(max_price=0.0)


def test_negative_min_price():
    with pytest.raises(ValidationError):
        SearchFilter(min_price=-10.0)


def test_negative_max_price():
    with pytest.raises(ValidationError):
        SearchFilter(max_price=-10.0)


def test_equal_min_max_price():
    filter8 = SearchFilter(min_price=50.0, max_price=50.0)
    assert filter8.min_price == 50.0
    assert filter8.max_price == 50.0


def test_invalid_sort_by():
    with pytest.raises(ValidationError):
        SearchFilter(sort_by="invalid")


def test_invalid_sort_order():
    with pytest.raises(ValidationError):
        SearchFilter(sort_order="invalid")


def test_serialization():
    filter3 = SearchFilter(
        query="laptop",
        min_price=500.0,
        max_price=2000.0,
        categories=["Electronics", "Computers"],
        in_stock=True,
        sort_by="price",
        sort_order="asc",
    )
    data = filter3.model_dump()
    assert data["query"] == "laptop"
    assert data["min_price"] == 500.0
    assert data["max_price"] == 2000.0
    assert data["categories"] == ["Electronics", "Computers"]
    assert data["in_stock"] is True
    assert data["sort_by"] == "price"
    assert data["sort_order"] == "asc"
