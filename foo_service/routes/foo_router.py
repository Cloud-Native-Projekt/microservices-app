from fastapi import APIRouter, Depends

from foo_service.dependencies import get_foobar_service
from foo_service.services.foobar_service import FooBarService


router = APIRouter()


@router.get("/foobar", status_code=200)
async def foobar_endpoint(foo_id: int, foobar_service: FooBarService = Depends(get_foobar_service)):
    return await foobar_service.get_foo(foo_id)
