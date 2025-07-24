from fastapi import Depends
from foo_service.repositories.implementations.foo_repository import FooRepository
from foo_service.repositories.interfaces.iface_foo_repository import FooRepositoryInterface
from foo_service.services.foobar_service import FooBarService


async def get_foo_repository() -> FooRepositoryInterface:
    return FooRepository()


async def get_foobar_service(foo_repository: FooRepositoryInterface = Depends(get_foo_repository)):
	return FooBarService(foo_repository)
