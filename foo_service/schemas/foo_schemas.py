from typing import Optional
from pydantic import BaseModel

from shared.models.bar_models import BarResponse


class Foo(BaseModel):
    foo_id: int
    foo_name: str


class FooBarResult(BaseModel):
    foo: Foo
    bar: BarResponse
