from fastapi import APIRouter, Depends

from bar_service.dependencies import get_bar_service
from bar_service.schemas.bar_schemas import Bar
from bar_service.services.bar_service import BarService
from shared.models.bar_models import BarResponse


router = APIRouter()


@router.get("/bar", status_code=200)
async def bar_endpoint(foo_id: int, bar_service: BarService = Depends(get_bar_service)):
    bar: Bar = await bar_service.get_bar(foo_id)

    bar_response: BarResponse = BarResponse(
        foo_id=bar.foo_id,
        bar_name=bar.bar_name
    )

    return bar_response
