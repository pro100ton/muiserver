from typing import Optional, List

import uvicorn
from fastapi import FastAPI

from dals.carting_dal import CartingDal
from db.config import async_session, engine, Base
from db.models.carting import Carting

app = FastAPI()


@app.on_event("startup")
async def startup():
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def hello_world():
    return "hello_world"


@app.post("/cartings")
async def create_carting(name: str, address: str, session_price: int):
    async with async_session() as session:
        async with session.begin():
            caring_dal = CartingDal(session)
            return await caring_dal.create_carting(name, address, session_price)


@app.get("/cartings")
async def get_all_cartings() -> List[Carting]:
    async with async_session() as session:
        async with session.begin():
            caring_dal = CartingDal(session)
            return await caring_dal.get_all_cartings()


@app.put("/cartings/{carting_id}")
async def update_book(carting_id: int,
                      name: Optional[str] = None,
                      address: Optional[str] = None,
                      session_price: Optional[int] = None):
    async with async_session() as session:
        async with session.begin():
            caring_dal = CartingDal(session)
            return await caring_dal.update_carting(carting_id, name, address, session_price)


if __name__ == '__main__':
    uvicorn.run("app:app", port=1111, host='127.0.0.1')
