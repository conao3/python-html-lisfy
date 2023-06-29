from __future__ import annotations

from typing import Optional
import itertools

import more_itertools

from . import types
from . import subr


def read_element(input_stream: more_itertools.peekable[str]) -> types.ValueElement:
    _ = subr.reader.peek_char(True, input_stream, recursive_p=True)

    tag = ''.join(subr.itertools.takewhile_inclusive(lambda x: (not x.isspace()) and x not in '/>', input_stream))

    peek = subr.reader.peek_char(True, input_stream, recursive_p=True)

    if peek == '/':
        next(input_stream)  # Skip '/'
        subr.reader.ensure_char('>', input_stream, recursive_p=True)
        return types.ValueElement(tag=tag, void=True)

    subr.reader.ensure_char('>', input_stream, recursive_p=True)

    child: list[str | types.Value] = []

    while True:
        body = ''.join(itertools.takewhile(lambda x: x != '<', input_stream))

        if body:
            child.append(body)

        peek = subr.reader.peek_char(True, input_stream, recursive_p=True)

        if peek == '/':
            subr.reader.ensure_char('/', input_stream)
            subr.reader.ensure_char(tag, input_stream)
            subr.reader.ensure_char('>', input_stream)
            break

        r = read(input_stream, recursive_p=True)
        child.append(r)

    return types.ValueElement(tag=tag, value=child)


def read(
    input_stream: more_itertools.peekable[str],
    eof_error_p: bool = True,
    eof_value: Optional[types.Value] = None,
    recursive_p: bool = False,
) -> types.Value:
    peek = subr.reader.peek_char(True, input_stream, False, 'EOF', recursive_p=recursive_p)

    if peek == 'EOF':
        if eof_error_p:
            raise types.ReaderError('Unexpected EOF')

        if eof_value is None:
            raise ValueError('eof_value must be provided if eof_error_p is False')

        return eof_value

    if peek == '<':
        next(input_stream)  # Skip '<'
        return read_element(input_stream)

    return read_element(input_stream)
