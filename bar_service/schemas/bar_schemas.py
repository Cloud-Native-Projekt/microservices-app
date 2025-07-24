from pydantic import BaseModel


class Bar(BaseModel):
    foo_id: int
    bar_id: int
    bar_name: str
    bar_description: str
    bar_timestamp: str
