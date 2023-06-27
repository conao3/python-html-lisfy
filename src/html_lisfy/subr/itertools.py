from typing import Iterable, Callable
import typing

import more_itertools


T = typing.TypeVar('T')

def takewhile_inclusive(pred: Callable[[T], bool], peekable: more_itertools.peekable[T]) -> Iterable[T]:
    while True:
        try:
            x = peekable.peek()
        except StopIteration:
            break

        if pred(x):
            yield next(peekable)
        else:
            break
