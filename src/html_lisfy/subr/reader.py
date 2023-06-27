from __future__ import annotations

import more_itertools

from .. import types

def skip_whitespace(input_stream: more_itertools.peekable[str]) -> None:
    while (peek := input_stream.peek(None)) and peek.isspace():
        next(input_stream)


def skip_whitespace_and_ensure(input_stream: more_itertools.peekable[str], expected: str) -> None:
    skip_whitespace(input_stream)

    s = ''.join(more_itertools.take(len(expected), input_stream))

    if s != expected:
        raise types.ReaderError(f'Expected {expected}, but got: {s}')