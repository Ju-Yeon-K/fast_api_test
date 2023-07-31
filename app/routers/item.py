from typing import Union

from fastapi import APIRouter

from app.utils import item_utils, user_utils

router = APIRouter(
    prefix="/item",
    tags=["item module"],
    # dependencies=[],
    # responses={404:{"description":"Not Found"}},
)

@router.get("/")
def read_root():
    return {"message": "기본 item router"}


@router.get("/detail/{user_id}")
def read_item(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}