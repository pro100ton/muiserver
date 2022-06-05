from db.config import async_session
from dals.carting_dal import CartingDal


async def get_carting_dal():
    async with async_session() as session:
        async with session.begin():
            yield CartingDal(session)