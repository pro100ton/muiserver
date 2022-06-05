from typing import List, Optional

from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.carting import Carting


class CartingDal():
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_carting(self, name: str, address: str, session_price: int):
        new_carting = Carting(name=name, address=address, session_price=session_price)
        self.db_session.add(new_carting)
        await self.db_session.flush()

    async def get_all_cartings(self) -> List[Carting]:
        q = await self.db_session.execute(select(Carting).order_by(Carting.id))
        return q.scalars().all()

    async def update_carting(self, carting_id: int, name: Optional[str], address: Optional[str],
                             session_price: Optional[int]):
        q = update(Carting).where(Carting.id == carting_id)
        if name:
            q = q.values(name=name)
        if address:
            q = q.values(address=address)
        if session_price:
            q = q.values(session_price=session_price)
        # make sure the entities we have in memory will by up to date with the new values we updated
        q.execution_options(synchronize_session="fetch")
        await self.db_session.execute(q)
