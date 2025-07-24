from datetime import datetime
from bar_service.repositories.interfaces.iface_bar_repository import BarRepositoryInterface
from bar_service.schemas.bar_schemas import Bar


class BarRepository(BarRepositoryInterface):

    async def get_bar(self, foo_id: int) -> Bar:
        # Simulate fetching Bar by Foo ID
        # In a real implementation, this would interact with a database or external service

        timestamp: str = datetime.now().isoformat()

        return Bar(
            foo_id=foo_id,
            bar_id=foo_id + 100,  # Example logic to generate a Bar ID
            bar_name=f"Bar Name {foo_id}",
            bar_description=f"Description for Bar {foo_id}",
            bar_timestamp=timestamp
        )
