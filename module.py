from typing import TypeVar

addable_type = TypeVar("addable_type", int, float, str)


def addition(a: addable_type, b: addable_type) -> addable_type:
    return a + b


print(addition(3, 1))
