from dataclasses import dataclass

from base_repository import BaseRepository


@dataclass
class User:
    id: int
    name: str
    email: str
    age: int


@dataclass
class UserCreate:
    name: str
    email: str
    age: int


@dataclass
class UserUpdate:
    name: str | None = None
    email: str | None = None
    age: int | None = None


@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int


@dataclass
class ProductCreate:
    name: str
    price: float
    stock: int


@dataclass
class ProductUpdate:
    name: str | None = None
    price: float | None = None
    stock: int | None = None


def test_create_returns_entity_with_id():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    user_data = UserCreate(name="Alice", email="alice@example.com", age=30)
    user = repo.create(user_data)
    assert user.id == 1
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert user.age == 30


def test_ids_are_auto_incremented():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    user1 = repo.create(UserCreate(name="Alice", email="alice@example.com", age=30))
    user2 = repo.create(UserCreate(name="Bob", email="bob@example.com", age=25))
    assert user1.id == 1
    assert user2.id == 2


def test_get_returns_entity_if_found():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    created = repo.create(UserCreate(name="Alice", email="alice@example.com", age=30))
    retrieved = repo.get(created.id)
    assert retrieved is not None
    assert retrieved.name == "Alice"


def test_get_returns_none_if_not_found():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    result = repo.get(999)
    assert result is None


def test_get_all_returns_all_entities():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    repo.create(UserCreate(name="Alice", email="alice@example.com", age=30))
    repo.create(UserCreate(name="Bob", email="bob@example.com", age=25))
    all_users = repo.get_all()
    assert len(all_users) == 2


def test_update_modifies_non_none_fields():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    user = repo.create(UserCreate(name="Alice", email="alice@example.com", age=30))
    update_data = UserUpdate(age=31)
    updated = repo.update(user.id, update_data)
    assert updated is not None
    assert updated.age == 31
    assert updated.name == "Alice"
    assert updated.email == "alice@example.com"


def test_update_returns_none_if_entity_not_found():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    update_data = UserUpdate(age=31)
    result = repo.update(999, update_data)
    assert result is None


def test_delete_removes_entity_and_returns_true():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    user = repo.create(UserCreate(name="Alice", email="alice@example.com", age=30))
    result = repo.delete(user.id)
    assert result is True
    assert repo.get(user.id) is None


def test_delete_returns_false_if_not_found():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    result = repo.delete(999)
    assert result is False


def test_repository_with_product_type():
    repo = BaseRepository[Product, ProductCreate, ProductUpdate]()
    product = repo.create(ProductCreate(name="Laptop", price=999.99, stock=50))
    assert product.id == 1
    assert product.name == "Laptop"
    assert product.price == 999.99


def test_multiple_repositories_are_independent():
    users_repo = BaseRepository[User, UserCreate, UserUpdate]()
    products_repo = BaseRepository[Product, ProductCreate, ProductUpdate]()
    users_repo.create(UserCreate(name="Alice", email="alice@example.com", age=30))
    products_repo.create(ProductCreate(name="Laptop", price=999.99, stock=50))
    assert len(users_repo.get_all()) == 1
    assert len(products_repo.get_all()) == 1


def test_empty_repository_returns_empty_list():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    all_users = repo.get_all()
    assert len(all_users) == 0


def test_update_with_all_none_fields_leaves_unchanged():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    user = repo.create(UserCreate(name="Alice", email="alice@example.com", age=30))
    update_data = UserUpdate()
    updated = repo.update(user.id, update_data)
    assert updated is not None
    assert updated.name == "Alice"
    assert updated.email == "alice@example.com"
    assert updated.age == 30


def test_deleted_entities_not_in_get_all():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    user1 = repo.create(UserCreate(name="Alice", email="alice@example.com", age=30))
    user2 = repo.create(UserCreate(name="Bob", email="bob@example.com", age=25))
    repo.delete(user1.id)
    all_users = repo.get_all()
    assert len(all_users) == 1
    assert all_users[0].name == "Bob"


def test_update_multiple_fields():
    repo = BaseRepository[User, UserCreate, UserUpdate]()
    user = repo.create(UserCreate(name="Alice", email="alice@example.com", age=30))
    update_data = UserUpdate(name="Alicia", age=31)
    updated = repo.update(user.id, update_data)
    assert updated is not None
    assert updated.name == "Alicia"
    assert updated.age == 31
    assert updated.email == "alice@example.com"
