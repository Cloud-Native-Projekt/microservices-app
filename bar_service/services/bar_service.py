from bar_service.repositories.interfaces.iface_bar_repository import BarRepositoryInterface
from bar_service.schemas.bar_schemas import Bar


class BarService():

    def __init__(self, bar_repository: BarRepositoryInterface):
        self.bar_repository = bar_repository


    async def get_bar(self, foo_id: int) -> Bar:
        """Fetch Foo and Bar data and return as FooBar."""

        bar: Bar = await self.bar_repository.get_bar(foo_id)
        if not bar:
            raise ValueError(f"Bar for Foo with id {foo_id} not found")

        return bar
