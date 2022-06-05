from typing import Optional, List

from fastapi import APIRouter, Depends

from dals.carting_dal import CartingDal
from db.config import async_session
from db.models.carting import Carting
from dependencies import get_carting_dal

router = APIRouter()


@router.post("/cartings")
async def create_carting(name: str, address: str, session_price: int,
                         carting_dal: CartingDal = Depends(get_carting_dal)):
    return await carting_dal.create_carting(name, address, session_price)


@router.get("/cartings")
async def get_all_cartings() -> List[Carting]:
    async with async_session() as session:
        async with session.begin():
            caring_dal = CartingDal(session)
            return await caring_dal.get_all_cartings()


@router.put("/cartings/{carting_id}")
async def update_book(carting_id: int,
                      name: Optional[str] = None,
                      address: Optional[str] = None,
                      session_price: Optional[int] = None,
                      caring_dal: CartingDal = Depends(get_carting_dal)):
    return await caring_dal.update_carting(carting_id, name, address, session_price)
