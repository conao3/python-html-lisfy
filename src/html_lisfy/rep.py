from typing import Optional

import more_itertools

from . import reader
from . import types


def read(x: str) -> Optional[types.Value]:
    stream = more_itertools.peekable(x)
    res = reader.read(stream, eof_error_p=False, eof_value=types.ValueElement(tag='EOF'))
    if isinstance(res, types.ValueElement) and res.tag == 'EOF':
        return None
    return res


def eval(x: Optional[types.Value]) -> Optional[types.Value]:
    return x


def print(x: Optional[types.Value]) -> Optional[str]:
    if x is None:
        return None

    return x.lisfy()


def rep(x: str) -> Optional[str]:
    return print(eval(read(x)))
