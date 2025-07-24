from abc import ABC, abstractmethod

from foo_service.schemas.foo_schemas import Foo


class FooRepositoryInterface(ABC):

	@abstractmethod
	async def get_foo(self, foo_id: int) -> Foo:
		pass
