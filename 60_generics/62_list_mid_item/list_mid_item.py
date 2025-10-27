def get_mid_item[T](items: list[T]) -> T:
    if not items:
        raise ValueError("List is empty")

    mid_index = len(items) // 2
    if len(items) % 2 == 0:
        mid_index -= 1

    return items[mid_index]
