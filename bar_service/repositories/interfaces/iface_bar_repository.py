from abc import ABC, abstractmethod

from bar_service.schemas.bar_schemas import Bar


class BarRepositoryInterface(ABC):

	@abstractmethod
	async def get_bar(self, foo_id: int) -> Bar:
		pass
