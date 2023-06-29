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
    attr: dict[str, str] = {}
    value: list[str | Value] = []

    def lisfy(self, minify: bool=False) -> str:
        str_values: list[str] = []
        for v in self.value:
            if isinstance(v, str):
                str_values.append(v)
                continue

            str_values.append(v.lisfy(minify=minify))

        str_attrs = [f'({k} . "{v}")' for k, v in self.attr.items()]
        str_attr = f'({" ".join(str_attrs)})' if str_attrs else 'nil'

        str_body = ' '.join([self.tag, str_attr, *str_values])
        return f'({str_body})'
