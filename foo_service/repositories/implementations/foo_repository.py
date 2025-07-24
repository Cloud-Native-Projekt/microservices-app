from foo_service.repositories.interfaces.iface_foo_repository import FooRepositoryInterface
from foo_service.schemas.foo_schemas import Foo


class FooRepository(FooRepositoryInterface):

	async def get_foo(self, foo_id: int) -> Foo:
		# Simulate fetching Foo by ID
		# In a real implementation, this would interact with a database or external service
		return Foo(
			foo_id=foo_id,
			foo_name=f"Foo Name {foo_id}"
		)
