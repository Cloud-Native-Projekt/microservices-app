from fastapi import Depends
from bar_service.repositories.implementations.bar_repository import BarRepository
from bar_service.repositories.interfaces.iface_bar_repository import BarRepositoryInterface
from bar_service.services.bar_service import BarService


async def get_bar_repository() -> BarRepositoryInterface:
    return BarRepository()


async def get_bar_service(bar_repository: BarRepositoryInterface = Depends(get_bar_repository)):
	return BarService(bar_repository)
