from typing import Union

from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user module"],
    # dependencies=[],
    # responses={404:{"description":"Not Found"}},
)

@router.get("/")
def read_root():
    return {"message": "기본 user router"}


@router.get("/detail/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}