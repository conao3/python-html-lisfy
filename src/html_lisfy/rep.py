from typing import Optional


def read(x: str) -> Optional[str]:
    return x


def eval(x: Optional[str]) -> Optional[str]:
    return x


def print(x: Optional[str]) -> Optional[str]:
    return x


def rep(x: str) -> Optional[str]:
    return print(eval(read(x)))
