from foo_service.repositories.interfaces.iface_foo_repository import FooRepositoryInterface
from foo_service.schemas.foo_schemas import Foo, FooBarResult
from shared.models.bar_models import BarResponse
from shared.service_caller import service_get


class FooBarService():

    def __init__(self, foo_repository: FooRepositoryInterface):
        self.foo_repository = foo_repository


    async def get_foo(self, foo_id: int) -> FooBarResult:
        """Fetch Foo and Bar data and return as FooBar."""

        foo: Foo = await self.foo_repository.get_foo(foo_id)
        if not foo:
            raise ValueError(f"Foo with id {foo_id} not found")

        bar: BarResponse = await service_get(
            service_name="bar_service",
            path="/bar",
            data_model=BarResponse,
            params={"foo_id": foo_id}
        )

        foobar: FooBarResult = FooBarResult(foo=foo, bar=bar)

        return foobar
