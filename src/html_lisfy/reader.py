from __future__ import annotations

import more_itertools

from . import types
from . import subr


def read_element(
    input_stream: more_itertools.peekable[str],
) -> types.ValueElement:
    next(input_stream)  # Skip '<'

    subr.reader.skip_whitespace(input_stream)

    tag = ''.join(subr.itertools.takewhile_inclusive(lambda x: (not x.isspace()) and x != '>', input_stream))
    subr.reader.skip_whitespace(input_stream)

    peek = input_stream.peek(None)
    if peek is None:
        raise types.ReaderError('Unexpected EOF')

    if peek == '/':
        next(input_stream)  # Skip '/'
        subr.reader.skip_whitespace_and_ensure(input_stream, '>')
        return types.ValueElement(tag=tag, void=True)

    if peek != '>':
        raise types.ReaderError(f'Expected ">", but got: {peek}')

    next(input_stream)  # Skip '>'

    body = ''.join(subr.itertools.takewhile_inclusive(lambda x: x != '<', input_stream))
    subr.reader.skip_whitespace_and_ensure(input_stream, '<')
    subr.reader.skip_whitespace_and_ensure(input_stream, '/')
    subr.reader.skip_whitespace_and_ensure(input_stream, tag)
    subr.reader.skip_whitespace_and_ensure(input_stream, '>')

    return types.ValueElement(tag=tag, value=body)


def read(
    input_stream: more_itertools.peekable[str],
    eof_error_p: bool = True,
    eof_value: types.Value = types.ValueElement(tag='__EOF__', value='', void=True),
) -> types.Value:
    subr.reader.skip_whitespace(input_stream)

    peek = input_stream.peek(None)

    if peek is None:
        if eof_error_p:
            raise types.ReaderError('Unexpected EOF')
        return eof_value

    if peek == '<':
        return read_element(input_stream)

    return types.ValueElement(tag='__EOF__', value='', void=True)
