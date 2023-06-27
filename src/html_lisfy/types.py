from __future__ import annotations


import pydantic


## Exceptions

class LisfyError(Exception):
    pass


## Values

class Value(pydantic.BaseModel):
    pass


class ValueElement(Value):
    tag: str
    value: str | list[Value]
    void: bool = False
