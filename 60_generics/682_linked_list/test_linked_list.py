from dataclasses import dataclass

from linked_list import LinkedList, Node


def test_node_stores_value_and_next():
    node = Node(10)
    assert node.value == 10
    assert node.next is None


def test_append_adds_to_end():
    lst = LinkedList[int]()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    assert lst.size() == 3


def test_prepend_adds_to_beginning():
    lst = LinkedList[int]()
    lst.append(20)
    lst.prepend(10)
    assert lst.find(10) == 10
    assert lst.size() == 2


def test_find_returns_item_if_found():
    lst = LinkedList[int]()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    assert lst.find(20) == 20


def test_find_returns_none_if_not_found():
    lst = LinkedList[int]()
    lst.append(10)
    lst.append(20)
    assert lst.find(999) is None


def test_remove_returns_true_when_item_removed():
    lst = LinkedList[int]()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    result = lst.remove(20)
    assert result is True
    assert lst.size() == 2
    assert lst.find(20) is None


def test_remove_returns_false_when_item_not_found():
    lst = LinkedList[int]()
    lst.append(10)
    result = lst.remove(999)
    assert result is False


def test_is_empty_returns_true_for_empty_list():
    lst = LinkedList[int]()
    assert lst.is_empty() is True


def test_is_empty_returns_false_for_non_empty_list():
    lst = LinkedList[int]()
    lst.append(10)
    assert lst.is_empty() is False


def test_size_returns_correct_count():
    lst = LinkedList[int]()
    assert lst.size() == 0
    lst.append(10)
    assert lst.size() == 1
    lst.append(20)
    assert lst.size() == 2
    lst.remove(10)
    assert lst.size() == 1


def test_linked_list_with_strings():
    lst = LinkedList[str]()
    lst.append("hello")
    lst.append("world")
    assert lst.find("hello") == "hello"
    assert lst.find("world") == "world"


def test_linked_list_with_custom_class():
    @dataclass
    class Song:
        title: str
        artist: str

    lst = LinkedList[Song]()
    song1 = Song("Imagine", "John Lennon")
    song2 = Song("Hey Jude", "The Beatles")
    lst.append(song1)
    lst.append(song2)
    assert lst.find(song1) == song1


def test_remove_from_empty_list_returns_false():
    lst = LinkedList[int]()
    result = lst.remove(10)
    assert result is False


def test_find_in_empty_list_returns_none():
    lst = LinkedList[int]()
    result = lst.find(10)
    assert result is None


def test_multiple_append_prepend_maintain_order():
    lst = LinkedList[int]()
    lst.append(20)
    lst.prepend(10)
    lst.append(30)
    assert lst.find(10) == 10
    assert lst.find(20) == 20
    assert lst.find(30) == 30


def test_removing_only_element_results_in_empty_list():
    lst = LinkedList[int]()
    lst.append(10)
    lst.remove(10)
    assert lst.is_empty() is True
    assert lst.size() == 0


def test_remove_first_occurrence_only():
    lst = LinkedList[int]()
    lst.append(10)
    lst.append(20)
    lst.append(10)
    lst.remove(10)
    assert lst.size() == 2
    assert lst.find(10) == 10


def test_repr_shows_chain():
    lst = LinkedList[int]()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    assert repr(lst) == "LinkedList(10 -> 20 -> 30)"


def test_repr_shows_empty_list():
    lst = LinkedList[int]()
    assert repr(lst) == "LinkedList()"


def test_repr_with_strings():
    lst = LinkedList[str]()
    lst.append("hello")
    lst.append("world")
    assert repr(lst) == "LinkedList('hello' -> 'world')"


def test_iteration_works():
    lst = LinkedList[int]()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    values = []
    for value in lst:
        values.append(value)
    assert values == [10, 20, 30]


def test_iteration_on_empty_list():
    lst = LinkedList[int]()
    values = list(lst)
    assert values == []


def test_list_conversion():
    lst = LinkedList[int]()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    assert list(lst) == [1, 2, 3]


def test_node_uses_generics():
    assert hasattr(Node, "__type_params__")
    assert len(Node.__type_params__) == 1
    assert Node.__type_params__[0].__name__ == "T"


def test_linked_list_uses_generics():
    assert hasattr(LinkedList, "__type_params__")
    assert len(LinkedList.__type_params__) == 1
    assert LinkedList.__type_params__[0].__name__ == "T"
