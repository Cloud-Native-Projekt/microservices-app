from pydantic import BaseModel


class BarResponse(BaseModel):
    foo_id: int
    bar_name: str
