from __future__ import annotations

import more_itertools

from . import types


def read(
    input_stream: more_itertools.peekable[str],
    eof_error_p: bool = True,
    eof_value: types.Value = types.ValueElement(tag='__EOF__', value='', void=True),
) -> types.Value:
    return types.ValueElement(tag='__EOF__', value='', void=True)
