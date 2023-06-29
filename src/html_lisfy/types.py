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
    def lisfy(self, minify: bool=False) -> str:
        raise NotImplementedError


class ValueElement(Value):
    tag: str
    value: list[str | Value] = []
    void: bool = False

    def lisfy(self, minify: bool=False) -> str:
        if self.void:
            return f'({self.tag} ((void . t)))'

        str_values: list[str] = []
        for v in self.value:
            if isinstance(v, str):
                str_values.append(v)
                continue

            str_values.append(v.lisfy(minify=minify))

        return f'({self.tag} nil {" ".join(str_values)})'
