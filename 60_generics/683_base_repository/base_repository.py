class BaseRepository[T, TCreate, TUpdate]:
    def __init__(self) -> None:
        self._storage: dict[int, T] = {}
        self._next_id = 1

    def create(self, data: TCreate) -> T:
        entity_data = vars(data).copy()
        entity_data["id"] = self._next_id
        entity = type("Entity", (), entity_data)()
        for field_name, field_value in entity_data.items():
            setattr(entity, field_name, field_value)
        self._storage[self._next_id] = entity
        self._next_id += 1
        return entity

    def get(self, entity_id: int) -> T | None:
        return self._storage.get(entity_id)

    def get_all(self) -> list[T]:
        return list(self._storage.values())

    def update(self, entity_id: int, data: TUpdate) -> T | None:
        entity = self._storage.get(entity_id)
        if entity is None:
            return None
        update_data = vars(data)
        for field_name, field_value in update_data.items():
            if field_value is not None:
                setattr(entity, field_name, field_value)
        return entity

    def delete(self, entity_id: int) -> bool:
        if entity_id in self._storage:
            del self._storage[entity_id]
            return True
        return False
