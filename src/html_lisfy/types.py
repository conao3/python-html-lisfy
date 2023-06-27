from __future__ import annotations
from typing import Optional


import pydantic


## Exceptions

class LisfyError(Exception):
    pass


class ReaderError(LisfyError):
    pass


## Values

class Value(pydantic.BaseModel):
    pass


class ValueElement(Value):
    tag: str
    value: Optional[str | list[Value]] = None
    void: bool = False
